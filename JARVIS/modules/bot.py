import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from config import SUDO_USERS
from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        jarvis = await e.reply(f"☞︎︎︎ 𓆰꯭⎯꯭꯭̽🥂꯭꯭꯭𝐍 ፝֟𝚘 𝚃 ͟𝚃 ͟𝚈 𓂍꯭༎ ⫷ 𝐁 ፝֟ᴏ 𝑦⫸ 🜲⛧‌ٖٖٖٖٖٖٜ𝆺꯭𝅥𝄄꯭꯭𝄄꯭꯭ ꯭𝅥ͦ𝆬𝆺꯭𝅥👻")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await jarvis.edit(f"[🇳ㄖㄒㄒㄚ  👻🇧O̾𝐘  𝐈𝐒  𝐑𝔸E͆ᗪㄚ  💫 ㄒㄖ  𝐅𝐔𝐂𝐊 💥 ](https://t.me/NEXT_TOPPPER)[ 𝐇𝐀𝐓𝐄𝐑𝐒 𝐊𝐈 𝐌𝐀𝐊𝐈𝐂𝐇𝐔𝐓 🥀](https://t.me/NEXT_TOPPPER)  😁😁😁😘\n» `{mp} ᴍꜱ`")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"`BOT IS RESTARTING PLEASE WAIT.`")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» __🇳𝐎𝐓𝐓𝐘 𝐊𝐀 𝗘𝗞 ᗩᑌᖇ BETA 𝘼𝘿𝘿 𝑯𝑶𝑹𝑯𝑨🌸🥀😂..__")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» BSDK...REPLY KRKE KAR !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"YE BHI 𝐍𝐎𝐓𝐓𝐘 𝙺𝙰 𝙷𝙸 𝙱𝙰𝙲𝙷𝙰 𝙷𝙰𝙸.. !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ADD KAR DIYE HAI SUDO..BOT RESTART HO RHA HAI`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» 𝐁𝐒𝐃𝐊 𝐒𝐈𝐑𝐅 𝐍𝐎𝐓𝐓𝐘 𝐇𝐈 𝐒𝐔𝐃𝐎 𝐃𝐄 𝐒𝐊𝐓𝐀 𝐋𝐖𝐃𝐄 😂😂...")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)
        ok = await event.reply(f"YE 𝐍𝐎𝐓𝐓𝐘 𝐁𝐎𝐘 𝐊𝐈 𝐍𝐀𝐉𝐀𝐄𝐒 𝐀𝐔𝐋𝐀𝐃 🤣😂💋...")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:\nPlease set up your HEROKU_APP_NAME`")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("Reply to a message to remove the user.")
            return
        if str(target) not in sudousers:
            await ok.edit("User is not in the sudo list.")
        else:
            new_sudo_users = " ".join([user for user in sudousers.split() if user != str(target)])
            await ok.edit(f"Removed sudo user: `{target}`")
            heroku_var["SUDO_USERS"] = new_sudo_users
    else:
        await event.reply("Only Jarvis can remove sudo users.")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudos(?: |$)(.*)" % hl))
async def show_sudo_users(event):
    if event.sender_id == OWNER_ID:
        sudo_users_list = "𝐍𝐎𝐓𝐓𝐘 Ke Bache hai ye:\n"
        for user_id in SUDO_USERS:
            sudo_users_list += f"- {user_id}\n"
        await event.reply(sudo_users_list)
    else:
        await event.reply("Only NOTTY view the sudo users list.")



