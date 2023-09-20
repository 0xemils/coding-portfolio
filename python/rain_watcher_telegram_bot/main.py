import config
import language_setup
import menu_markup
from weather_checker import WeatherChecker
from db_manager import DBManager

from datetime import datetime
import logging
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

weather_checker = WeatherChecker()
db = DBManager("rain_bot_data.db")


class SetState(StatesGroup):
    WAITING_FOR_CITY_INPUT = State()
    WAITING_FOR_TIME_INPUT = State()
    WAITING_FOR_MENU_INPUT = State()
    WAITING_FOR_LANG_INPUT = State()
    SETUP_IS_FINISHED = State()


@dp.message_handler(state="*", commands=("start", "setup"))
async def command_start_handler(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["user_first_name"] = message.from_user.first_name
        data["chat_id"] = message.from_user.id

        # If subscriber is found in the database, using the user's last set language
        if db.subscriber_does_exist(chat_id=data["chat_id"]):
            for subscriber in db.get_subscriptions():
                if subscriber[1] == str(data["chat_id"]):
                    data["user_language"] = subscriber[5]
                    # Setting UI text language
                    language_setup.set_language(lang=data["user_language"])
                    # Reloading all the inline keyboards, in order for the language setting to take effect.
                    menu_markup.update()

        # If subscriber is not found, using default settings
        else:
            # By default, the language is set to English
            data["user_language"] = "en"
            db.update_user_language(chat_id=message.from_user.id)
            # Setting UI text language
            language_setup.set_language(lang=data["user_language"])
            # Reloading all the inline keyboards, in order for the language setting to take effect.
            menu_markup.update()

        welcome_message_data = await message.answer(language_setup.welcome_message % data["user_first_name"],
                                                    reply_markup=menu_markup.main_menu,
                                                    parse_mode="Markdown")
        # Storing the welcome/setup message ID to be able to edit it in case user sets another language.
        data["setup_message_id"] = welcome_message_data["message_id"]

    await SetState.WAITING_FOR_MENU_INPUT.set()


@dp.callback_query_handler(state=SetState.WAITING_FOR_MENU_INPUT)
async def bot_start_message(call: types.CallbackQuery, state: FSMContext):
    if call.data == "change-lang":
        async with state.proxy() as data:
            await bot.edit_message_text(chat_id=data["chat_id"],
                                        message_id=data["setup_message_id"],
                                        text=language_setup.setup_message,
                                        reply_markup=menu_markup.lang_menu)
            await SetState.WAITING_FOR_LANG_INPUT.set()

    elif call.data == "continue":
        await call.message.answer(language_setup.city_setup_message,
                                  parse_mode="Markdown")
        await SetState.WAITING_FOR_CITY_INPUT.set()

    await call.answer()


@dp.message_handler(state=SetState.WAITING_FOR_CITY_INPUT)
async def get_user_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            # Checking if the city can be found using OpenWeatherMap
            weather_checker.get_city_coordinates(message.text, data["user_language"])
        except Exception as e:
            await message.answer(text=language_setup.city_not_found)
            await SetState.WAITING_FOR_CITY_INPUT.set()
            return
        else:
            data["city_name"] = message.text
            data["city_coordinates"] = weather_checker.get_city_coordinates(message.text, data["user_language"])

        await message.answer(text=language_setup.time_setup_message,
                             parse_mode="Markdown")

    await SetState.next()


@dp.message_handler(state=SetState.WAITING_FOR_TIME_INPUT)
async def get_event_time(message: types.Message, state: FSMContext):
    try:
        user_time = datetime.strptime(message.text, "%H:%M")
    except Exception as e:
        await message.answer(text=language_setup.incorrect_input)
        await SetState.WAITING_FOR_TIME_INPUT.set()
        return
    else:
        async with state.proxy() as data:
            data["set_time"] = user_time.strftime("%H:%M")
            await message.answer(text=language_setup.confirmation_message % (data["set_time"], data["city_name"]))

            if db.subscriber_does_exist(chat_id=data["chat_id"]):
                print("Existing subscriber data has been updated!")
                db.update_subscription(chat_id=f"{data['chat_id']}",
                                       notification_time=f"{data['set_time']}",
                                       city=f"{data['city_name']}",
                                       city_coordinates=f"{data['city_coordinates']}",
                                       user_language=f"{data['user_language']}")
            else:
                print("New subscriber has been added!")
                db.add_subscriber(chat_id=f"{data['chat_id']}",
                                  notification_time=f"{data['set_time']}",
                                  city=f"{data['city_name']}",
                                  city_coordinates=f"{data['city_coordinates']}",
                                  user_language=f"{data['user_language']}")
            await SetState.SETUP_IS_FINISHED.set()


@dp.message_handler(state=SetState.SETUP_IS_FINISHED)
async def bot_reply(message: types.Message):
    await message.answer(text=language_setup.incorrect_input_setup_message)


@dp.callback_query_handler(state=SetState.WAITING_FOR_LANG_INPUT)
async def set_bot_language(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if call.data == "finnish-lang":
            # Setting the chosen language and updating all the elements:
            data["user_language"] = "fi"
            language_setup.set_language(lang=data["user_language"])
            menu_markup.update()

            await bot.edit_message_text(chat_id=data["chat_id"],
                                        message_id=data["setup_message_id"],
                                        text=language_setup.welcome_message % data["user_first_name"],
                                        reply_markup=menu_markup.main_menu,
                                        parse_mode="Markdown")

            db.update_user_language(chat_id=data["chat_id"], user_language=data["user_language"])

        elif call.data == "chinese-lang":
            data["user_language"] = "zh_cn"
            language_setup.set_language(lang=data["user_language"])
            menu_markup.update()

            await bot.edit_message_text(chat_id=data["chat_id"],
                                        message_id=data["setup_message_id"],
                                        text=language_setup.welcome_message % data["user_first_name"],
                                        reply_markup=menu_markup.main_menu,
                                        parse_mode="Markdown")

            db.update_user_language(chat_id=data["chat_id"], user_language=data["user_language"])

        else:
            data["user_language"] = "en"
            language_setup.set_language(lang=data["user_language"])
            menu_markup.update()

            await bot.edit_message_text(chat_id=data["chat_id"],
                                        message_id=data["setup_message_id"],
                                        text=language_setup.welcome_message % data["user_first_name"],
                                        reply_markup=menu_markup.main_menu,
                                        parse_mode="Markdown")

            db.update_user_language(chat_id=data["chat_id"], user_language=data["user_language"])

    await SetState.WAITING_FOR_MENU_INPUT.set()
    await call.answer()


@dp.message_handler(state="*", commands="unsubscribe")
async def unsubscribe(message: Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(text=language_setup.unsubscribe_message)
        db.unsubscribe(chat_id=data["chat_id"])


async def check_weather():
    current_time = datetime.now().strftime("%H:%M")
    for subscriber in db.get_subscriptions():
        language_setup.set_language(subscriber[5])

        if subscriber[2] == current_time and weather_checker.will_rain(eval(subscriber[4])) and subscriber[6] == 1:
            await bot.send_message(chat_id=subscriber[1], text=language_setup.rain_message % subscriber[3])


scheduler = AsyncIOScheduler()
scheduler.add_job(check_weather, "cron", day_of_week="mon-sun", minute="*/1")

if __name__ == "__main__":
    scheduler.start()
    executor.start_polling(dp, skip_updates=False)
