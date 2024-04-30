# Обработка данных погоды
def data_processing(data, name):
    # Дата
    date = '.'.join(str(data['date']).split('-')[::-1])
    # Температура воздуха
    temperature = data['temperature']
    if temperature > 0:
        temperature = f'+{temperature}'
    # Облачность
    cloudiness = {'CLEAR': 'Ясно', 'PARTLY': 'Малооблачно',
                  'SIGNIFICANT': 'Переменная облачность',
                  'CLOUDY': 'Облачно', 'OVERCAST': 'Пасмурно'}[data['cloudiness']]
    # Влажность воздуха
    humidity = data['humidity']
    # Тип осадков
    precType = {'NO_TYPE': 'без осадков', 'RAIN': 'дождь', 'SLEET': 'мокрый снег',
                'SNOW': 'снег', 'HAIL': 'град'}[data['precType']]
    # Давление
    pressure = data['pressure']
    # Скорость ветра
    windSpeed = data['windSpeed']
    # Направление ветра
    windDirection = {'CALM': 'штиль', 'NORTH': 'северный', 'NORTH_EAST': 'северо-восточный',
                     'EAST': 'восточный', 'SOUTH_EAST': 'юго-восточный', 'SOUTH': 'южный',
                     'SOUTH_WEST': 'юго-Западный', 'WEST': 'западный',
                     'NORTH_WEST': 'северо-западный'}[data['windDirection']]
    return f'🗓️ {date}\n' \
           f'🏙️ {name}\n' \
           f'🌡️ {temperature}°C\n' \
           f'💧 {humidity}%\n' \
           f'⏲️ {pressure} мм рт.ст.\n' \
           f'💨 {windSpeed} м/c, {windDirection}\n' \
           f'☁️ {cloudiness}, {precType}\n'
