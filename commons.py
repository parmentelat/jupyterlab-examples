#!/usr/bin/env python

"""
a tool to monitor projects that follow the guidelines in this project
"""

import os
import hashlib
from datetime import datetime as DateTime
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass

import colorama
from colorama import Fore, Style

# my first time with click
import click

colorama.init()

@click.group()
# @click.option('--debug/--no-debug', default=False)
def commons_cli():
    """
    click boilerplate
    """
    # click.echo(f"Debug mode is {'on' if debug else 'off'}")
    # pass

PROJECT_PATTERNS = [
    "ue12-p24-intro",
    "ue12-p24-numerique",
    "flotpython-exos-ds",
    "ue12-p24-git",
    "flotpython-slides",
    "flotpython-exos-python",
# not yet duplicated
    "ue22-p23-web",
#    "ue22-p24-web",
    "jupyterlab-examples",
]

COMMONS = [
    # we search at depths 1 and 2, more leads to too long searching times
    'Makefile.book',
    'Makefile.prune',
    'Makefile.toc',
    'Makefile.norm',
    'Makefile.style',
    'style_common.css',
    'jupytext.toml',
    '.readthedocs.yaml',
    'my-book.js',
    # no longer useful with this file as we focus on a specific set of projects
    # 'Makefile.pypi',
]

COMMON_ROOT = Path.home() / 'git/'

PROJECTS = [ p for pattern in PROJECT_PATTERNS
               for p in COMMON_ROOT.glob(pattern)]


def run_commands(commands, *, dry_run=False, interactive=False):
    """
    runs a list of commands
    """
    for command in commands:
        if dry_run:
            print(f"DRY RUN: {command}")
            continue
        if interactive:
            answer = input(f"{command} - OK [y/N] ? ")
            if answer.lower() not in ['y', 'yes']:
                print("skipping")
                continue
        os.system(command)


def spot_common(seed):
    """
    returns a member of the COMMONS list whose name contains seed
    """
    for common in COMMONS:
        if seed in common:
            return common
    print(f"WARNING: could not spot a common file with seed {seed}, using it verbatim")
    return seed


class PrettyTimestamp:
    """
    just a helper to print timestamps in a human readable format
    """
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def __str__(self):
        return DateTime.fromtimestamp(self.timestamp).strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class File:
    """
    the details on one given file
    """
    path: Path
    sha: str
    nbytes: int
    mtime: PrettyTimestamp
    rank: int = -1

    # latest first
    def __lt__(self, other):
        return self.mtime.timestamp > other.mtime.timestamp

    def short(self):
        """
        typically PosixPath('flotpython-exos-ds/notebooks/_static/style_common.css')
        """
        return self.path.relative_to(COMMON_ROOT)

    def path_in_project(self):
        """
        typically notebooks/_static/style_common.css
        """
        return '/'.join(self.short().parts[1:])

    def has_symlink(self):
        """
        is this a symlink or is any of its parents a symlink ?
        """
        for parent in self.path.parents:
            if parent.is_symlink():
                return True
        return False

    def is_pushed(self):
        """
        boolean: this actually describes the whole repo
        """
        dir_ = self.path.parents[0]
        # name = self.path.name
        command = f"git -C {dir_} merge-base --is-ancestor HEAD @{{upstream}}"
        return os.system(command) == 0

    # fine-grained: check for pending changes in any of the 2 areas (added or not)
    def has_pending_changes(self, area):
        """
        area is expected to be either 'index' or 'worktree' or 'any'
        """
        assert area in ['index', 'worktree', 'any']
        dir_ = self.path.parents[0]
        name = self.path.name
        if area == 'index':
            command = f"git -C {dir_} diff-index --quiet --cached HEAD {name}"
        elif area == 'any':
            command = f"git -C {dir_} diff-index --quiet HEAD {name}"
        elif area == 'worktree':
            command = f"git -C {dir_} diff-files --quiet -- {name}"
        return os.system(command) != 0


