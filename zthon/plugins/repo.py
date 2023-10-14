import base64
import contextlib
import io
import os

from telethon import types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from validators.url import url

from ..core.logger import logging
from ..helpers.functions import delete_conv
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import sarub

LOGS = logging.getLogger(__name__)

# =========================================================== #
#الـعـب بعيد لك                 https://t.me/HunerThon                                        #
# =========================================================== #
Warn = "تخمـط بـدون ذكـر المصـدر - ابلعــك نعــال وراح اهينــك"
REPO_SEARCH_STRING = "<b>╮ جـارِ التحميـل مـن كيثـاب ...♥️╰</b>"
REPO_NOT_FOUND = "<b>⎉╎عذرًا .. لـم استطـع ايجـاد المطلـوب</b>"
# =========================================================== #
#الـسـاروت الـحـمـصـي https://t.me/Y_H_E                                                       
# =========================================================== #


@sarub.sar_cmd(pattern="repo(?:\s|$)([\s\S]*)")
async def alsarot(event):
    alsarot = event.pattern_match.group(1)
    chat = "@GitHub_Download_robot"
    reply_id_ = await reply_id(event)
    sarthon = await edit_or_reply(event, REPO_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            purgeflag = await conv.send_message(zelzal)
        except YouBlockedUserError:
            await sarub(unblock("GitHub_Download_robot"))
            await conv.send_message("/start")
            await conv.get_response()
            purgeflag = await conv.send_message(zelzal)
        repo = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        if not repo.document:
            return await edit_delete(sarthon, REPO_NOT_FOUND, parse_mode="html")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_file(
            event.chat_id,
            repo,
            caption=f"<b>⎉╎الريبـو :- <code>{alsarot}</code></b>\n<b>⎉╎تم التحميـل بواسطـة تيبــثون :- @HunerThon</b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await sarthon.delete()
        await delete_conv(event, chat, purgeflag)
