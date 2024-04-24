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
# my first time with click
import click

colorama.init()

@click.group()
# @click.option('--debug/--no-debug', default=False)
def cli():
    # click.echo(f"Debug mode is {'on' if debug else 'off'}")
    pass

COMMONS = [
    'notebooks/Makefile.book',
    'notebooks/Makefile.prune',
    'notebooks/Makefile.style',
    'notebooks/Makefile.toc',
    'notebooks/Makefile.norm',
    'Makefile.pypi',
    'notebooks/_static/style.css',
    'notebooks/_static/style_common.css',
    'jupytext.toml',
    '.readthedocs.yaml',
]

COMMON_ROOT = Path.home() / 'git/'


def spot_common(seed):
    """
    returns a member of the COMMONS list whose name contains seed
    """
    for common in COMMONS:
        if seed in common:
            return common
    raise ValueError(f"no common file found with seed {seed}")


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
        return self.path.relative_to(COMMON_ROOT)

class Common:
    """
    finds all instances of a common file
    e.g. common = notebooks/Makefile.book
    """
    def __init__(self, common):
        self.common = spot_common(common)
        self.groups = defaultdict(list)

        paths = list(COMMON_ROOT.glob(f"*/{self.common}"))
        files = []

        for path in paths:
            with path.open('rb') as f:
                m = hashlib.sha256()
                m.update(f.read())
                files.append(File(
                    path, m.hexdigest(), path.stat().st_size,
                    PrettyTimestamp(path.stat().st_mtime)))

        files.sort()
        for index, file in enumerate(files):
            file.rank = index

        for file in files:
            self.groups[file.sha].append(file)

    def is_ok(self):
        return len(self.groups) == 1

    def nb_groups(self):
        return len(self.groups)

    def nb_files(self):
        return sum(len(files) for files in self.groups.values())

    def files(self, relative):
        """
        prints on stdout all the filename for one sample of each group
        if relative is True, the filename is relative to COMMON_ROOT
        """
        for group, files in self.groups.items():
            file = files[0]
            print(file.path.relative_to(COMMON_ROOT) if relative else file.path)

    def summary(self):
        """
        displays current status for a common file:
        - number of instances found
        - number of groups found
        - outline which is latest
        """

        from colorama import Fore, Back, Style
        color = Fore.GREEN if self.is_ok() else Fore.RED

        print(f"{self.common} has {self.nb_files()} instances in {self.nb_groups()} groups")
        for group, files in self.groups.items():
            print(f"Group {group}")
            for file in files:
                if file.rank == 0:
                    print(color, end="")
                print(f"  {file.rank:02}: {file.nbytes}B  @{file.mtime} {file.short()}")
                if file.rank == 0:
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

    @staticmethod
    def run_commands(commands, dry_run, interactive):
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
                self.run_commands([command], dry_run, interactive)

    def commit(self, dry_run, interactive):
        """
        same logic as adopt, but would do git add / git commit

        the implementation is different though, because at that point
        we have done 'adopt', so now all the files are in the same group...
        """
        print("WARNING: make sure the projects have no pending changes"
              " in their index before running this command")
        for group, files in self.groups.items():
            for file in files:
                dir = file.path.parents[0]
                name = file.path.name
                command = f"git -C {dir} diff-index HEAD {name} | grep -q ."
                # print(command)
                needs_commit = os.system(command) == 0
                # print(f"{file.short()} needs commit: {needs_commit}")
                if needs_commit:
                    commands = [
                        f"git -C {dir} add {name}",
                        f"git -C {dir} commit -m 'adopt {name} with {__file__}'",
                    ]
                    self.run_commands(commands, dry_run, interactive)


def list_projects(common=None):
    """
    lists all projects that have at least a common file
    focus on one specific common file if provided
    """
    projects = set()
    commons = [common] if common else COMMONS
    for common in commons:
        paths = list(COMMON_ROOT.glob(f"*/{common}"))
        for path in paths:
            projects.add(path.relative_to(COMMON_ROOT).parts[0])
    return projects


@cli.command()  # @cli, not @click!
@click.option('-r', '--relative', is_flag=True, help='Display relative paths only')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def files(commons, relative):
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


@cli.command()  # @cli, not @click!
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


@cli.command()  # @cli, not @click!
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


@cli.command()  # @cli, not @click!
@click.option('-r', '--rank', default=0, help='Rank of the source file')
@click.option('-d', '--dry-run/--no-dry-run', is_flag=True, default=False, help='Dry run')
@click.option('-i', '--interactive/--no-interactive', is_flag=True, default=True,
              help='prompts before copying into each project')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def adopt(commons, rank, dry_run, interactive):
    commons = commons or COMMONS
    for common in commons:
        common_obj = Common(common)
        print(f"{4*'-'} {common_obj.common}")
        common_obj.adopt(rank, dry_run, interactive)


@cli.command()  # @cli, not @click!
@click.option('-d', '--dry-run/--no-dry-run', is_flag=True, default=False, help='Dry run')
@click.option('-i', '--interactive/--no-interactive', is_flag=True, default=True,
              help='prompts before copying into each project')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def commit(commons, dry_run, interactive):
    commons = commons or COMMONS
    for common in commons:
        common_obj = Common(common)
        print(f"{4*'-'} {common_obj.common}")
        common_obj.commit(dry_run, interactive)


@cli.command()  # @cli, not @click!
@click.option('-v', '--verbose', is_flag=True, help='Display details')
@click.argument('commons', metavar='common', envvar="COMMONS", nargs=-1, type=str)
def git_status(commons, verbose):
    """
    run git status in all projects that have that common file
    """
    commons = commons or COMMONS
    projects = set()
    for common in commons:
        common = spot_common(common)
        more = list_projects(common)
        if verbose:
            print(f"{common=}: in projects {sorted(more)}")
        projects.update(more)
    projects = sorted(projects)
    for project in projects:
        print(f"{4*'-'} {project}")
        os.system(f"git -C {COMMON_ROOT / project} status --short --untracked-files=no")


if __name__ == '__main__':
    cli()
