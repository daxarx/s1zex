# ©️ s1zex by Dan Gazizullin, 2021-2023
# ©️ Adaptator by Dima Admiralov, 2022-20?? 
# This file is a part of Adaptator Userbot
# 🌐 https://github.com/s1zexxx/Adaptator
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ---------------------------------------------------------------------------------
# ⠄⠄⠄⠄⡠⣿⢷⣻⣿⣾⣳⡇⢺⠟⠒⠒⠶⢤⣈⠃⢠⡀
# ⠄⠄⠄⢀⣼⡿⠋⢉⣉⣙⠿⠁⢁⣤⣤⣄⡀⠄⠈⠳⢾⣿⣄
# ⠄⠄⠄⢞⡞⠄⣴⣿⡿⠛⠓⠄⠉⠉⠉⠉⠹⣷⣄⠄⠄⠙⢿⣦
# ⠄⢀⣾⡟⠄⣸⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⡀⠄⠰⣿⣆
# ⠄⢸⣿⠁⢸⣿⠄⠄⢸⢸⠄⠄⠄⢸⣆⢠⣀⡀⣧⣨⣻⡀⠄⢻⣿⣦⣀
# ⠄⢸⡇⡀⠘⣿⢰⣐⢾⢿⡀⠄⡀⢨⣎⣻⣷⣶⣿⣿⣿⣇⢀⢸⣿⣿⣿⣷
# ⠄⢸⣣⡇⣧⣿⣿⣿⣿⡎⢳⣟⠿⣿⣿⣏⣉⣿⣿⣿⢻⣿⣿⣾⣿⣿⣿⣿⣦
# ⠄⠄⢼⡇⢹⣿⡏⢠⣿⣿⠄⠉⠄⠄⠈⠄⢹⣿⠟⠼⢻⣿⣿⣿⣿⣿⣿⣿⣿
# ⠄⠄⠈⢿⢈⣿⡛⠘⣿⡇⠄⠄⡀⠄⠄⠄⠈⠉⠁⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿
# ⠄⠄⢀⣿⣼⡿⣿⣀⠄⠄⠄⠄⠃⠄⠄⠄⠄⠄⠄⠘⣻⡏⣿⣿⢻⣿⣿⣿⣿
# ⠄⠄⠾⢻⡇⣿⣸⣦⣀⠄⠄⠐⢟⠙⢻⠃⠄⠄⠄⣾⡏⣷⢻⡹⡟⣿⣿⡟⢿
# ⠄⢀⡴⢻⣇⢿⣷⢻⡟⠻⣶⣤⣀⠉⠄⣀⣴⡿⢣⡟⠄⣿⢸⡇⣰⡟⠻⠃⢸
# ⢠⡏⠄⠄⠈⠻⣿⣏⣷⠄⠈⠻⠉⠛⠛⠉⠄⠄⢛⠄⠄⠻⢠⠁⢛⠁⠄⠄⢸
# ⣼⠄⠄⠄⠄⠄⠈⢿⡘⠃⠄⠄⠄⠄⠄⠄⠠⠈⠄⠄⠄⢠⣸⣠⡞⠄⠄⠄⣿
# ⣤⠄⠄⠄⠄⠄⠄⢸⣇⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⠟⠄⠄⠄⣸⣿
#
# 🥀 Module for Telethon User Bot (Adaptator, s1zex, FTG)
# ---------------------------------------------------------------------------------
# meta developer: @s1zexbee
# meta description: Configurable ping

import datetime
import logging
import time
from telethon.tl.functions.messages import SendMediaRequest
import random
from asyncio import sleep
import os
from .. import loader, utils, version
from telethon.tl.functions.users import GetFullUserRequest
import time
import logging
import re
from ..inline.types import InlineCall
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import Message
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.users import GetFullUserRequest
from datetime import datetime
from math import sqrt
import requests
import git
import datetime
import asyncio
from telethon import types
from telethon.tl.functions.channels import GetFullChannelRequest
from .. import loader, utils
from asyncio import sleep
from datetime import timedelta
from telethon import types
import datetime
import logging
import time
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message
from datetime import datetime
from datetime import timedelta
from telethon import functions
from os import remove
from telethon.tl.functions.channels import LeaveChannelRequest, InviteToChannelRequest 
from telethon.errors import UserIdInvalidError, UserNotMutualContactError, UserPrivacyRestrictedError, BotGroupsBlockedError, ChannelPrivateError, YouBlockedUserError,  MessageTooLongError, \
                            UserBlockedError, ChatAdminRequiredError, UserKickedError, InputUserDeactivatedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantsAdmins, PeerChat, ChannelParticipantsBots
