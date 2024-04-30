from telegram import ReplyKeyboardMarkup
from telegram.ext import filters

STANDARD_KEYBOARD = [['🌞 Погода сейчас', '⛅ Погода на завтра'],
                     ['🌈 Прогноз погоды'],
                     ['🔔 Уведомления'],
                     ['🌎 Изменить город']]
STANDARD_MARKUP = ReplyKeyboardMarkup(STANDARD_KEYBOARD, one_time_keyboard=False)

FORECAST_KEYBOARD = [['2️⃣ Погода на 2 дня вперёд'],
                     ['3️⃣ Погода на 3 дня вперёд'],
                     ['4️⃣ Погода на 4 дня вперёд'],
                     ['5️⃣ Погода на 5 дней вперёд'],
                     ['6️⃣ Погода на 6 дней вперёд'],
                     ['↩️ Назад']]
FORECAST_MARKUP = ReplyKeyboardMarkup(FORECAST_KEYBOARD, one_time_keyboard=False)

NOTIFICATION_KEYBOARD = [['🔔 Добавить уведомление'],
                         ['🔕 Удалить все уведомления'],
                         ['↩️ Назад']]
NOTIFICATION_MARKUP = ReplyKeyboardMarkup(NOTIFICATION_KEYBOARD, one_time_keyboard=False)

WEATHER_NOW = filters.Regex('🌞 Погода сейчас')
WEATHER_TOMORROW = filters.Regex('⛅ Погода на завтра')
FORECAST = filters.Regex('🌈 Прогноз погоды')
WEATHER_FORECAST_2 = filters.Regex('2️⃣ Погода на 2 дня вперёд')
WEATHER_FORECAST_3 = filters.Regex('3️⃣ Погода на 3 дня вперёд')
WEATHER_FORECAST_4 = filters.Regex('4️⃣ Погода на 4 дня вперёд')
WEATHER_FORECAST_5 = filters.Regex('5️⃣ Погода на 5 дней вперёд')
WEATHER_FORECAST_6 = filters.Regex('6️⃣ Погода на 6 дней вперёд')
NOTIFICATION = filters.Regex('🔔 Уведомления')
ADD_NOTIFICATION = filters.Regex('🔔 Добавить уведомление')
DELETE_NOTIFICATION = filters.Regex('🔕 Удалить все уведомления')
CHANGE_LOCATION = filters.Regex('🌎 Изменить город')
BACK = filters.Regex('↩️ Назад')

ALL_COMMAND = (WEATHER_NOW | WEATHER_TOMORROW | WEATHER_FORECAST_2 | WEATHER_FORECAST_3 |
               WEATHER_FORECAST_4 | WEATHER_FORECAST_5 | NOTIFICATION | ADD_NOTIFICATION |
               WEATHER_FORECAST_6 | DELETE_NOTIFICATION | CHANGE_LOCATION | BACK | FORECAST)

STANDARD_MESSAGES = ['Извините, я не понял ваш запрос. Можете повторить?',
                     'Простите, я не смог распознать ваш запрос. Можете пояснить?',
                     'Пожалуйста, уточните ваш вопрос, я не совсем понял.',
                     'Извините, мне не удалось понять вашу просьбу. '
                     'Может быть, вы можете перефразировать?',
                     'К сожалению, я не могу дать ответ на ваш вопрос, так как не понял его.',
                     'Прошу прощения, но я не понимаю вашего запроса. Можете объяснить подробнее?',
                     'Извините, мне не удалось распознать ваш запрос. Попробуйте еще раз.',
                     'Простите, я не совсем понял, что вы имели в виду. Можете уточнить?',
                     'Извините, я не могу дать ответ на ваш вопрос из-за недостаточной информации.',
                     'Прошу прощения, но я не могу помочь вам, так как не понял ваш запрос.']
