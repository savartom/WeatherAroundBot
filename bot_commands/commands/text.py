from config import STANDARD_MESSAGES, STANDARD_MARKUP
from random import choice


# Обработка нестандартных сообщений
async def text_command(update, context):
    await update.message.reply_text(
        choice(STANDARD_MESSAGES),
        reply_markup=STANDARD_MARKUP
    )
