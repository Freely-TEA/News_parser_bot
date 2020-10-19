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
            url = inp()
            #url = "https://3dnews.ru/news"
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
        try:
            tag = inp()
            #tag = "span"
            print("Теперь введите то, что идет далее до знака равно")
            separate = inp()
            #separate = "2" 
            print("Введите значение после знака равно")
            id_time = inp()
            #id_time = "entry-date"
            time_string = soup.findAll(tag, separate = id_time)
            print(time_string[0])
            print(
                "Выведенная строка поожа на искомую? (дата может отличаться)\n"
                "1. Да\n2. Нет\n3. Никак не получается"
                )
        except IndexError:
            print("Не получилось найти строки с данными параметрами")
        breaking = inp()
        #breaking = "1"
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
        num = int(inp())
        #num = 26
        num -= 1
        print(time_string[num].text)
        print(
            "Это искомая дата?\n"
            "1. Да\n2. Нет\n3. Никак не получается"
            )
        breaking = inp()
        #breaking = "1"
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
        #constructor = ['up', 'up', 'up', 'down']
        constructor = []
        while True:
            buffer = inp()
            if buffer == "0":
                break
            constructor.append(buffer)
            print(constructor)
        for el in constructor:
            if el == "up":
                time_string = time_string.find_previous()
            if el == "down":
                time_string = time_string.find_next()

        time_string = time_string.find_all("a")
        for i, el in enumerate(time_string):
            print(i + 1, el)
        print(
            "Выберите ту строку, в которой находится ссылка на последнюю статью \n"
            "Она должна находиться после href= (она может быть обрезанной)\n"
            "Если вы не нашли здесь искомую ссылку, введите 0 и перепровеьте комбинацию шагов"
            )
        breaking = int(inp())
        #breaking = 2
        if breaking == 0:
            continue
        break
    breaking -= 1
    time_string = time_string[breaking]
    while True:
        print("Полученная ссылка")
        print(time_string['href'])
        print(
            "Необходимо ли к ней добавить доменое имя?\n"
            "1. Да\n"
            "2. Нет\n"
            )
        breaking = inp()
        if breaking == "1":
            print("Введите недостающую часть")
            complete_url = inp()
            print("Перейдите по получившейся ссылке для проверки")
            print(complete_url+time_string["href"])
            print(
                "Всё прошло удачно?\n"
                "1. Да\n"
                "2. Нет\n"
            )
            breaking = inp()
            if breaking == "1":
                # Нужно сохранить все переменные в бд, а именно
                # url tag separate id_time last_time constructor time_string['href'] complete_url
                # И ещё добить чутка
                break
            elif breaking == "2":
                print("Повторим")
                continue
            else:
                print("Ошибка ввода. Возврат назад")
                continue
        elif breaking == "2":
            complete_url = ""
            # Нужно сохранить все переменные в бд, а именно
            # url tag separate id_time last_time constructor time_string['href'] complete_url 
            break
                
        else:
            print("Ошибка ввода. Возврат назад")
            continue
    print(url, tag, separate, last_time, constructor, time_string['href'], complete_url  )



    
add_url_page()
