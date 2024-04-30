from config import STANDARD_MARKUP


# Команда возвращения назад
async def back_command(update, context):
    await update.message.reply_text(
        'Вот список того, что я умею:',
        reply_markup=STANDARD_MARKUP
    )
