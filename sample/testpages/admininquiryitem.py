import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class admininquiry:
    def __init__(self):
        pass
    def inquiryTest(driver,logger,logger_console):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SIGN-IN TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SIGN-IN TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_id('userDropdown').click()
        driver.find_element_by_id('adminPage').click()
        time.sleep(1)
        # De2O 회사 클릭
        driver.find_element_by_xpath('//*[@id="tbCmpnyList"]/tbody/tr[2]/td[1]').click()


        # for i in range(len(elems)):
        #