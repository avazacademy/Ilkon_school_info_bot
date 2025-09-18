# Ilmkon_school_info_bot
Ilmkon_school

📌 Ilmkon School Bot – Texnik Topshiriq (TZ)
🎯 Maqsad

Ilmkon School haqida ota-onalar, o‘quvchilar, o‘qituvchilar va ish izlovchilar uchun qulay ma’lumot berish, maktab e’lonlarini ulashish va murojaatlarni qabul qilish.

👥 Foydalanuvchilar
        Ota-onalar – farzandi haqida ma’lumot, dars jadvali, e’lonlar, to‘lov tugmasi.
        O‘quvchilar – dars jadvali, yangiliklar.
        O‘qituvchilar – o‘z profili (ism, rasm, fan, tajriba).
        Ish izlovchilar – ariza topshirish.
        Adminlar – ma’lumotlarni qo‘shish, o‘chirish va yangilash.

🔑 Asosiy funksiyalar
        1. 📚 Maktab haqida
        Maktab tarixi, manzil, telefon raqamlari.
        Rasm va video lavhalar.
        Yangiliklar / e’lonlar.

2. 👩‍🏫 O‘qituvchilar bo‘limi
        O‘qituvchilar ro‘yxati.
        Har bir o‘qituvchi uchun:
        rasm
        ism-familiya
        mutaxassisligi (fan)
        tajribasi
        Kontakt ma’lumotlari (ixtiyoriy).

3. 🎥 Dars lavhalari
        Foto va videolarni ko‘rish.
        Foydalanuvchi bo‘limdan tanlab dars jarayonlarini ko‘rishi mumkin.

4. 👨‍👩‍👧 Ota-onalar bo‘limi
        Farzandining sinfi, dars jadvali, baholarini ko‘rish (agar tizim mavjud bo‘lsa).
        “To‘lov qilish” tugmasi – bosilganda admin(lar)ga quyidagicha xabar boradi:
        “Ota-ona to‘lov qilishni xohlaydi. Ism: …, Farzandi: …, Sinfi: …”
        Maktab e’lonlari.

5. 📝 Ishga kirish uchun ariza
        Foydalanuvchi quyidagilarni to‘ldiradi:
        Ism, familiya
        Fan
        Tajriba
        Telefon raqam
        (ixtiyoriy) CV fayl
        Ma’lumotlar adminlarga yuboriladi va bazada saqlanishi mumkin.

6. 💳 To‘lov tizimi (soddalashtirilgan)
        API integratsiya yo‘q.
        “To‘lov qilish” tugmasi → admin(lar)ga Telegram xabari yuboradi.
        Admin ota-ona bilan bog‘lanadi.
        Xohlasa, admin panelda “To‘lov so‘rovlari tarixi” saqlanishi mumkin.

7. ⚙️ Admin Panel
        Yangilik va e’lon qo‘shish / o‘chirish.
        O‘qituvchi profillarini qo‘shish / tahrirlash.
        Ishga kirish arizalarini ko‘rish.
        (ixtiyoriy) To‘lov so‘rovlarini ko‘rish.
        🛠 Texnologiyalar
        Telegram Bot API – aiogram (Python).
        Database – SQLite (boshlash uchun) yoki PostgreSQL.
        Admin Panel – Django yoki Flask (web).
        Hosting – Heroku / PythonAnywhere / VPS.

📅 Ish bosqichlari
        Prototip – asosiy menyu, maktab info, o‘qituvchilar, ota-onalar bo‘limi tugmalari.
        Media qo‘shish – dars lavhalari, yangiliklar.
        Ariza bo‘limi – ishga kiruvchilar uchun form.
        Admin Panel – barcha ma’lumotlarni boshqarish.
        To‘lov tugmasi – adminlarga xabar yuboradigan oddiy tizim.

✅ Yakuniy natija
        Foydalanuvchi maktab haqida ma’lumot oladi.
        Ota-ona dars jadvali va e’lonlarni ko‘radi, to‘lov tugmasi orqali admin bilan bog‘lanadi.
        O‘qituvchilar ro‘yxati rasmlari va ma’lumotlari bilan chiqadi.
        Ish izlovchilar ariza yuboradi.
        Adminlar hammasini boshqaradi.
