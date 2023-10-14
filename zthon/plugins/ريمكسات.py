import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from hunthon import sarub
from hunthon.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "البحث"

@sarub.sar_cmd(
    pattern="ريماكس ([\s\S]*)",
    command=("ريماكس", plugin_category),
    info={
        "header": "ريمكسـات اغـانـي قصيـره",
        "الاستـخـدام": "{tr}ريماكس + كلمـة",
    },
)
async def remaxsarthon(sarrm):
    ok = sarrm.pattern_match.group(1)
    if not ok:
        if sarrm.is_reply:
            what = (await sarrm.get_reply_message()).message
        else:
            await sarrm.edit("`Sir please give some query to search and download it for you..!`")
            return
    sticcers = await bot.inline_query(
        "spotifybot", f"{(deEmojify(ok))}")
    await sticcers[0].click(sarrm.chat_id,
                            reply_to=sarrm.reply_to_msg_id,
                            silent=True if sarrm.is_reply else False,
                            hide_via=True)
    await sarrm.delete()
    

@sarub.sar_cmd(
    pattern="ريمكس ([\s\S]*)",
    command=("ريمكس", plugin_category),
    info={
        "header": "ريمكسـات اغـانـي قصيـره",
        "الاستـخـدام": "{tr}ريمكس + كلمـة",
    },
)
async def sar(event):
    if event.fwd_from:
        return
    sarr = event.pattern_match.group(1)
    alsarot = "@spotifybot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(zelzal, sarr)
    await tap[0].click(event.chat_id)
    await event.delete()

