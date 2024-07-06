"""Entry point. Checks for user and starts main script"""

# ©️ Dan Gazizullin, 2021-2023
# This file is a part of s1zex Userbot
# 🌐 https://github.com/hikariatama/s1zex
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html
# Adaptator Team modifided s1zex files for Adaptator
# 🌐 https://github.com/s1zexxx/Adaptator

import getpass
import os
import subprocess
import sys

from ._internal import restart

if (
    getpass.getuser() == "root"
    and "--root" not in " ".join(sys.argv)
    and all(trigger not in os.environ for trigger in {"DOCKER", "GOORM"})
):
    print("🚫" * 15)
    print("You attempted to run Adaptator on behalf of root user")
    print("Please, create a new user and restart script")
    print("If this action was intentional, pass --root argument instead")
    print("🚫" * 15)
    print()
    print("Type force_insecure to ignore this warning")
    if input("> ").lower() != "force_insecure":
        sys.exit(1)


if sys.version_info < (3, 8, 0):
    print("🚫 Error: you must use at least Python version 3.8.0")
elif __package__ != "s1zex":  # In case they did python __main__.py
    print("🚫 Error: you cannot run this as a script; you must execute as a package")
else:
    try:
        # If telethon is not installed, just skip to a part of main startup
        # then main.py will through an error and re-install all deps
        import telethon
    except Exception:
        pass
    else:
        try:
            import telethon

            if tuple(map(int, telethon.__version__.split("."))) < (2, 0, 4):
                raise ImportError
        except ImportError:
            print("🔄 Installing telethon...")

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--force-reinstall",
                    "-q",
                    "--disable-pip-version-check",
                    "--no-warn-script-location",
                    "telethon",
                ],
                check=True,
            )

            restart()

        try:
            import pyrogram

            if tuple(map(int, pyrogram.__version__.split("."))) < (2, 0, 103):
                raise ImportError
        except ImportError:
            print("🔄 Installing pyrogram...")

            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "--force-reinstall",
                    "-q",
                    "--disable-pip-version-check",
                    "--no-warn-script-location",
                    "pyrogram",
                ],
                check=True,
            )

            restart()

    try:
        from . import log

        log.init()

        from . import main
    except (ModuleNotFoundError, ImportError) as e:
        print(f"{str(e)}\n🔄 Attempting dependencies installation... Just wait ⏱")

        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "-q",
                "--disable-pip-version-check",
                "--no-warn-script-location",
                "-r",
                "requirements.txt",
            ],
            check=True,
        )

        restart()

    if __name__ == "__main__":
        if "S1ZEX_DO_NOT_RESTART" in os.environ:
            del os.environ["S1ZEX_DO_NOT_RESTART"]

        main.s1zex.main()  # Execute main function
