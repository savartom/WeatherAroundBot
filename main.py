from all_imports import *


def main():
    # Создаём объект Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Обработчик команды помощи
    help_handler = CommandHandler('help', help_command)
    # Обработчик погоды сейчас
    weather_now_handler = MessageHandler(WEATHER_NOW, weather_now_command)
    # Обработчик погоды на завтра
    weather_tomorrow_handler = MessageHandler(WEATHER_TOMORROW, weather_tomorrow_command)
    # Обработчик выбора прогноза погоды
    forecast_handler = MessageHandler(FORECAST, forecast)
    # Обработчик прогноза погоды
    weather_forecast_handler = MessageHandler(WEATHER_FORECAST_2 | WEATHER_FORECAST_3 |
                                              WEATHER_FORECAST_4 | WEATHER_FORECAST_5 |
                                              WEATHER_FORECAST_6, weather_forecast_command)
    # Обработчик установки уведомлений
    notification_handler = MessageHandler(NOTIFICATION, notification)
    # Удаление установленных уведомлений
    delete_notification_handler = MessageHandler(DELETE_NOTIFICATION, delete_notification_command)
    # Обработчик возвращения назад
    back_handler = MessageHandler(BACK, back_command)
    # Обработчик сообщений
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND & ~ALL_COMMAND, text_command)

    # Стартовый сценарий
    application.add_handler(start_conversation_handler)
    # Стартовый сценарий
    application.add_handler(change_location_conversation_handler)
    # Команда помощи
    application.add_handler(help_handler)
    # Погода сейчас
    application.add_handler(weather_now_handler)
    # Погода завтра
    application.add_handler(weather_tomorrow_handler)
    # Выбор прогноза погоды
    application.add_handler(forecast_handler)
    # Прогноз погоды
    application.add_handler(weather_forecast_handler)
    # Уведомления
    application.add_handler(notification_handler)
    # Стартовый сценарий
    application.add_handler(add_notification_conversation_handler)
    # Удаление уведомлений
    application.add_handler(delete_notification_handler)
    # Возвращение назад
    application.add_handler(back_handler)
    # Обработка прочих сообщения
    application.add_handler(text_handler)

    # Запускаем приложение
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s -  %(message)s', level=logging.INFO
    )
    logger = logging.getLogger(__name__)
    main()
