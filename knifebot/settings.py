# Copyright (c) 2020 Slavfox
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import os
from pathlib import Path
import logging

KNIFEBOT_DIR = Path(__file__).parent
REPO_ROOT = KNIFEBOT_DIR.parent

MODULES = ["ping"]
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
LOGGING_LEVEL = logging.INFO
