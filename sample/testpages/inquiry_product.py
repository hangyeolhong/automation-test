import datetime
import time
from selenium.webdriver.common.alert import Alert

class inquiry_product:
    def __init__(self):
        pass

    def productTest(driver, logger, logger_console):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_id('userDropdown').click()
        driver.find_element_by_id('adminPage').click()
        time.sleep(2)
        driver.find_element_by_link_text('Product').click()

        # driver.find_element_by_xpath('//*[@id="navbarDropdown"]').click()
        time.sleep(1)

        # inquiry product
        driver.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[1]/li[4]/div/a[2]').click()
        time.sleep(3)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def newProduct(driver, logger, logger_console):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/button').click()
        time.sleep(1)

        driver.find_element_by_name('inquiryProdBrand').send_keys('No Brand Edit')
        driver.find_element_by_name('inquiryProdNm').send_keys('Circle')
        driver.find_element_by_name('inquiryProdModelNo').send_keys('23')
        driver.find_element_by_name('inquiryProdUnit').send_keys('EA')

        driver.find_element_by_xpath('//*[@id="newInquiryProdModal"]/div/div/form/div[2]/button[1]').click() # Save
        time.sleep(1)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def modifyProduct(driver, logger, logger_console):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-MODIFY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-MODIFY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        elems = driver.find_elements_by_xpath('//i[@class="fa fa-edit fa-2x mr-2"]')

        for i in range(len(elems)):
            elems[i].click()
            time.sleep(2)
            driver.find_element_by_id("inquiryProdUnit").clear()
            driver.find_element_by_id("inquiryProdUnit").send_keys("Dozen")
            driver.find_element_by_xpath('//*[@id="modifyInquiryProdModal"]/div/div/form/div[2]/button[1]').click()
            time.sleep(1)
            elems = driver.find_elements_by_xpath('//i[@class="fa fa-edit fa-2x mr-2"]')

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-MODIFY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-MODIFY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def deleteProduct(driver, logger, logger_console):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-DELETE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-DELETE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        elems = driver.find_elements_by_xpath('//i[@class="fa fa-trash fa-2x"]')

        elems[4].click()
        time.sleep(1)
        Alert(driver).dismiss()

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-DELETE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] PRODUCT-INQUIRY-DELETE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))