# Copyright (c) 2020 Slavfox
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import os
import subprocess
import sys

from discord.ext import commands

from knifebot.settings import REPO_ROOT


def find_cogs(module):
    return [cog for cog in vars(module).values() if isinstance(cog,
                                                         commands.CogMeta)]


def update_and_restart():
    subprocess.run(["git", "pull"], cwd=REPO_ROOT.resolve())
    os.execl(sys.executable, sys.executable, *sys.argv)
