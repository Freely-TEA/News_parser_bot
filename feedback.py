import aiogram
import asyncio


def feedback():
    API_TOKEN = '1084378685:AAFzoIodC-PdhqHkw5XWxvdV3msIMrfLpoQ'
    bot = aiogram.Bot(token=API_TOKEN)
    user_id = '417275099'
    print(
        "Неизвестная ошибка. Я уже получил фидбек, "
        "будьте добры прислать мне скриншоты ваших вводов >> @tea_man_in_tg <<, "
        "а пока бот остановлен")
    async def send_message():
        await bot.send_message(user_id,"АААААААААААААААААААААААААААААААААААААААААА, ЧИНИ БОТА ПАРСЕРА CРОЧНААААААААААА")
        try:
            log = open("app.log", "r")
            await bot.send_document(user_id, document= log)
            log.close()
        except:
            pass
    if __name__ == '__main__':
        asyncio.run(send_message())
        exit()