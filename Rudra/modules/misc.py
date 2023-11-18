from .. import SUDOERS
from pyrogram.types import *
from traceback import format_exc
from typing import Callable


def sudo_user_only(func: Callable) -> Callable:
    async def decorator(client, message: Message):
        if message.from_user.id in SUDOERS:
            return await func(client, message)
        
    return decorator


def cb_wrapper(func):
    async def wrapper(bot, cb):
        from .. import bot
        users = SUDOERS
        if cb.from_user.id not in users:
            await cb.answer(
                "❎ You Are Not A Sudo User❗",
                cache_time=0,
                show_alert=True,
            )
        else:
            try:
                await func(bot, cb)
            except Exception:
                print(format_exc())
                await cb.answer(
                    f"❎ Something Went Wrong, Please Check Logs❗..."
                )

    return wrapper


def inline_wrapper(func):
    async def wrapper(bot, query):
        from .. import bot
        users = SUDOERS
        if query.from_user.id not in users:
            try:
                button = [
                    [
                        InlineKeyboardButton(
                            "💥 Deploy Rudra Userbot ✨",
                            url=f"https://github.com/RUDRA-JAAT/Rudra-User-Bot"
                        )
                    ]
                ]
                await bot.answer_inline_query(
                    query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultPhoto(
                                photo_url=f"https://mallucampaign.in/images/img_1693670648.jpg",
                                title="🥀 Rudra Userbot ✨",
                                thumb_url=f"https://mallucampaign.in/images/img_1693670648.jpg",
                                description=f"🌷 Deploy Your Own Rudra-Userbot 🌿...",
                                caption=f"<b>🥀 Welcome › To › Rudra 🌷\n✅ Userbot v2.0 ✨...</b>",
                                reply_markup=InlineKeyboardMarkup(button),
                            )
                        )
                    ],
                )
            except Exception as e:
                print(str(e))
                await bot.answer_inline_query(
                    query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title="",
                                input_message_content=InputTextMessageContent(
                                    f"||**🥀 Please, Deploy Your Own 𝐏𝐚𝐫𝐭𝐡 𝐔𝐬𝐞𝐫𝐛𝐨𝐭❗...\n\nRepo:** <i>https://github.com/RUDRA-JAAT/Rudra-User-Bot/</i>||"
                                ),
                            )
                        )
                    ],
                )
            except Exception as e:
                print(str(e))
                pass
        else:
           return await func(bot, query)

    return wrapper
