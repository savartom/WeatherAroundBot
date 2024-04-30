from config import STANDARD_MARKUP


# Команда помощи
async def help_command(update, context):
    await update.message.reply_text(
        'Я бот, умеющий показывать погоду вокруг тебя!\n'
        'Управление происходит с помощью кнопок.',
        reply_markup=STANDARD_MARKUP
    )
