#
# 🔒 The MIT License (MIT)
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
#
# ---------------------------------------------------------------------------------
# 👾 Module for Adaptator User Bot (based on s1zex 6.0.0)⚠️ Owner @kaio1777 and @yuki_marry
# ---------------------------------------------------------------------------------
# meta developer: @s1zexbee

from .. import loader, utils
import logging
import random

logger = logging.getLogger(__name__)


@loader.tds
class ModsMod(loader.Module):
    """List of all of the modules currently installed"""

    strings = {
        "name": "Mods",
        "amount": "  <emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5352874370148604740>➡️</emoji> <b>{}</b> modules loaded:\n",
        "partial_load": (
            "\n<emoji document_id=5393097151192509026>💬</emoji> <b>it's not all modules"
            " Adaptator is loading</b>"
        ),
        "module": "<emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5352874370148604740>➡️</emoji>",
        "core_module": "<emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5352874370148604740>➡️</emoji>"
    }

    strings_ru = {
        "amount": "<emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5352874370148604740>➡️</emoji> <b>{}</b> модулей:",
        "partial_load": (
            "\n<emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5352874370148604740>➡️</emoji> <b>Это не все модули,"
            " Adaptator загружается</b>"
        ),
        "cmd": "<i><b><code></code></i></b>\n",
        "module": "<emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5352874370148604740>➡️</emoji>",
        "core_module": "<emoji document_id=5352919308391424163>🔥</emoji><emoji document_id=5406876368350751327>〰️</emoji><emoji document_id=5352874370148604740>➡️</emoji>"
    }
    
    @loader.command(
        ru_doc="Показать все установленные модули"
        )
    async def modscmd(self, message):
        """- List of all of the modules currently installed"""

        prefix = f"{self.strings('cmd').format(str(self.get_prefix()))}\n"
        result = f"{self.strings('amount').format(str(len(self.allmodules.modules)))}\n"

        for mod in self.allmodules.modules:
            try:
                name = mod.strings["name"]
            except KeyError:
                name = mod.__clas__.__name__
            emoji = self.strings("core_module") if mod.__origin__.startswith("<core") else self.strings("module")
            result += f"\n {emoji} <code>{name}</code>"

        result += "" if self.lookup("Loader").fully_loaded else f"\n\n{self.strings('partial_load')}"
        result += f"\n\n {prefix}"
        media_files = ("https://te.legra.ph/file/7ba08e8c39c5519d2c869.jpg", "https://te.legra.ph/file/7ba08e8c39c5519d2c869.jpg")
        chat_id = message.chat_id
        if chat_id:
             await self.client.send_file(message.peer_id, random.choice(media_files), caption=result)
             await message.delete()
             
        await utils.answer(message, result, self.strings("loading"))
