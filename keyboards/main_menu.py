from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏫 Maktab haqida"),
            KeyboardButton(text="👩‍🏫 O‘qituvchilar")],
            [KeyboardButton(text="💳 To‘lov haqida"),   
            KeyboardButton(text="📝 Ishga ariza")],
        ],
        resize_keyboard=True,   # tugmalar ekran o'lchamiga moslashadi
        one_time_keyboard=False # tugmalar doimiy bo‘lib turadi
    )
    return kb



def fan_qush() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="➕ Fan qo‘shish"),
                KeyboardButton(text="🔙 Ortga qaytish")   
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return kb