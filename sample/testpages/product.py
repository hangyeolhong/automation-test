import datetime
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

from init import find_pre

class product:
    def __init__(self):
        pass
    def productTest(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-HOME TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-HOME TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_id('userDropdown').click()
        driver.find_element_by_id('adminPage').click()
        time.sleep(2)
        driver.find_element_by_link_text('Product').click()

        #driver.find_element_by_xpath('//*[@id="navbarDropdown"]').click()
        time.sleep(1)
        find_pre.find_pre(driver,logger_console,err_logger)
        #homepage product
        driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[1]/li[4]/div/a[1]').click()
        time.sleep(3)
        find_pre.find_pre(driver, logger_console, err_logger)
        # #inquiry product
        # driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[1]/li[4]/div/a[2]').click()
        # time.sleep(3)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-HOME TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-HOME TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def newProduct(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/button').click()
        time.sleep(3)
        find_pre.find_pre(driver, logger_console, err_logger)
        driver.find_element_by_id("categoryNm").send_keys("anon")
        driver.find_element_by_id("categoryDesc").send_keys("11")
        driver.find_element_by_id("imageNm").send_keys("C:\\Users\de2o\Desktop\\fam.png")
        parent = Select(driver.find_element_by_name("parentCategory"))
        parent.select_by_value('173')  # select parent category

        driver.find_element_by_xpath('//button[@type="submit"]').click()
        find_pre.find_pre(driver, logger_console, err_logger)
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def modifyProduct(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-MODIFY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-MODIFY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        elems = driver.find_elements_by_xpath('//*[@id="tbCategory"]/tbody/tr/td[4]/span/i[1]')
        elems[26].click() # modify
        time.sleep(3)

        driver.find_element_by_id("prodCategoryNm").clear()
        driver.find_element_by_id("prodCategoryNm").send_keys("Circle")
        driver.find_element_by_id("displayOrder").clear()
        driver.find_element_by_id("displayOrder").send_keys("4")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="updateCategoryModal"]/div/div/form/div[2]/div/div/button[1]').click()
        time.sleep(3)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-MODIFY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-MODIFY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def deleteProduct(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-DELETE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-DELETE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        elems = driver.find_elements_by_xpath('//i[@class="fa fa-trash fa-2x"]')

        # for i in range(len(elems)):
        #     elems[i].click()
        #     time.sleep(2)
        #     Alert(driver).accept()

        elems[26].click()
        time.sleep(2)
        Alert(driver).dismiss()

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-DELETE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-DELETE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))