class Common:
    """
    finds all instances of a common file
    e.g. common = notebooks/Makefile.book
    """

    def __init__(self, common):
        self.common = spot_common(common)
        self.groups = defaultdict(list)

        paths = []
        for depth in 0, 1, 2, 3:
            paths += [
                x for project in PROJECTS
                for x in project.glob(f"{'*/'*depth}{self.common}")
            ]
        files = []

        for path in paths:
            with path.open('rb') as f:
                m = hashlib.sha256()
                m.update(f.read())
                files.append(File(
                    path, m.hexdigest(), path.stat().st_size,
                    PrettyTimestamp(path.stat().st_mtime)))

        files.sort()
        files = [f for f in files if not f.has_symlink()]
        for index, file in enumerate(files):
            file.rank = index

        for file in files:
            self.groups[file.sha].append(file)


    def __repr__(self) -> str:
        return self.common


    def is_ok(self):
        """
        True if all instances of the common file are identical
        """
        return len(self.groups) == 1


    def nb_groups(self):
        """
        how many different versions of the common file are found
        """
        return len(self.groups)


    def nb_files(self):
        """
        how many instances of the common file are found
        """
        return sum(len(files) for files in self.groups.values())


    def files(self, relative):
        """
        prints on stdout the filename for one sample of each group
        if relative is True, the filename is relative to COMMON_ROOT
        """
        for _group, files in self.groups.items():
            file = files[0]
            print(file.path.relative_to(COMMON_ROOT) if relative else file.path)


    def summary(self):
        """
        displays current status for a common file:
        - number of instances found
        - number of groups found
        - outline which is latest
        """

        color = Fore.GREEN if self.is_ok() else Fore.RED

        print(f"{self.common} has {self.nb_files()} instances in {self.nb_groups()} groups")
        for group, files in self.groups.items():
            print(f"Group {group}")
            for file in files:
                red = file.has_pending_changes('worktree')
                green = file.has_pending_changes('index')
                changes = (
                    f"{Fore.YELLOW}M{Style.RESET_ALL}" if red and green
                    else f"{Fore.GREEN}M{Style.RESET_ALL}" if green
                    else f"{Fore.RED}M{Style.RESET_ALL}" if red
                    else " "
                )
                needs_push = " " if file.is_pushed() else f"{Fore.RED}P{Style.RESET_ALL}"
                linecolor = color if file.rank == 0 else ""
                print(f"{changes}{needs_push} {file.rank:02}: "
                      f"{linecolor}{file.nbytes}B  @{file.mtime} {file.short()}")
                print(Style.RESET_ALL, end="")


    def diff(self, rank):
        """
        runs diffs between most recent and previous versions of a common file
        """
        if self.is_ok():
            # print("NO DIFF - common file is consistent across all projects")
            return
        keys = list(self.groups.keys())
        file0 = self.groups[keys[0]][0]
        file1 = self.groups[keys[rank]][0]
        print(f"diff {file0.short()} {file1.short()}")
        os.system(f"diff {file0.path} {file1.path}")


    def adopt(self, rank, dry_run, interactive):
        """
        copies a file from one group to all others
        """
        keys = list(self.groups.keys())
        reference = self.groups[keys[rank]][0]
        for group, files in self.groups.items():
            # skip the reference group
            if group == keys[rank]:
                continue
            # copy the reference file to all the files in the group
            for file in files:
                command = f"rsync -a {reference.path} {file.path}"
                run_commands([command], dry_run=dry_run, interactive=interactive)


    def list_projects(self):
        """
        lists all projects that have that common file
        """
        projects = set()
        for files in self.groups.values():
            for file in files:
                projects.add(file.path.relative_to(COMMON_ROOT).parts[0])
        return projects


    def locate_in_project(self, projectname):
        """
        returns a File object or None
        """
        for files in self.groups.values():
            for file in files:
                if file.path.relative_to(COMMON_ROOT).parts[0] == projectname:
                    return file
        return None



@commons_cli.command()
@click.option('-a', '--aggregate', is_flag=True, help='Aggregate all results')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def list_projects(commons, aggregate):
    """
    lists all projects that have that common file
    """
    aggregated_projects = set()
    commons = commons or COMMONS
    for common in commons:
        common = Common(common)
        projects = common.list_projects()
        aggregated_projects.update(projects)
        if not aggregate:
            print(f"{4*'-'} {common=}: found in projects\n{" ".join(sorted(projects))}")
    if aggregate:
        print(" ".join(sorted(aggregated_projects)))



@commons_cli.command()
@click.option('-r', '--relative', is_flag=True, help='Display relative paths only')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def samples(commons, relative):
    """
    for each mentioned common file, lists one file per group
    with --relative, the filename is relative to COMMON_ROOT

    if no common file is mentioned, all known common files are processed
    """
    commons = commons or COMMONS
    for common in commons:
        common_obj = Common(common)
        print(f"{4*'-'} {common_obj.common}")
        common_obj.files(relative=relative)



@commons_cli.command()
@click.option('-v', '--verbose', is_flag=True, help='Display details')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def summary(commons, verbose):
    """
    for each mentioned common file, shows how many # versions (groups) are found
    if no common file is mentioned, all known common files are processed
    """
    commons = commons or COMMONS
    for common in commons:
        common_obj = Common(common)
        if verbose or not common_obj.is_ok():
            print(f"{4*'-'} {common_obj.common}")
            common_obj.summary()



@commons_cli.command()
@click.option('-r', '--rank', default=1, help='Rank of the group to compare with')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def diff(commons, rank):
    """
    for each mentioned common file, shows the diff between the most recent group
    and the previous version (or use -r to spot another group)
    """
    commons = commons or COMMONS
    for common in commons:
        common_obj = Common(common)
        print(f"{4*'-'} {common_obj.common}")
        common_obj.diff(rank)



