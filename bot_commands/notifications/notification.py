from config import NOTIFICATION_MARKUP


# Работа с уведомлениями
async def notification(update, context):
    await update.message.reply_text(
        'Установить или удалить уведомление?',
        reply_markup=NOTIFICATION_MARKUP
    )
