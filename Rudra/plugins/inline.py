import asyncio

from .. import *
from .. import __version__
from ..modules.misc import *
from ..modules.utils import *
from pyrogram.types import *


async def help_menu_logo(answer):
    if var.USERBOT_PICTURE:
        thumb_image = var.USERBOT_PICTURE
    else:
        thumb_image = "https://telegra.ph/file/2a1a01a656b4ab766bad0.jpg"
    button = paginate_plugins(0, PLUGINS, "help")
    answer.append(
        InlineQueryResultPhoto(
            photo_url=f"{thumb_image}",
            title="🥀 Help Menu ✨",
            thumb_url=f"{thumb_image}",
            description=f"🥀 Open Help Menu Of Parth-Userbot ✨...",
            caption=f"""
**🥀 Welcome To Help Menu Of
Parth Userbot » {__version__} ✨...

Click On Below 🌺 Buttons To
Get Userbot Commands.

🌷Powered By : [𝐤𝐢𝐧𝐠 𝐏𝐚𝐫𝐭𝐡](https://t.me/THE_KING_PARTH).**
            """,
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def help_menu_text(answer):
    button = paginate_plugins(0, PLUGINS, "help")
    answer.append(
        InlineQueryResultArticle(
            title="🥀 Help Menu ✨",
            input_message_content=InputTextMessageContent(f"""
**🥀 Welcome To Help Menu Of
Parth Userbot » {__version__} ✨...

Click On Below 🌺 Buttons To
Get Userbot Commands.

🌷Powered By : [𝐤𝐢𝐧𝐠 𝐏𝐚𝐫𝐭𝐡](https://t.me/THE_KING_PARTH).**""",
            disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


@bot.on_inline_query()
@inline_wrapper
async def inline_query_handler(bot, query):
    text = query.query
    if text.startswith("help_menu_logo"):
        answer = []
        answer = await help_menu_logo(answer)
        try:
            await bot.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except Exception as e:
            print(str(e))
            return
    elif text.startswith("help_menu_text"):
        answer = []
        answer = await help_menu_text(answer)
        try:
            await bot.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except Exception as e:
            print(str(e))
            return
    else:
        return
