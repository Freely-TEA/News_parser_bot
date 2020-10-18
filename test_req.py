from bs4 import BeautifulSoup
import requests
import logging
import aiogram
import asyncio


logging.basicConfig(filename='newsparser.bot.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def inp():
    return input(">> ")

#tg_bot section for feedback to me
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
    if __name__ == '__main__':
        asyncio.run(send_message())
        exit() 


def add_url_page():
    while True:
        try:
            print(
                "Введите url страницы c http:// или https://, где можно найти последнюю статью сайта\n"
                "(не url статьи)"
                )
            #global.url = inp()
            url = "https://3dnews.ru/news"
            resp = requests.get(url)
            if resp.status_code == 404:
                print("ERROR 404")
            resp = resp.text
            soup = BeautifulSoup(resp, 'html.parser')
        except requests.exceptions.ConnectionError:
            print("Ошибка соединения, возможно неверно задан url")
            logging.error(f"ConnectionError : Введена ссылка {url}")
            #continue
        except requests.exceptions.MissingSchema:
            print(
                "Не верный формат ссылки"
                "Приведите ссылку к формату http(s)://*.* или http(s)://*.*/*"
                )
            logging.error(f"MissingChema : Введена ссылка {url}")
            #continue
        except:
            logging.exception("hmmmmm")
            feedback()
        print(
            "Подтверждено сохранение ссылки на страницу (надеюсь всё норм)"
            "Переход к точной настройке, будьте готовы"
            "Все действия выполняются на введённой вами странице"
            )
        break

# section of searching last news time
    while True:
        print(
            "Откройтие в браузере данную вами страницу.\n."
            "Далее нажмите пкм на дату последнего поста и иследуйте элемент\n"
            "Вы получите сроку типа <имя_тэга класс(ид)='значение'> дата </имя_тэга>\n"
            "Если получена строка без даты, то проверьте данный нам url и если введено верно то кричите мне @tea_man_in_tg"
            "сo скриншотами того, что вводили и ссылкой на ресурс.\n"
            "Введите наименоваие тега, где находится строка со временем публикации"
            )
        #tag = inp()
        tag = "span"
        print(
            "Далее после тега стоит id или class?\n"
            "1. id\n2. class"
            )
        #separate = inp()
        separate = "2" 
        print("Введите id элемента, следующего после именования тега")
        #id_time = inp()
        id_time = "entry-date"
        if separate == "1":
            time_string = soup.findAll(tag, id = id_time)
        elif separate =="2":
            time_string = soup.findAll(tag, class_ = id_time)
        print(time_string[0])
        print(
            "Выведенная строка поожа на искомую? (дата может отличаться)\n"
            "1. Да\n2. Нет\n3. Никак не получается"
            )
        #breaking = inp()
        breaking = "1"
        if breaking == "1":
            print("Сохранено")
            break
        elif breaking == "2":
            print("Повторим сначала, будьте внимательнее")
            continue
        elif breaking == "3":
            print("Будьте добры прислать мне скриншоты ваших вводов >> @tea_man_in_tg <<")
            break
    while True:
        for i, el in enumerate(time_string):
            print(i + 1, el)
        print("Выберите ту дату, которая является искомой (введите позиционное число)")
        #num = int(inp())
        num = 26
        num -= 1
        print(time_string[num].text)
        print(
            "Это искомая дата?\n"
            "1. Да\n2. Нет\n3. Никак не получается"
            )
        #breaking = inp()
        breaking = "1"
        if breaking == "1":
            time_string = time_string[num]
            last_time = time_string.text
            print("Сохранено")
            break
        elif breaking == "2":
            print("Повторим сначала, будьте внимательнее")
            continue
        elif breaking == "3":
            print("Будьте добры прислать мне скриншоты ваших вводов >> @tea_man_in_tg <<")
            break
       
#section of search last news url
    print(
        "Сейчас будет очень сложно и может не получится с первой попытки\n"
        "Советую взять ручку и листок для упрощения"
        )
    instruction = (
        "Инструкция по дальшим действиям:\n"
        "Вам надо исследовать элемент ссылки на последнюю статью.\n"
        "Он же, как правило, является заголовком.\n"
        "Когда найдёте ссылку на последнюю статью вам надо будет провести путь от даты до ссылки/n"
        "Будет использоваться поиск по элементам как при поиске даты/n"
        "\n"
        "\n"
        "\n"
        "\n"
        "\n"
    )
    while True:
        constructor = ['up', 'up', 'up', 'down']
        #while True:
            #buffer = inp()
            #if buffer == "0":
            #    break
            #constructor.append(buffer)
            #print(constructor)
        for el in constructor:
            if el == "up":
                time_string = time_string.find_previous()
            if el == "down":
                time_string = time_string.find_next()

        time_string = time_string.find_all("a")
        for i, el in enumerate(time_string):
            print(i + 1, el)
        print(
            "Выберите ту строку, в которой находится искомая ссылка (она может быть обрезанной)\n"
            "Если вы не нашли здесь искомую ссылку, введите 0 и перепровеьте комбинацию шагов"
            )
        #breaking = int(inp())
        breaking = 2
        if breaking == 0:
            continue
        break
    breaking -= 1
    time_string = time_string[breaking]
    print(time_string['href'])
    



    
add_url_page()
print(soup.prettify())
#code = 'document.getElementsByClassName("entry-date")[25].innerText'