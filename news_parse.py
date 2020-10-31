import logging
import configparser
from time import sleep

from bs4 import BeautifulSoup
import requests

import feedback

try:
    # add loger
    logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

    # its for simple use
    def inp():
        return input(">> ")

    while True:
        # get parse setting from conf
        config = configparser.ConfigParser()
        config.read("parse_conf.ini")

        with open("sections.ini", "r") as sections_file:
            sections = sections_file.read()
        
        sections = sections.split()

        for el in sections:
            # read conf file
            url = config.get(el, "url")
            tag = config.get(el, "tag")
            classes = config.get(el, "classes")
            id = config.get(el, "id")
            time_num = config.get(el, "time_num")
            saves = config.get(el, "saves")
            search_steps = config.get(el, "search_steps")
            full_url = config.get(el, "full_url")

            # connect and get site
            try:
                resp = requests.get(url)
                if resp.status_code == 404:
                    logging.error(f"NEWS_PARSE:-:404 ERROR: not found in [{el}] section")
                    continue
                resp = resp.text
                soup = BeautifulSoup(resp, "html.parser")
            except requests.exceptions.ConnectionError:
                logging.error(f"NEWS_PARSE:-:CONNECTION ERROR: cant connect to url in [{el}] section")
                continue
            except requests.exceptions.MissingSchema:
                logging.error(f"NEWS_PARSE:-:MISSING SCHEMA: wrong url in [{el}] section")
                continue
            except:
                logging.exception("IN CONNECT AND GET SITE")

            # tag, classes, id, time_num sections search
            try:
                if (tag == None) or (classes == None):
                    logging.error(f"NEWS_PARSE:-:EMPTY SEARCH INFO: tag or clases == None in {el}] section")
                    continue
            
                if classes == "0":
                    time_string = soup.findAll(tag, class_ = id)
                else:
                    time_string = soup.findAll(tag, classes = id)

                if len(time_string) == 0:
                    logging.error(f"NEWS_PARSE:-:EMPTY SEARCH OUTPUT: not find any string with time in [{el}] section")
                    continue
            except:
                logging.exception("IN TAG, CLASSES, ID, etc")

            # get time string
            try:
                time_num = int(time_num)
            except ValueError:
                logging.error(f"NEWS_PARSE:-:VALUE ERROR: time_num not int in [{el}] section")
                continue
            
            try:
                if saves in time_string[time_num].text:
                    logging.debug(f"Not a news in [{el}]")
                    continue                
                else:
                    link_search = time_string[time_num]
                    search_steps = search_steps.split()
                    saves = link_search.text
                    for step in search_steps:
                        if step == "up":
                            link_search = link_search.findPrevious()
                        elif step == "down":
                            link_search = link_search.findNext()
                        elif (step != 'up') or (step != 'down'):
                            logging.error(f"NEWS_PARSE:-: STEPS ERROR: error in steps in [{el}] sections")
                    print(full_url + link_search['href'])
            except IndexError:
                logging.error(f"NEWS_PARSE:-:INDEX ERROR: doesn exsist this string in [{el}]sections")
            except:
                logging.exception("in steps sections")  

            # update saves in config
            config.set(el, "saves", saves)
            with open("parse_conf.ini", "w") as config_file:
                config.write(config_file)


        sleep(600)

except:
    logging.exception("OH NO")