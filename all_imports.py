from bot_commands.commands.change_location import (
    start_conversation_handler,
    change_location_conversation_handler
)
from bot_commands.commands.help import help_command
from bot_commands.commands.back import back_command
from bot_commands.commands.text import text_command

from bot_commands.weather_requests.weather_now import weather_now_command
from bot_commands.weather_requests.weather_tomorrow import weather_tomorrow_command
from bot_commands.weather_requests.weather_forecast import (
    forecast, weather_forecast_command
)

from bot_commands.notifications.notification import notification
from bot_commands.notifications.add_notifications import add_notification_conversation_handler
from bot_commands.notifications.delete_notifications import delete_notification_command

from tokens import TELEGRAM_TOKEN
from config import (
    ALL_COMMAND, WEATHER_NOW, WEATHER_TOMORROW, WEATHER_FORECAST_2, WEATHER_FORECAST_3,
    WEATHER_FORECAST_4, WEATHER_FORECAST_5, WEATHER_FORECAST_6,
    NOTIFICATION, DELETE_NOTIFICATION, BACK, FORECAST
)

from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update

import logging
