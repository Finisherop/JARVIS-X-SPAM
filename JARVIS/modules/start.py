from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• 💌𝐂𝐎𝐌𝐌𝐀𝐍𝐃💌 •", data="help_back")
    ],
    [
        Button.url("• 💌𝐂𝐡𝐚𝐧𝐧𝐞𝐥💌 •", "https://t.me/NEXT_TOPPPER"),
        Button.url("• 💌𝐒𝐮𝐩𝐩𝐨𝐫𝐭💌 •", "https://t.me/NEXT_TOPPPER")
    ],
    [
        Button.url("• 💌𝐑𝐄𝐏𝐎💌 •", "https://github.com/Finisherop/JARVIS-X-SPAM")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        ANNIE = await event.client.get_me()
        bot_name = ANNIE.first_name
        bot_id = ANNIE.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **🇲𝐘 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : [𝐍𝐎𝐓𝐓𝐘 𝐁𝐎𝐘](https://t.me/II_ABOUT_FINISHER_II)**\n\n"
        TEXT += f"»» **𝐍𝐎𝐓𝐓𝐘𝐁𝐎𝐘 𝕍2 :** `M 1.8.31`\n"
        TEXT += f"»» ** 𝑷𝒚𝒕𝒉𝒐𝒏 :** `3.11.3`\n"
        TEXT += f"» ** 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒗𝒆𝒓𝒔𝒊𝒐𝒏 :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
              event.chat_id,
                    "https://telegra.ph/file/0bff810c9cade084f4848.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