@commons_cli.command()
@click.option('-r', '--rank', default=0, help='Rank of the source file')
@click.option('-n', '--dry-run/--no-dry-run', is_flag=True, default=False, help='Dry run')
@click.option('-i', '--interactive/--no-interactive', is_flag=True, default=True,
              help='prompts before copying into each project')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def adopt(commons, rank, dry_run, interactive):
    """
    copies most recent version of a common file to all
    instances of that file in a group
    """
    commons = commons or COMMONS
    for common in commons:
        common_obj = Common(common)
        print(f"{4*'-'} {common_obj.common}")
        common_obj.adopt(rank, dry_run, interactive)



@commons_cli.command()
@click.option('-v', '--verbose', is_flag=True, help='Display details')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def git_status(commons, verbose):
    """
    run git status in all projects that have that common file
    """
    commons = commons or COMMONS
    projects = set()
    for common in commons:
        common = Common(common)
        more = common.list_projects()
        # if verbose:
        #     print(f"{common=}: in projects {sorted(more)}")
        projects.update(more)
    projects = sorted(projects)
    depth = 3 if verbose else 1
    for project in projects:
        print(f"{4*'-'} {project}")
        os.system(f"git -C {COMMON_ROOT / project} rev-parse --abbrev-ref HEAD")
        os.system(f"git -C {COMMON_ROOT / project} la -{depth}")
        os.system(f"git -C {COMMON_ROOT / project} status --short --untracked-files=no")


@commons_cli.command()
@click.option('-n', '--dry-run', is_flag=True, help='display list of projects only')
@click.option('-i', '--interactive/--no-interactive', is_flag=True, default=True,
              help='prompts before copying into each project')
@click.argument('common', metavar='common', envvar="COMMON", nargs=1, type=str)
def git_add(common, dry_run, interactive):
    """
    run git add in all projects that have that common file - requires exactly one argument
    """
    # transform str into Common object
    common = Common(common)
    projects = sorted(common.list_projects())
    for project in projects:
        file = common.locate_in_project(project)
        if not file:
            print(f"OOPS - {file} not found in {project}")
            continue
        if not file.has_pending_changes('worktree'):
            print(f"skipping project {project} - no pending changes in {common}")
            continue
        print(f"{4*'-'} {project}")
        command = f"git -C {COMMON_ROOT / project} add {file.path_in_project()}"
        run_commands([command], dry_run=dry_run, interactive=interactive)


@commons_cli.command()
@click.option('-n', '--dry-run/--no-dry-run', is_flag=True, default=False, help='Dry run')
@click.option('-i', '--interactive/--no-interactive', is_flag=True, default=True,
              help='prompts before copying into each project')
@click.argument('common', metavar='common', envvar="COMMON", nargs=1, type=str)
def git_commit(common, dry_run, interactive):
    """
    performs a git commit in all projects that have that common file - requires exactly one argument
    the message is labelled as 'adopt latest version of <common_file>'

    NOTE: no check is made on the status of the index, it is expected that
    commons.py git-add <common>
    and
    commons.py git-status <common>
    have been run before to make a visual check that only the common file is a pending addition
    """
    # transform str into Common object
    common = Common(common)
    projects = sorted(common.list_projects())
    for project in projects:
        file = common.locate_in_project(project)
        if not file:
            print(f"OOPS - {file} not found in {project}")
            continue
        if file.has_pending_changes('worktree'):
            print(f"WARNING: project {project} "
                  f"still has pending changes in the worktree !! - skipping")
            continue
        if not file.has_pending_changes('index'):
            print(f"skipping project {project} - no pending changes in {common}")
            continue
        commit_message = f"'adopt latest version of {common.common}'"
        command = f"git -C {COMMON_ROOT / project} commit -m{commit_message}"
        print(f"{4*'-'} {project}")
        run_commands([command], dry_run=dry_run, interactive=interactive)


@commons_cli.command()
@click.option('-n', '--dry-run', is_flag=True, help='display list of projects only')
@click.option('-i', '--interactive/--no-interactive', is_flag=True, default=True,
              help='prompts before copying into each project')
@click.option('-f', '--force', is_flag=True, help='Force push')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def git_push(commons, dry_run, interactive, force):
    """
    run git push in all projects that have that common file
    """
    commons = commons or COMMONS
    # used to compute whether a project is pushed
    common0 = None
    projects = set()
    for common in commons:
        common = Common(common)
        # register the first one
        common0 = common0 or common
        more = common.list_projects()
        projects.update(more)
    projects = sorted(projects)
    for project in projects:
        file0 = common0.locate_in_project(project)
        if not file0:
            print(f"OOPS - {file0} not found in {project}")
            continue
        if file0.is_pushed():
            print(f"skipping project {project} - already pushed")
            continue
        print(f"{4*'-'} {project}")
        force_option = " --force" if force else ""
        command = f"git -C {COMMON_ROOT / project} {force_option} push"
        run_commands([command], dry_run=dry_run, interactive=interactive)


if __name__ == '__main__':
    commons_cli()
