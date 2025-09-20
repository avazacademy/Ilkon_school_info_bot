from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database.db import add_subject, get_subjects
from keyboards.subjects_kb import subjects_keyboard

sub_router = Router()

from config import ADMIN_ID
  

# O‘qituvchilar tugmasi bosilganda
@sub_router.message(F.text == "👩‍🏫 O‘qituvchilar")
async def show_subjects(message: types.Message):
    kb = subjects_keyboard()
    if kb:
        await message.answer("📚 Quyidagi fanlardan birini tanlang:", reply_markup=kb)
    else:
        await message.answer("❌ Hali fanlar qo‘shilmagan")

# Admin uchun — Fan qo‘shish tugmasi
@sub_router.message(F.text == "➕ Fan qo‘shish")
async def ask_subject(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("⛔ Siz admin emassiz.")
    await message.answer("✍️ Yangi fan nomini kiriting:")

# Fan nomini qabul qilish
@sub_router.message(F.text, lambda msg: msg.from_user.id == ADMIN_ID)
async def add_new_subject(message: types.Message):
    text = message.text.strip()
    if text.startswith("➕") or text in [
        "🏫 Maktab haqida",
        "👩‍🏫 O‘qituvchilar",
        "💳 To‘lov haqida",
        "📝 Ishga ariza"
    ]:
        return  # menyu tugmalarini e’tiborsiz qoldiramiz

    add_subject(text)
    await message.answer(f"✅ Fan qo‘shildi: <b>{text}</b>")
