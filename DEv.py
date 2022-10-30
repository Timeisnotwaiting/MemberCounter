from pyrogram import Client, filters, idle
import os

ID = os.environ["API_ID"]
HASH = os.environ["API_HASH"]
TOKEN = os.environ["BOT_TOKEN"]
SUDO = os.environ["SUDO_USERS"]
CHANNEL_IDS = os.environ["CHANNEL_IDS"]

IDS = CHANNEL_IDS.split(" ")

SUDOS = SUDO.split(" ")

dev = Client(":logger:", api_id=ID, api_hash=HASH, bot_token=TOKEN)

@dev.on_message(filters.command("getinfo"))
async def z(_, m):
    info = []
    for i in IDS:
        MEMBERS = []
        BOTS = []
        DELETED = []
        o = await _.get_chat(i)
        title = o.title
        async for c in _.get_chat_members(i):
            if c.user.is_bot:
                BOTS.append(c.user.id)
            elif c.user.is_deleted:
                DELETED.append(c.user.id)
            else:
                MEMBERS.append(c.user.id)
            s = {"TITLE": title, "MEMBERS": len(MEMBERS), "BOTS": len(BOTS), "DELETED": len(DELETED)}
            info.append(s)
    txt = ""
    for h in info:
        txt += "\n" + h["TITLE"] + "\n"
        txt += "Members :" + h["MEMBERS"] + "\n"
        txt += "Bots :" + h["BOTS"] + "\n"
        txt += "Deleted :" + h["DELETED"] + "\n"

    await m.reply(txt)

dev.start()
print("Bot started successfully..!")
idle()
