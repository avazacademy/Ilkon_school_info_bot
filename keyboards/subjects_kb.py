from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.db import get_subjects




def subjects_keyboard():
    subjects = get_subjects()
    if not subjects:
        return None

    buttons = []
    row = []
    for idx, (_, name) in enumerate(subjects, start=1):
        row.append(InlineKeyboardButton(text=name, callback_data=f"subject:{name}"))
        if idx % 2 == 0:  
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    return InlineKeyboardMarkup(inline_keyboard=buttons)
