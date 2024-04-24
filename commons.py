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

    def diff(self, rank=1):
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
                if dry_run:
                    print(f"DRY RUN: {command}")
                    continue
                if interactive:
                    answer = input(f"{command} - OK ? ")
                    if answer.lower() not in ['y', 'yes']:
                        print("skipping")
                        continue
                os.system(command)


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
@click.option('-c', '--common', envvar="COMMON",
    default=None, help='list filenames, one per group')
@click.option('-r', '--relative', is_flag=True, help='Display relative paths only')
def files(common, relative):
    if common is None:
        for common in COMMONS:
            print(f"{4*'-'} {common}")
            Common(common).files(relative=relative)
    Common(common).files(relative=relative)

@cli.command()  # @cli, not @click!
@click.option('-c', '--common', envvar="COMMON",
    default=None, help='Focus on one specific common file')
@click.option('-v', '--verbose', is_flag=True, help='Display details')
def summary(common, verbose):
    if common is None:
        for common in COMMONS:
            common_obj = Common(common)
            if verbose or not common_obj.is_ok():
                print(f"{4*'-'} {common}")
                common_obj.summary()
    else:
        Common(common).summary()


@cli.command()  # @cli, not @click!
@click.option('-c', '--common', envvar="COMMON",
    default=None, help='Focus on one specific common file')
def diff(common):
    if common is None:
        for common in COMMONS:
            common_obj = Common(common)
            common_obj.diff()
    else:
        Common(common).diff()


@cli.command()  # @cli, not @click!
@click.option('-c', '--common', envvar="COMMON",
    default=None, help='Focus on one specific common file')
@click.option('-r', '--rank', default=0, help='Rank of the source file')
@click.option('-d', '--dry-run/--no-dry-run', is_flag=True, default=True, help='Dry run')
@click.option('-i', '--interactive/--no-interactive', is_flag=True, default=True,
              help='prompts before copying into each project')
def adopt(common, rank, dry_run, interactive):
    if common is None:
        for common in COMMONS:
            common_obj = Common(common)
            common_obj.adopt(rank, dry_run, interactive)
    else:
        Common(common).adopt(rank, dry_run, interactive)


@cli.command()  # @cli, not @click!
@click.option('-c', '--common', envvar="COMMON",
    default=None, help='Focus on one specific common file')
def git_status(common):
    projects = sorted(list_projects(common))
    for project in projects:
        print(f"{4*'-'} {project}")
        os.system(f"git -C {COMMON_ROOT / project} status --short --untracked-files=no")


if __name__ == '__main__':
    cli()
