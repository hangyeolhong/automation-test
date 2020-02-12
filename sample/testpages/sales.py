import datetime
import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from init import find_pre

REPETITION = 3

class sales:

    def __init__(self):
        pass

    def salesTest(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SALES TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SALES TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_link_text("Project").click()
        # find_pre.find_pre(driver,logger_console,err_logger)
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SALES TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SALES TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        time.sleep(3)

    def details(driver,logger,logger_console,err_logger):

        elem = driver.find_elements_by_xpath('// *[ @ id = "tbSalesOptntList"] / tbody / tr / td / a')
        for j in range(len(elem)):
            now = datetime.datetime.now()
            logger.debug("[%d.%d.%d %d:%d:%d] SALES-DETAILS TEST START : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-DETAILS TEST START : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))

            print(j)
            elem[j].click()
            time.sleep(2);
            # find_pre.find_pre(driver, logger_console, err_logger)

            # 견적요청, 발송내역 조회 3회 반복
            for i in range(REPETITION):
                driver.find_element_by_id("salesOptntReqModalLabel").click()
                driver.find_element_by_id("salesOptntReqModalLabel").click()
                driver.find_element_by_id("salesOptntDocModalLabel").click()
                driver.find_element_by_id("salesOptntDocModalLabel").click()

            driver.find_element_by_xpath('//*[@id="salesOptntModal"]/div/div/div[3]/button').click()  # CLOSE
            time.sleep(1)

            elem = driver.find_elements_by_xpath('//tr[@role="row"]/td/a')

            now = datetime.datetime.now()
            logger.debug("[%d.%d.%d %d:%d:%d] SALES-DETAILS TEST END : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-DETAILS TEST END : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))

        time.sleep(3)

    def register(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SALES-REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-REGISTER TEST START " % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        # Create

        driver.find_element_by_xpath('//div[@class="row"]/div[@class="col"]/button').click()
        driver.find_element_by_name("salesOptntNm").send_keys("aa")
        driver.find_element_by_name("salesOptntAddr").send_keys("register test")
        driver.find_element_by_name("customNm").send_keys("register test")
        driver.find_element_by_name("salesOptntStartDt").send_keys("2020")
        time.sleep(1)
        driver.find_element_by_name("salesOptntStartDt").send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_name("salesOptntStartDt").send_keys("02")
        time.sleep(1)

        driver.find_element_by_name("salesOptntStartDt").send_keys("02")
        time.sleep(1)
        driver.find_element_by_xpath('//button[@type="submit"]').click()

        find_pre.find_pre(driver,logger_console,err_logger)

        #
        # if driver.find_element_by_xpath('//div[@class="invalid-feedback"]').is_displayed():
        #     print("validation 실패")
        #     driver.find_element_by_name("salesOptntNm").send_keys("register test")  # 재시도

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SALES-REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        time.sleep(1)

    def register_back(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SALES-REGISTER-BACK TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-REGISTER-BACK TEST START " % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_xpath('//div[@class="row"]/div[@class="col"]/button').click()
        time.sleep(2)
        # find_pre.find_pre(driver, logger_console, err_logger)
        driver.find_element_by_xpath('//*[@id="salesOptntForm"]/div[5]/div/button[1]').click()
        time.sleep(1)
        # find_pre.find_pre(driver, logger_console, err_logger)
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SALES-REGISTER-BACK TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-REGISTER-BACK TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        time.sleep(3)

    def modify(driver,logger,logger_console,err_logger):

        elem = driver.find_elements_by_xpath('//i[@class="fa fa-edit fa-2x mr-2"]')

        for j in range(len(elem)):
            now = datetime.datetime.now()
            logger.debug("[%d.%d.%d %d:%d:%d] SALES-MODIFY TEST START : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-MODIFY TEST START : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))

            elem[j].click()
            time.sleep(3)
            # find_pre.find_pre(driver, logger_console, err_logger)
            # driver.find_element_by_name("salesOptntNm").clear()
            driver.find_element_by_name("salesOptntNm").send_keys("ver2.0")
            # driver.find_element_by_name("salesOptntNm").clear()
            driver.find_element_by_name("salesOptntAddr").send_keys("ver2.0")
            # driver.find_element_by_name("salesOptntNm").clear()
            driver.find_element_by_name("customNm").send_keys("ver2.0")
            driver.find_element_by_xpath('//button[@type="submit"]').click()
            # find_pre.find_pre(driver, logger_console, err_logger)
            elem = driver.find_elements_by_xpath('//i[@class="fa fa-edit fa-2x mr-2"]')

            now = datetime.datetime.now()
            logger.debug("[%d.%d.%d %d:%d:%d] SALES-MODIFY TEST END : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-MODIFY TEST END : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            time.sleep(3)
            if j == 0 :
                break

        time.sleep(1)

    def delete(driver,logger,logger_console,err_logger):
        elem = driver.find_elements_by_xpath('//i[@class="fa fa-trash fa-2x"]')

        for j in range(len(elem)):
            now = datetime.datetime.now()
            logger.debug("[%d.%d.%d %d:%d:%d] SALES-DELETE TEST START : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-DELETE TEST START : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            elem[j].click()
            time.sleep(2)
            try:
                Alert(driver).accept()
                time.sleep(2)
            except NoAlertPresentException:
                pass

            elem = driver.find_elements_by_xpath('//i[@class="fa fa-trash fa-2x"]')

            now = datetime.datetime.now()
            logger.debug("[%d.%d.%d %d:%d:%d] SALES-DELETE TEST END : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            logger_console.debug("[%d.%d.%d %d:%d:%d] SALES-DELETE TEST END : index[%d]" % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, j))
            time.sleep(3)
            if j == 0 :
                break
        time.sleep(3)