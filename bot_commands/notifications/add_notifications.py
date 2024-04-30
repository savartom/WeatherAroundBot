from bot_commands.weather_requests.weather_now import weather_now
from bot_commands.weather_requests.data_processing import data_processing
from telegram.ext import MessageHandler, filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardRemove
from config import STANDARD_MARKUP, ADD_NOTIFICATION
import datetime


# Добавление уведомлений
async def add_notification(update, context):
    # Если не выбрано местоположение
    if 'location' not in context.user_data:
        # Сообщаем об этом
        await update.message.reply_text(
            'Не выбран населённый пункт.',
            reply_markup=STANDARD_MARKUP
        )
        # Заканчиваем сценарий
        return ConversationHandler.END
    # Иначе продолжаем
    await update.message.reply_text(
        'Введите время ежедневного уведомления в формате ЧЧ:ММ',
        reply_markup=ReplyKeyboardRemove()
    )
    return 1


# Установка уведомлений
async def set_notification(update, context):
    # Проверяем формат ввода
    try:
        notification_time = datetime.datetime.strptime(update.message.text, '%H:%M')
    except Exception:
        await update.message.reply_text(
            'Несоответствие формату. Введите время в формате ЧЧ:ММ',
            reply_markup=ReplyKeyboardRemove()
        )
        return 1
    # Устанавливаем уведомление
    context.job_queue.run_daily(weather_now_command, notification_time,
                                user_id=update.message.from_user.id,
                                chat_id=update.message.chat.id)
    # Сообщаем об этом
    await update.message.reply_text(
        'Уведомление установлено.',
        reply_markup=STANDARD_MARKUP
    )
    # Заканчиваем сценарий
    return ConversationHandler.END


# Погода в данный момент для уведомлений
async def weather_now_command(context):
    # Получаем данные
    data = weather_now(context.user_data['location'])
    data['date'] = datetime.datetime.now().date()

    # Обрабатываем их
    message = data_processing(data, context.user_data['location_name'])

    # Отправляем сообщение
    await context.bot.send_message(context.job.chat_id,
                                   text=message,
                                   reply_markup=STANDARD_MARKUP
                                   )


# Остановка сценария
async def stop(update, context):
    await update.message.reply_text(
        'Уведомление не было добавлено.',
        reply_markup=STANDARD_MARKUP
    )
    return ConversationHandler.END


# Сценарий добавления уведомления
add_notification_conversation_handler = ConversationHandler(
    # Точка входа в диалог
    entry_points=[MessageHandler(ADD_NOTIFICATION, add_notification)],
    # Состояния внутри диалога
    states={
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_notification)],
    },
    # Точка прерывания диалога
    fallbacks=[CommandHandler('stop', stop)]
)
