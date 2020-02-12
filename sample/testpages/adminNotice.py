import datetime
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
# from init import find_pre
from init import whitelabel
# def whitelabel(driver,err_logger, name):
#     try:
#         a = driver.find_element_by_xpath('/html/body/h1')
#         b = driver.find_element_by_xpath('/html/body/div[3]')
#         err_logger.debug("[%s ERROR] %s %s" % (name, a.text, b.text))
#         driver.back()
#         time.sleep(3)
#     except :
#         pass

class adminNotice:
    def __init__(self):
        pass

    def hi(self):
        print('hi')

    def adminNoticeTest(driver, logger, logger_console, err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        driver.find_element_by_id('userDropdown').click()
        driver.find_element_by_id('adminPage').click()
        time.sleep(1)
        driver.find_element_by_link_text('Notice/Document').click()
        time.sleep(1)
        # find_pre.find_pre(driver, logger_console, err_logger)

        #filtering test
        driver.find_element_by_xpath('//input[@type="search"]').send_keys("notice")
        time.sleep(1)

        driver.find_element_by_link_text('Notice/Document').click()
        time.sleep(2)

        # find_pre.find_pre(driver,logger_console,err_logger)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        time.sleep(3)

    def newNotice(driver, logger, logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/button').click()
        time.sleep(1)
        # find_pre.find_pre(driver, logger_console, err_logger)
        driver.find_element_by_name('noticeTitle').send_keys("DE2O 공지")
        driver.find_element_by_xpath('//*[@id="noticeForm"]/div[2]/div/div[1]/div[3]/div[3]/p').send_keys("de2o 공지")
        cmpny = Select(driver.find_element_by_id("noticeAuthCd"))
        cmpny.select_by_value('002')  # specific company
        driver.find_element_by_name('cmpnyNm').send_keys("s")
        driver.find_element_by_xpath('//*[@id="modalFindCmpny"]/div/div/div[2]/div[1]/div[2]/input').click()
        driver.find_element_by_xpath('//*[@id="modalFindCmpny"]/div/div/div[3]/button[1]').click() # Apply
        # driver.find_element_by_xpath('//*[@id="uploader"]/div/div/div[3]/input').click()
        driver.find_element_by_name('qqfile').send_keys("C:\\Users\de2o\Desktop\\fam.png")
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/button[2]').click()
        time.sleep(1)
        # find_pre.find_pre(driver, logger_console, err_logger)
        #
        # driver.find_element_by_id('userDropdown').click()
        # driver.find_element_by_id('adminPage').click()
        # time.sleep(1)
        #
        # driver.find_element_by_link_text('Notice/Document').click()
        # time.sleep(1)
        # find_pre.find_pre(driver, logger_console, err_logger)
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def modifyNotice(driver, logger, logger_console,err_logger):


        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE MODIFY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE MODIFY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        pages = driver.find_elements_by_xpath('//ul[@class="pagination pagination-rounded"]/li')
        for j in range(len(pages) - 2):
            elems = driver.find_elements_by_xpath('//i[@class="fa fa-edit fa-2x mr-2"]')
            for i in range(len(elems)):
                # if i==0:
                #     i=i+1
                #     continue
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] NOTICE-MODIFY-ADMIN TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE-MODIFY-ADMIN TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

                elems[i].click()
                time.sleep(3)
                # find_pre.find_pre(driver, logger_console, err_logger)
                driver.find_element_by_name('noticeTitle').clear()
                driver.find_element_by_name('noticeTitle').send_keys("Admin notice modify test")

                cmpny = Select(driver.find_element_by_id("noticeAuthCd"))
                cmpny.select_by_value('001')  # specific company

                driver.find_element_by_id("cmpnyNm").send_keys("storyd")
                driver.find_element_by_xpath('//*[@id="modalFindCmpny"]/div/div/div[2]/div[1]/div[2]/input').click()
                driver.find_element_by_xpath('//*[@id="modalFindCmpny"]/div/div/div[3]/button[1]').click()
                driver.find_element_by_xpath('//*[@id="noticeForm"]/div[2]/div/div/div[3]/div[3]/p').send_keys("수정")


                # 파일 다운로드
                driver.find_element_by_xpath('//*[@id="tbNoticeDocList"]/tbody/tr/td[2]/span[1]/i').click()
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="tbNoticeDocList"]/tbody/tr/td[2]/span[2]/i').click()

                driver.find_element_by_xpath('//button[@type="submit"]').click()
                # find_pre.find_pre(driver, logger_console, err_logger)
                time.sleep(3)

                for k in range(j):
                    driver.find_element_by_xpath('//*[@id="tbNoticeList_next"]/a').click()
                    time.sleep(2)

                k=0

                time.sleep(4)
                elems = driver.find_elements_by_xpath('//i[@class="fa fa-edit fa-2x mr-2"]')
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] NOTICE-MODIFY-ADMIN TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE-MODIFY-ADMIN TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

                #첫 notice만 test하려고 추가한 부분 (전체 순회하려면 이거 지우면 됨)
                if i == 0:
                    test=1
                    break

            if j < len(pages) -3 :

                # 첫 notice만 test하려고 추가한 부분 (전체 순회하려면 이거 지우면 됨)
                if test==1 :
                    break

                driver.find_element_by_xpath('//*[@id="tbNoticeList_next"]/a').click()
                time.sleep(2)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE MODIFY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE MODIFY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        time.sleep(3)

    def deleteNotice(driver, logger, logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE DELETE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE DELETE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        pages = driver.find_elements_by_xpath('//ul[@class="pagination pagination-rounded"]/li')
        for j in range(len(pages) - 2):
            elems = driver.find_elements_by_xpath('//i[@class="fa fa-trash fa-2x"]')
            for i in range(len(elems)):
                # if i==0:
                #     i=i+1
                #     continue
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] NOTICE-DELETE-ADMIN TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE-DELETE-ADMIN TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

                #dismiss
                elems[i].click()
                time.sleep(3)
                Alert(driver).dismiss()
                time.sleep(3)
                # find_pre.find_pre(driver, logger_console, err_logger)

                #accept
                elems[i].click()
                time.sleep(3)
                Alert(driver).accept()
                time.sleep(3)
                # find_pre.find_pre(driver, logger_console, err_logger)

                elems = driver.find_elements_by_xpath('//i[@class="fa fa-trash fa-2x"]')
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] NOTICE-DELETE-ADMIN TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE-DELETE-ADMIN TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

                time.sleep(3)
                # 첫 notice만 test하려고 추가한 부분 (전체 순회하려면 이거 지우면 됨)
                if i == 0:
                    test=1
                    break

            if j < len(pages) -3 :

                # 첫 notice만 test하려고 추가한 부분 (전체 순회하려면 이거 지우면 됨)
                if test==1:
                    break

                driver.find_element_by_xpath('//*[@id="tbNoticeList_next"]/a').click()
                time.sleep(2)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE DELETE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN NOTICE DELETE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        time.sleep(3)

    def noticeDetailAdmin(driver, logger, logger_console, err_logger):

        pages = driver.find_elements_by_xpath('//ul[@class="pagination pagination-rounded"]/li')
        for j in range(len(pages) - 2):
            notices = driver.find_elements_by_xpath('//*[@id="tbNoticeList"]/tbody/tr/td/a')
            for i in range(len(notices)):
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] NOTICE-DETAIL-ADMIN TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE-DETAIL-ADMIN TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

                notices[i].click()
                time.sleep(1)
                downloads = driver.find_elements_by_xpath('//i[@class="fa fa-download fa-2x mr-2"]')

                if len(downloads)>0 :
                    for m in range(len(downloads)):
                        downloads[m].click()
                        whitelabel.whitelabel(driver,err_logger,"Admin Notice Detail")
                        downloads = driver.find_elements_by_xpath('//i[@class="fa fa-download fa-2x mr-2"]')
                # find_pre.find_pre(driver, logger_console, err_logger)
                driver.find_element_by_xpath('//*[@id="wrap"]/div/button').click()  # List
                # find_pre.find_pre(driver, logger_console, err_logger)

                for k in range(j):
                    driver.find_element_by_xpath('//*[@id="tbNoticeList_next"]/a').click()
                    time.sleep(1)

                k=0

                time.sleep(4)
                notices = driver.find_elements_by_xpath('//*[@id="tbNoticeList"]/tbody/tr/td/a')
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] NOTICE-DETAIL-ADMIN TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] NOTICE-DETAIL-ADMIN TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

            if j < len(pages) -3 :
                driver.find_element_by_xpath('//*[@id="tbNoticeList_next"]/a').click()
                time.sleep(2)

        time.sleep(3)