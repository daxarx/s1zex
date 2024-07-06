"""Represents current userbot version"""
# ©️ Dan Gazizullin, 2021-2023
# This file is a part of s1zex Userbot
# 🌐 https://github.com/hikariatama/s1zex
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html
# Netfoll Team modifided s1zex files for Netfoll
# 🌐 https://github.com/MXRRI/Netfoll

__version__ = (6, 6, 6)
netver = (7, 7, 7)
netrev = ""
import os
import git

try:
    branch = git.Repo(
        path=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ).active_branch.name
except Exception:
    branch = "main"
