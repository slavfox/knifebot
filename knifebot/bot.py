# Copyright (c) 2020 Slavfox
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
from typing import Dict, List
from importlib import import_module
from types import ModuleType
import logging

import discord
from discord.ext import commands

from knifebot.helpers import find_cogs
from knifebot.settings import MODULES, DISCORD_TOKEN, LOGGING_LEVEL

logging.basicConfig(level=LOGGING_LEVEL)
logger = logging.getLogger(__name__)

class KnifeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=self._get_prefix,
        )
        self.modules = self.load_modules()

    def load_modules(self) -> Dict[str, ModuleType]:
        modules = {
            module: import_module(f"knifebot.modules.{module}")
            for module in MODULES
        }
        logger.info(f"Loaded %s module(s).", len(modules))
        for module in modules.values():
            for cog in find_cogs(module):
                self.add_cog(cog(self))
        logger.info("Loaded %s cog(s).", len(self._BotBase__cogs))
        return modules

    def _get_prefix(
        self, bot: commands.Bot, message: discord.Message
    ) -> List[str]:
        prefixes = [
            f"<@!{bot.user.id}> ",
            f"<@{bot.user.id}> ",
            f"{bot.user} ",
        ]
        prefixes.sort(key=len, reverse=True)
        return prefixes

if __name__ == "__main__":
    bot = KnifeBot()
    bot.run(DISCORD_TOKEN)
