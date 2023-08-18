from telebot import TeleBot
from os import getenv

BOT = TeleBot(getenv("TOKEN"))

"""
Аминистратор

- Добавление / Удаление услуг
- Просмотр записей
- Удаление записей
- Добавление / Удаление последних работ
"""