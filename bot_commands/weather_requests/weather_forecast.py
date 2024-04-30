from bot_commands.weather_requests.data_processing import data_processing
from tokens import YANDEX_WEATHER_TOKEN
from config import STANDARD_MARKUP, FORECAST_MARKUP
import requests
import datetime


# Прогноз погоды
async def forecast(update, context):
    await update.message.reply_text(
        'Выберите день прогноза:',
        reply_markup=FORECAST_MARKUP
    )


# Прогноз погоды на определённое количество дней
def weather_forecast(days, location):
    # Широта и долгота
    latitude, longitude = location
    # Запрос
    query = f"""{{
      weatherByPoint(request: {{ lat: {latitude}, lon: {longitude} }}) {{
        forecast {{
          days(limit: {days}) {{
            parts {{
              day {{
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
          }}
        }}
      }}
    }}"""
    # Получаем ответ
    response = requests.post('https://api.weather.yandex.ru/graphql/query',
                             headers={'X-Yandex-API-Key': YANDEX_WEATHER_TOKEN},
                             json={'query': query}).json()
    # Выбираем нужное
    forecast = response['data']['weatherByPoint']['forecast']['days']
    forecast = list(map(lambda data: data['parts']['day'], forecast))

    return forecast


# Команда прогноза погоды
async def weather_forecast_command(update, context):
    # Если не выбрано местоположение
    if 'location' not in context.user_data:
        # Сообщаем об этом
        await update.message.reply_text(
            'Не выбран населённый пункт.',
            reply_markup=STANDARD_MARKUP
        )
        return

    # Находим количество дней
    n = 2
    for i in range(2, 7):
        if str(i) in update.message.text:
            n = i

    # Получаем данные
    data = weather_forecast(n + 1, context.user_data['location'])[n]
    data['date'] = datetime.datetime.now().date() + datetime.timedelta(days=n)

    # Обрабатываем их
    message = data_processing(data, context.user_data['location_name'])

    # Отправляем сообщение
    await update.message.reply_text(
        message,
        reply_markup=STANDARD_MARKUP
    )
