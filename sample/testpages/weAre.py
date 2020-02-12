import datetime
import time

from bs4 import BeautifulSoup

class weAre:
    def __init__(self):
        pass
    def weAreTest(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] WE-ARE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] WE-ARE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_link_text("We are").click()

        # req = driver.page_source
        # bsObj = BeautifulSoup(req, "html.parser")
        #
        # for info in bsObj.findAll(["span","p"]):
        #     print("We Are Text-info : ", info.text)
        #     f.write('We Are Text-info : %s\n' % (info.text))

        # find_pre.find_pre(driver,logger_console,err_logger)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] WE-ARE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] WE-ARE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        time.sleep(1)
