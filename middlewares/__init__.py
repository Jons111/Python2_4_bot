from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .Majburiy_azolik import Asosiy_checking

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
   
