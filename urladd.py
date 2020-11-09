import logging
import configparser

from bs4 import BeautifulSoup
import requests

import feedback

try:
    # add loger
    logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

    # its for simple use
    def inp():
        return input(">> ")

    # url site
    while True:
        try:
            print("URL")
            url = inp()
            #url = "https://dszn.ru/press-center/news?gclid=Cj0KCQjwreT8BRDTARIsAJLI0KIw-WwIuCC2SeHttRB224etxIO9HakfvUanUbnfrNdBIOHF0jMo5-4aAlK3EALw_wcB#news/tab/day_map_all"
            resp = requests.get(url)
            if resp.status_code == 404:
                print("ERROR 404")
                continue
            resp = resp.text
            soup = BeautifulSoup(resp, 'html.parser')
        except requests.exceptions.ConnectionError:
            print("Conection error")
            logging.error(f"ADDRL:-:CONNECTION ERROR: cant connect to >> {url} <<")
            continue
        except requests.exceptions.MissingSchema:
            print("URL error. Wrong url")
            logging.error(f"ADDURL:-:MISSING SCHEMA: wrong url >> {url} <<")
            continue
        print("\n\nCheckpoint\n\n")
        break

    # time search
    while True:
        print('<tag classes="id">text</tag>')
        print("TAG")
        tag = inp()
        print("CLASSES")
        classes = inp()
        print(
            "ID\n"
            "if id a dinamic value press enter"
            )
        id = inp()
        #tag = "p"
        #classes = "0"
        #id = "page-date text-light"

        # empty input
        if (tag == None) or (classes == None):
            print("Empty input. Return to checkpoint")
            continue
        
        # serch all time string
        if classes == "class":
            time_string = soup.findAll(tag, class_ = id)
        else:
            time_string = soup.findAll(tag, classes = id)
        
        if len(time_string) == 0:
            print("Dont find string. Please check input\n")
            continue
        print("\n\nCheckpoint\n\n")
        break

    while True:
        for num, el in enumerate(time_string):
            print(f"{num}. {el}")
        try:
            time_num = int(inp())
            #time_num = 0
        except ValueError:
            print("Input must be INT type")
            continue
        if (time_num < 0) or (time_num > len(time_string)):
            print("This string doesn't exsist")
            continue
        link_search = time_string[time_num]
        print("\n\nCheckpoint\n\n")
        break

    # saves block
    while True:
        print("<tag classes = id> text in string </tag>")
        print(link_search)
        to_save = ["id", "text in string"]
        print("What we need save to can parse. What be editetd and can tracked")
        for num, el in enumerate(to_save):
            print(f"{num}. {el}")
        print("Select")
        select = inp()
        if select == "0":
            saves_type = select
            saves = link_search.get(classes) #save id in string
            print("\n\nCheckpoint\n\n")
            break
        elif select == "1":
            saves_type = select
            saves = link_search.text #save text from line
            print("\n\nCheckpoint\n\n")
            break
        else:
            print("This item doesn't exsist")
            continue

    # search url string
    while True:
        print("Mooving on strings in html document")
        print("up or down")
        search_steps = []
        while True:
            step = inp()
            if step == "0":
                break       
            elif step == "up":
                link_search = link_search.findPrevious()
                print(link_search, end= "\n\n")
                search_steps.append(step)
                continue
            elif step == "down":
                link_search = link_search.findNext()
                print(link_search, end= "\n\n")
                search_steps.append(step)
                continue
            elif (step != 'up') or (step != 'down'):
                print('Input must be "up" or "down"')
                continue
        print("\n\nCheckpoint\n\n")
        break

    # get href tag and full url
    while True:
        print(link_search['href'])
        print("Input text to complete url")
        full_url = inp()
        #full_url = "https://dszn.ru"
        print(f"{full_url}{link_search['href']}")
        break

    # conf section
    steps_in_str = ""
    for el in search_steps:
        steps_in_str += el + " "
    print("Input name for confing section (whithout space)")
    conf_sec_name = inp()
    config = configparser.ConfigParser()
    config.add_section(conf_sec_name)
    config.set(conf_sec_name, "URL", url)
    config.set(conf_sec_name, "TAG", tag)
    config.set(conf_sec_name, "CLASSES", classes)
    config.set(conf_sec_name, "ID", id)
    config.set(conf_sec_name, "TIME_NUM", str(time_num))
    config.set(conf_sec_name, "SAVES_TYPE", saves_type)
    config.set(conf_sec_name, "SAVES", saves)
    config.set(conf_sec_name, "SEARCH_STEPS", steps_in_str)
    config.set(conf_sec_name, "FULL_URL", full_url)

    with open("sections.ini", "a") as sections:
        sections.write(conf_sec_name + " ")

    with open("parse_conf.ini", "a") as conf_file:
        config.write(conf_file)

except:
    logging.exception("Hmmmm")
    feedback.feedback()