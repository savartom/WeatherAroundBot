from bot_commands.weather_requests.data_processing import data_processing
from tokens import YANDEX_WEATHER_TOKEN
from config import STANDARD_MARKUP
import requests
import datetime


# Погода в данный момент
def weather_now(location):
    # Широта и долгота
    latitude, longitude = location
    # Запрос
    query = f"""{{
      weatherByPoint(request: {{ lat: {latitude}, lon: {longitude} }}) {{
        now {{
          temperature
          cloudiness
          humidity
          precType
          precStrength
          pressure
          windSpeed
          windDirection
        }}
      }}
    }}"""
    # Получаем ответ
    response = requests.post('https://api.weather.yandex.ru/graphql/query',
                             headers={'X-Yandex-API-Key': YANDEX_WEATHER_TOKEN},
                             json={'query': query}).json()
    # Выбираем нужное
    data = response['data']['weatherByPoint']['now']

    return data


# Команда погоды в данный момент
async def weather_now_command(update, context):
    # Если не выбрано местоположение
    if 'location' not in context.user_data:
        # Сообщаем об этом
        await update.message.reply_text(
            'Не выбран населённый пункт.',
            reply_markup=STANDARD_MARKUP
        )
        return

    # Получаем данные
    data = weather_now(context.user_data['location'])
    data['date'] = datetime.datetime.now().date()

    # Обрабатываем их
    message = data_processing(data, context.user_data['location_name'])

    # Отправляем сообщение
    await update.message.reply_text(
        message,
        reply_markup=STANDARD_MARKUP
    )