from telethon.tl.functions.messages import AddChatUserRequest
import io
import io
import logging
from io import BytesIO

import requests
from requests import post
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename

from .. import loader, utils
import string
from typing import List
from urllib.parse import quote
import requests
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from datetime import datetime
import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message
from telethon import types
from random import randint
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto
from telethon import errors, functions
from telethon.errors import (
    BotGroupsBlockedError,
    ChannelPrivateError,
    ChatAdminRequiredError,
    ChatWriteForbiddenError,
    InputUserDeactivatedError,
    MessageTooLongError,
    UserAlreadyParticipantError,
    UserBlockedError,
    UserIdInvalidError,
    UserKickedError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
)
from telethon.tl.functions.channels import InviteToChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest, GetCommonChatsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)
from .. import loader, utils

from asyncio import sleep

from datetime import timedelta

from telethon import types

import datetime

import logging

import time

import random

import io

from asyncio import sleep

from os import remove



from telethon import errors, functions

from telethon.errors import (

    BotGroupsBlockedError,

    ChannelPrivateError,

    ChatAdminRequiredError,

    ChatWriteForbiddenError,

    InputUserDeactivatedError,

    MessageTooLongError,

    UserAlreadyParticipantError,

    UserBlockedError,

    UserIdInvalidError,

    UserKickedError,

    UserNotMutualContactError,

    UserPrivacyRestrictedError,

    YouBlockedUserError,

)

from telethon.tl.functions.channels import InviteToChannelRequest, LeaveChannelRequest

from telethon.tl.functions.messages import AddChatUserRequest, GetCommonChatsRequest

from telethon.tl.functions.users import GetFullUserRequest

from telethon.tl.types import (

    ChannelParticipantCreator,

    ChannelParticipantsAdmins,

    ChannelParticipantsBots,

)

from telethon import types



from telethon.tl.types import Message

from datetime import datetime

from datetime import timedelta

from telethon import functions

from telethon.tl.functions.users import GetFullUserRequest

import datetime

from datetime import datetime

from datetime import timedelta



from telethon import functions

from telethon.tl.types import Message

import time

from random import randint

from contextlib import suppress

from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message
from telethon import types
from random import randint
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto
from telethon import errors, functions
from telethon.errors import (
    BotGroupsBlockedError,
    ChannelPrivateError,
    ChatAdminRequiredError,
    ChatWriteForbiddenError,
    InputUserDeactivatedError,
    MessageTooLongError,
    UserAlreadyParticipantError,
    UserBlockedError,
    UserIdInvalidError,
    UserKickedError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
)
from telethon.tl.functions.channels import InviteToChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest, GetCommonChatsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from datetime import datetime
from .. import loader, utils
from asyncio import sleep
from datetime import timedelta
from telethon import types
import datetime
import logging
import time
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message
from datetime import datetime
from datetime import timedelta
from telethon import functions
from os import remove
from telethon.tl.functions.channels import LeaveChannelRequest, InviteToChannelRequest 
from telethon.errors import UserIdInvalidError, UserNotMutualContactError, UserPrivacyRestrictedError, BotGroupsBlockedError, ChannelPrivateError, YouBlockedUserError,  MessageTooLongError, \
                            UserBlockedError, ChatAdminRequiredError, UserKickedError, InputUserDeactivatedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantsAdmins, PeerChat, ChannelParticipantsBots
from telethon.tl.functions.messages import AddChatUserRequest
import io
import string
from typing import List
from urllib.parse import quote
import requests
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from telethon.tl.types import Message

from .. import loader, main, utils

logger = logging.getLogger(__name__)

start = datetime.now()

