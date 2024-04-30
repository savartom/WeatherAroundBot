from bot_commands.weather_requests.data_processing import data_processing
from bot_commands.weather_requests.weather_forecast import weather_forecast
from config import STANDARD_MARKUP
import datetime


# Прогноз погоды на завтра
async def weather_tomorrow_command(update, context):
    # Если не выбрано местоположение
    if 'location' not in context.user_data:
        # Сообщаем об этом
        await update.message.reply_text(
            'Не выбран населённый пункт.',
            reply_markup=STANDARD_MARKUP
        )
        return

    # Получаем данные
    data = weather_forecast(1, context.user_data['location'])[0]
    data['date'] = datetime.datetime.now().date() + datetime.timedelta(days=1)

    # Обрабатываем их
    message = data_processing(data, context.user_data['location_name'])

    # Отправляем сообщение
    await update.message.reply_text(
        message,
        reply_markup=STANDARD_MARKUP
    )
