import datetime
import time

from bs4 import BeautifulSoup

class notice:
    def __init__(self):
        pass

    def noticeTest(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] NOTICE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_link_text("Notice").click()
        time.sleep(2)

        # find_pre.find_pre(driver, logger_console, err_logger)
        # filtering 실험
        driver.find_element_by_xpath('//input[@type="search"]').send_keys("Notice")
        driver.find_element_by_link_text("Notice").click()
        time.sleep(2)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] NOTICE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        time.sleep(3)
    def noticeDetail(driver,logger,logger_console,err_logger):
        pages = driver.find_elements_by_xpath('//ul[@class="pagination pagination-rounded"]/li')
        for j in range(len(pages) - 2):

            notices = driver.find_elements_by_xpath('//*[@id="tbNoticeList"]/tbody/tr/td/a')
            for i in range(len(notices)):
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] NOTICE-DETAIL TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE-DETAIL TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

                notices[i].click()
                time.sleep(3)
                # find_pre.find_pre(driver,logger_console,err_logger)
                driver.find_element_by_xpath('//*[@id="wrap"]/div/button').click()  # List
                time.sleep(4)
                # find_pre.find_pre(driver, logger_console, err_logger)
                notices = driver.find_elements_by_xpath('//*[@id="tbNoticeList"]/tbody/tr/td/a')

                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] NOTICE-DETAIL TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE-DETAIL TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

            if j != len(pages) - 3:
                driver.find_element_by_xpath('//*[@id="tbNoticeList_next"]/a').click()
                time.sleep(2)

        time.sleep(3)

