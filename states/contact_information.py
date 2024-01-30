from telebot.handler_backends import State, StatesGroup

class UserInfoState(StatesGroup):
    name = State()
    age = State()
    contry = State()
    city = State()
    telephone_number = State()

class UserEnterData(StatesGroup):
    city = State()