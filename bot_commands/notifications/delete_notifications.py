from config import STANDARD_MARKUP


# Удаление всех уведомлений
async def delete_notification_command(update, context):
    # Получаем id чата
    chat_id = str(update.message.chat.id)
    # Получаем текущие уведомления
    current_jobs = context.job_queue.get_jobs_by_name(chat_id)
    # Удаляем все уведомления
    for job in current_jobs:
        job.schedule_removal()
    # Отправляем сообщение
    await update.message.reply_text(
        'Уведомления удалены.',
        reply_markup=STANDARD_MARKUP
    )
