import datetime
import time

from bs4 import BeautifulSoup
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
# from init import find_pre

class weMake():
    def __init__(self):
        pass

    def weMakeTest(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] WE-MAKE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] WE-MAKE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_link_text("We make").click()

        #
        # req = driver.page_source
        # bsObj = BeautifulSoup(req, "html.parser")
        #
        # for title in bsObj.find("div", {"class": "div-content"}).findAll(["h5","p"]):
        #     print("We Make Detail Info : ", title.text)
        #     f.write("We Make Detail Info : %s\n" % (title.text))

        # find_pre.find_pre(driver,logger_console,err_logger)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] WE-MAKE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] WE-MAKE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        time.sleep(1)

    # def request_catalogue(self):
    #     driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div/button').click()
    #     time.sleep(3)
    #     driver.find_element_by_id('btnSend').click()
    #     time.sleep(1)

    def weMakeDetail(driver,logger,logger_console,err_logger):

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] WEMAKE-DETAIL TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] WEMAKE-DETAIL TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        parent = driver.find_elements_by_xpath('//img[@class="card-img-top"]')
        for i in range(len(parent)):
            print(i)
            parent = driver.find_elements_by_xpath('//img[@class="card-img-top"]')
            # try:
            #     parent[i].click()
            #     time.sleep(1)
            #     Alert(driver).accept()
            #     i=i+1
            #     continue
            # except NoAlertPresentException:
            #     pass

            parent[i].click()
            time.sleep(1)
            # find_pre.find_pre(driver, logger_console, err_logger)
            # req = driver.page_source
            # bsObj = BeautifulSoup(req, "html.parser")
            #
            # for title in bsObj.find("div", {"class": "div-content"}).findAll(["h5", "p"]):
            #     print("We Make Detail Info : ", title.text)
            #     f.write("We Make Detail Info : %s\n" % (title.text))

            try:
                Alert(driver).accept()
                i = i + 1
                continue
            except NoAlertPresentException:
                elem = driver.find_elements_by_xpath('//img[@class="card-img-top"]')

            if len(elem) == 0:
                driver.back()
                time.sleep(1)
                i = i + 1
                print("no elem")
                continue
            else:
                for j in range(len(elem)):
                    elem = driver.find_elements_by_xpath('//img[@class="card-img-top"]')
                    elem[j].click()
                    print("click")
                    time.sleep(1)
                    # find_pre.find_pre(driver, logger_console, err_logger)

                    try:
                        Alert(driver).accept()
                        j = j + 1
                        time.sleep(1)
                        continue
                    except NoAlertPresentException:
                        rows = driver.find_elements_by_xpath('//img[@class="card-img-top"]')

                    if len(rows) == 0:
                        driver.back()
                        time.sleep(1)
                        j = j + 1
                        print("no elem")
                        continue
                    else:
                        for k in range(len(rows)):
                            print("*******************")
                            print(k)

                            rows[k].click()
                            time.sleep(1)
                            # find_pre.find_pre(driver, logger_console, err_logger)
                            try:
                                Alert(driver).accept()
                            except NoAlertPresentException:
                                driver.back()
                                time.sleep(1)
                                k = k + 1

                            rows = driver.find_elements_by_xpath('//img[@class="card-img-top"]')

                    driver.back()
                    time.sleep(1)

                driver.back()
                time.sleep(1)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] WEMAKE-DETAIL TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] WEMAKE-DETAIL TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        time.sleep(1)