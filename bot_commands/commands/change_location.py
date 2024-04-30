from tokens import YANDEX_GEOCODE_TOKEN
from config import STANDARD_MARKUP, CHANGE_LOCATION

from telegram.ext import MessageHandler, filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import aiohttp


# Стартовая команда
async def start_command(update, context):
    await update.message.reply_text(
        'Напишите название или адрес населенного пункта, чтобы я показал погоду.',
        reply_markup=ReplyKeyboardRemove()
    )
    return 1


# Получение топонимов: адрес и координаты
async def geocoder(update, context):
    # URI геокодера Яндекса
    geocoder_uri = 'http://geocode-maps.yandex.ru/1.x/'
    # Ответ на запрос
    response = await get_response(geocoder_uri, params={
        'apikey': YANDEX_GEOCODE_TOKEN,
        'format': "json",
        'geocode': update.message.text
    })
    # Выбираем нужное
    data = response['response']['GeoObjectCollection']['featureMember']

    if len(data) == 0:
        await update.message.reply_text(
            'Извините, я вас не понял. Введите название или адрес населенного пункта ещё раз.',
            reply_markup=ReplyKeyboardRemove()
        )
        return 1

    # Создаём или очищаем поля
    context.user_data['names'] = []
    context.user_data['addresses'] = []
    context.user_data['positions'] = []
    # Выбираем первые 5 вариантов
    for geo_object in data[:5]:
        # Сам объект
        geo_object = geo_object['GeoObject']
        # Имя объекта
        name = geo_object['name']
        # Адрес объекта
        address = geo_object['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
        # Координаты объекта
        position = geo_object['Point']['pos']
        # Добавляем в словарь
        context.user_data['names'].append(name)
        context.user_data['addresses'].append(address)
        context.user_data['positions'].append(position)

    # Создаём клавиатуру с вариантами
    address_keyboard = [[address] for address in context.user_data['addresses']]
    markup = ReplyKeyboardMarkup(address_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
        'Выберите подходящий вариант с помощью кнопок:',
        reply_markup=markup
    )

    return 2


# Получение ответа на запрос
async def get_response(url, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            return await resp.json()


# Изменение местоположения
async def change_location(update, context):
    # Если введён один из предложенных вариантов
    if update.message.text in context.user_data['addresses']:
        # Получаем индекс в списке
        index = context.user_data['addresses'].index(update.message.text)
        # Запоминаем местоположение
        longitude, latitude = context.user_data['positions'][index].split()
        name = context.user_data['names'][index]
        context.user_data['location_name'] = name
        context.user_data['location'] = (latitude, longitude)
        # Отправляем сообщение
        await update.message.reply_text(
            'Местоположение было изменено.',
            reply_markup=STANDARD_MARKUP
        )
        # Завершаем сценарий
        return ConversationHandler.END
    # Пробуем ещё раз
    return 2


# Остановка сценария
async def stop(update, context):
    await update.message.reply_text(
        'Местоположение не было изменено',
        reply_markup=STANDARD_MARKUP
    )
    return ConversationHandler.END


# Стартовый сценарий
start_conversation_handler = ConversationHandler(
    # Точка входа в диалог
    entry_points=[CommandHandler('start', start_command)],
    # Состояния внутри диалога
    states={
        # Функция читает ответ на первый вопрос и задаёт второй
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, geocoder)],
        # Функция читает ответ на второй вопрос и завершает диалог
        2: [MessageHandler(filters.TEXT & ~filters.COMMAND, change_location)]
    },
    # Точка прерывания диалога
    fallbacks=[CommandHandler('stop', stop)]
)

# Сценарий изменения местоположения
change_location_conversation_handler = ConversationHandler(
    # Точка входа в диалог
    entry_points=[MessageHandler(CHANGE_LOCATION, start_command)],
    # Состояния внутри диалога
    states={
        # Функция читает ответ на первый вопрос и задаёт второй
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, geocoder)],
        # Функция читает ответ на второй вопрос и завершает диалог
        2: [MessageHandler(filters.TEXT & ~filters.COMMAND, change_location)]
    },
    # Точка прерывания диалога
    fallbacks=[CommandHandler('stop', stop)]
)
