# ©️ Dan Gazizullin, 2021-2023
# This file is a part of s1zex Userbot
# 🌐 https://github.com/hikariatama/s1zex
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html
# s1zex Team modifided s1zex files for s1zex
# 🌐 https://github.com/yukimarry/s1zex

import re


def compat(code: str) -> str:
    """
    Reformats modules, built for GeekTG to work with Adaptator
    :param code: code to reformat
    :return: reformatted code
    """
    return "\n".join(
        [
            re.sub(
                r"^( *)from \.\.inline import (.+)$",
                r"\1from ..inline.types import \2",
                re.sub(
                    r"^( *)from \.\.inline import rand[^,]*$",
                    "\1from ..utils import rand",
                    re.sub(
                        r"^( *)from \.\.inline import rand, ?(.+)$",
                        r"\1from ..inline.types import \2\n\1from ..utils import rand",
                        re.sub(
                            r"^( *)from \.\.inline import (.+), ?rand[^,]*$",
                            r"\1from ..inline.types import \2\n\1from ..utils import"
                            r" rand",
                            re.sub(
                                r"^( *)from \.\.inline import (.+), ?rand, ?(.+)$",
                                r"\1from ..inline.types import \2, \3\n\1from ..utils"
                                r" import rand",
                                line.replace("GeekInlineQuery", "InlineQuery").replace(
                                    "self.inline._bot",
                                    "self.inline.bot",
                                ),
                                flags=re.M,
                            ),
                            flags=re.M,
                        ),
                        flags=re.M,
                    ),
                    flags=re.M,
                ),
                flags=re.M,
            )
            for line in code.splitlines()
        ]
    )
