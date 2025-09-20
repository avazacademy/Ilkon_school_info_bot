from aiogram import Router, types
from aiogram.filters import Command

from keyboards.main_menu import main_menu, fan_qush
from config import ADMIN_ID
from keyboards.subjects_kb import subjects_keyboard

start_router = Router()

WELCOME_TEXT = """
👋 <b>Assalomu alaykum!</b>

🎓 <b>Ilmkon School</b> botiga xush kelibsiz! 🏫✨

Bu bot orqali siz quyidagi xizmatlardan foydalanishingiz mumkin:  

📘 <i>Maktab haqida ma'lumot</i>  
👩‍🏫 <i>O‘qituvchilar ro‘yxati</i>  
💳 <i>To‘lov haqida ma'lumot</i>  
📝 <i>Ishga ariza yuborish</i>  

📢 Eng so‘nggi yangiliklar va e’lonlarni ham shu yerdan kuzatib boring!  

⬇️ <b>Quyidagi menyudan boshlang:</b>
"""

@start_router.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.from_user.id not in ADMIN_ID:   # 👈 foydalanuvchi oddiy bo‘lsa
        await message.answer(
            WELCOME_TEXT,
            reply_markup=main_menu(),
            disable_web_page_preview=True
        )
    else:  # 👨‍💻 adminlar uchun
        await message.answer("Salom Admin", reply_markup=fan_qush())
