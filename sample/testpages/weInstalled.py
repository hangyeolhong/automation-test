import datetime
import time

from bs4 import BeautifulSoup
# from init import find_pre

class weInstalled:
    def __init__(self):
        pass
    def weInstalledTest(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] WE-installed TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] WE-installed TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_link_text("We installed").click()
        # find_pre.find_pre(driver, logger_console, err_logger)
        elems = driver.find_elements_by_xpath('//img[@class="card-img-top"]')

        for j in range(len(elems)):
            now = datetime.datetime.now()
            logger.debug("[%d.%d.%d %d:%d:%d] WE INSTALLED DETAIL TEST START : index[%d] " % (
                now.year, now.month, now.day, now.hour, now.minute, now.second,j))
            logger_console.debug("[%d.%d.%d %d:%d:%d] WE INSTALLED DETAIL TEST START : index[%d] " % (
                now.year, now.month, now.day, now.hour, now.minute, now.second,j))

            elems[j].click()
            time.sleep(1)

            # find_pre.find_pre(driver, logger_console, err_logger)
            # req = driver.page_source
            # bsObj = BeautifulSoup(req, "html.parser")
            #
            # for info in bsObj.find("div",{"class":"div-content min-height"}).findAll(["span", "p"]):
            #     print("We Installed info : ", info.text)
            #     f.write("We Installed info : %s\n" % (info.text))
            # product detail 조회
            product_detail = driver.find_elements_by_xpath('// *[ @ id = "divRefProdList"] / div / div / a')
            if len(product_detail) > 0:
                for i in range(len(product_detail)):
                    product_detail[i].click()
                    time.sleep(2)
                    # find_pre.find_pre(driver, logger_console, err_logger)
                    driver.back()
                    time.sleep(2)
                    product_detail = driver.find_elements_by_xpath('// *[ @ id = "divRefProdList"] / div / div / a')
                driver.back()

            now = datetime.datetime.now()
            logger.debug("[%d.%d.%d %d:%d:%d] WE INSTALLED DETAIL TEST END : index[%d] " % (
                now.year, now.month, now.day, now.hour, now.minute, now.second,j))
            logger_console.debug("[%d.%d.%d %d:%d:%d] WE INSTALLED DETAIL TEST END : index[%d] " % (
                now.year, now.month, now.day, now.hour, now.minute, now.second,j))

            time.sleep(2)
            driver.back()
            time.sleep(2)
            elems = driver.find_elements_by_xpath('//img[@class="card-img-top"]')

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] WE-installed TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] WE-installed TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        time.sleep(1)