class PingMod(loader.Module):

    strings = {
        "name": "Ping",
        "loading": "<b><emoji document_id=5460898999575785614>❤️</emoji>𝙿𝙸𝙽𝙶 𝙰𝙳𝙰𝙿𝚃𝙰𝚃𝙾𝚁<emoji document_id=5458654823329050591>❤️</emoji></b>"}

    @loader.command()
    async def ping(self, message: Message):
        """- Get your ping"""
        args = utils.get_args_raw(message)

        starter = datetime.now()

        end = datetime.now()

        pins = (end-start).microseconds / 100

        timing = starter - start

        ping_string = str(pins)

        pingg = ping_string.split(".")

        ping = float(pingg[1])

        time_string = str(timing)

        time_result = time_string.split(".")[0]

        reply = await message.get_reply_message()


        message = await utils.answer(message, self.strings("loading"))
        await message.delete()
        media_files = ("https://x0.at/S1l8.mp4", "https://x0.at/S1l8.mp4")
        try:
            user_id = (
                (
                    (
                        await self.client.het_entity(
                            args if not args.isdigit() else int(args)
                        )
                    ).id
                )
                if args
                else reply.sender_id
            )
        except Exception:
            user_id = self._tg_id
            user = await self._client(GetFullUserRequest(user_id))
            user_ent = user.users[0]

            ping_info = (
                f"<b>[<emoji document_id=5404722257568213390>💜</emoji>]-<emoji document_id=5467550576772390426>✏️</emoji><emoji document_id=5467715911538450661>✏️</emoji><emoji document_id=5467511977901301709>✏️</emoji> -<emoji document_id=5467701196980493651>✏️</emoji><emoji document_id=5467528096913563620>✏️</emoji><emoji document_id=5467880052303600075>✏️</emoji><emoji document_id=5467859213122280132>✏️</emoji>-[<emoji document_id=5404722257568213390>💜</emoji>]</b> <code>{ping}</code>\n\n"
                f"<b>[<emoji document_id=5411472550293154265>🤫</emoji>]-<emoji document_id=5467827297220304662>✏️</emoji><emoji document_id=5467701196980493651>✏️</emoji><emoji document_id=5467795484397543772>✏️</emoji><emoji document_id=5467715911538450661>✏️</emoji><emoji document_id=5467903936616734517>✏️</emoji><emoji document_id=5467452754597258874>✏️</emoji>-[<emoji document_id=5411472550293154265>🤫</emoji>]</b> <code>{time_result}</code>\n"
                f"<b>[<emoji document_id=5415661985947723664>ℹ️</emoji>]-<emoji document_id=5467528096913563620>✏️</emoji><emoji document_id=5467880052303600075>✏️</emoji><emoji document_id=5467428530981706972>✏️</emoji><emoji document_id=5467827297220304662>✏️</emoji>-[<emoji document_id=5415661985947723664>ℹ️</emoji>]</b>\n"
                f"<b>[<emoji document_id=5413370444801647615>🫠</emoji>]-<emoji document_id=5467701196980493651>✏️</emoji><emoji document_id=5467827297220304662>✏️</emoji><emoji document_id=5467835659521630666>✏️</emoji><emoji document_id=5467647668803083362>✏️</emoji><emoji document_id=5467888053827673866>✏️</emoji><emoji document_id=5467827297220304662>✏️</emoji><emoji document_id=5467550576772390426>✏️</emoji><emoji document_id=5467715911538450661>✏️</emoji><emoji document_id=5467795484397543772>✏️</emoji><emoji document_id=5467769203492658451>✏️</emoji><emoji document_id=5467835659521630666>✏️</emoji><emoji document_id=5467647668803083362>✏️</emoji>-[<emoji document_id=5413370444801647615>🫠</emoji>]</b>\n\n"
                f"<b><emoji document_id=5776336086582169312>🔣</emoji><emoji document_id=6179355601227745013>😌</emoji><emoji document_id=5776286368040753186>🔣</emoji>Кᴩᴀᴛᴋᴏᴇ иʍя</b> <emoji document_id=5776057768406421201>➡️</emoji> @{user_ent.username or '☠️'}\n"
                f"<b><emoji document_id=5776336086582169312>🔣</emoji><emoji document_id=6176967693900449962>😞</emoji><emoji document_id=5776286368040753186>🔣</emoji>Иʍя ᴨᴏᴧьɜᴏʙᴀᴛᴇᴧя</b> <emoji document_id=5776057768406421201>➡️</emoji> {user_ent.first_name or '🚫'}\n"
                f"<b><emoji document_id=5776336086582169312>🔣</emoji><emoji document_id=6179188011603855854>😅</emoji><emoji document_id=5776286368040753186>🔣</emoji>Айди</b> <emoji document_id=5776057768406421201>➡️</emoji> <code>{user_ent.id}</code>\n"
            )
            chat_id = message.chat.id
            if chat_id:
                await self.client.send_file(message.peer_id, random.choice(media_files), caption=ping_info)