import datetime
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


REPETITION = 3
class inquiry:
    def __init__(self):
        pass

    def newInquiry(driver,logger,logger_console,err_logger):
        driver.find_element_by_link_text("Inquiry").click()
        time.sleep(2)
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] NEW INQUIRY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] NEW INQUIRY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_id('newEstimateRequest').click()
        time.sleep(2)

        project = Select(driver.find_element_by_id("salesOptntId"))
        project.select_by_value('231')

        driver.find_element_by_name("estmReqDt").send_keys("2022")
        time.sleep(1)
        driver.find_element_by_name("estmReqDt").send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_name("estmReqDt").send_keys("03")
        time.sleep(1)

        driver.find_element_by_name("estmReqDt").send_keys("01")
        time.sleep(1)


        # # new project
        # driver.find_element_by_id('createSalesOptnt').click()
        # driver.find_element_by_id('salesOptntNm').send_keys("테스트용")
        # driver.find_element_by_id('salesOptntAddr').send_keys("#")
        # driver.find_element_by_id('customNm').send_keys("복어")
        # driver.find_element_by_name("salesOptntStartDt").send_keys("2020")
        # time.sleep(1)
        # driver.find_element_by_name("salesOptntStartDt").send_keys(Keys.TAB)
        # time.sleep(1)
        # driver.find_element_by_name("salesOptntStartDt").send_keys("05")
        # time.sleep(1)
        #
        # driver.find_element_by_name("salesOptntStartDt").send_keys("25")
        # time.sleep(1)
        #
        # driver.find_element_by_name("salesOptntEndDt").send_keys("2020")
        # time.sleep(1)
        # driver.find_element_by_name("salesOptntEndDt").send_keys(Keys.TAB)
        # time.sleep(1)
        # driver.find_element_by_name("salesOptntEndDt").send_keys("10")
        # time.sleep(1)
        #
        # driver.find_element_by_name("salesOptntEndDt").send_keys("04")
        # time.sleep(1)
        # driver.find_element_by_id('modal-SalesOptnt-create').click()


        time.sleep(1)
        driver.find_element_by_id('unCode').send_keys("5")
        driver.find_element_by_id('brandNm').send_keys("five")



        driver.find_element_by_id('btnAddLine').click()
        driver.find_element_by_xpath('//*[@id="tbBody"]/tr/td[2]/input').click()
        time.sleep(2)
        driver.find_element_by_id('nav-group-tab').click() # Group
        time.sleep(1)
        project = Select(driver.find_element_by_id("selectGroup"))
        project.select_by_value('35')  # 테스트용

        # # Product
        # driver.find_element_by_id('inputProdSearch').send_keys("a")
        # driver.find_element_by_id('btnProdSearch').click()
        # driver.find_element_by_xpath('//*[@id="tbInquiryProdList"]/tbody/tr[2]').click()
        driver.find_element_by_xpath('//*[@id="modalSelectItem"]/div/div/div[3]/div/div/button[1]').click() # Select

        driver.find_element_by_id('estmReqCnt').send_keys("5")
        driver.find_element_by_id('remark').send_keys("10")

        driver.find_element_by_id('price').send_keys('100,000')
        driver.find_element_by_id('protectPack').send_keys('Y')
        driver.find_element_by_id('payment').send_keys('N')
        driver.find_element_by_id('deliveryTime').send_keys('2022-05-25')
        driver.find_element_by_id('offerScope').send_keys('1')

        driver.find_element_by_id('comment').send_keys('코멘트는20자내외로')
        # driver.find_element_by_xpath('/html/body/div[1]/div[10]/div/button[3]').click() # Save
        driver.find_element_by_xpath('/html/body/div[1]/div[10]/div/button[2]').click() # Inquiry
        time.sleep(5)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] NEW INQUIRY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] NEW INQUIRY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def modify(driver,logger,logger_console,err_logger):
        pass

    def detail(driver,logger,logger_console,err_logger):
        elems = driver.find_elements_by_xpath('//tr[@role="row"]/ td[1] / span')

        for i in range(len(elems)):
            elems[i].click()
            time.sleep(2)
            # find_pre.find_pre(driver,logger_console,err_logger)
            driver.back()
            time.sleep(2)
            elems = driver.find_elements_by_xpath('//tr[@role="row"]/ td[1] / span')
