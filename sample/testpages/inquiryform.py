import datetime
import time

REPETITION = 5
class inquiryform:
    def __init__(self):
        pass
    def newForm(driver,logger,logger_console):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] NEW INQUIRY FORM TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] NEW INQUIRY FORM TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))


        driver.find_element_by_id('userDropdown').click()
        driver.find_element_by_id('adminPage').click()
        time.sleep(2)
        driver.find_element_by_link_text('Inquiry Form').click()
        time.sleep(2)

        for i in range(REPETITION):
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/button').click()
            time.sleep(2)
            driver.find_element_by_id('estmGroupName').send_keys("Circle")
            driver.find_element_by_id('estmDescription').send_keys("OO")

            driver.find_element_by_xpath('//*[@id="btnAddLine"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="tbBody"]/tr/td[2]/input').click()
            time.sleep(1)
            driver.find_element_by_id('inputProdSearch').send_keys("c")
            driver.find_element_by_xpath('//*[@id="btnProdSearch"]').click()
            time.sleep(1)
            # driver.find_element_by_xpath('//*[@id="tbInquiryProdList"]/tbody/tr[1]/td[1]').click()
            # time.sleep(1)
            driver.find_element_by_xpath('//*[@id="modalSelectItem"]/div/div/div[3]/div/div/button[1]').click()

            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div/div[6]/div/button[2]').click()
            time.sleep(4)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] NEW INQUIRY FORM TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] NEW INQUIRY FORM TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def modify(driver,logger,logger_console):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] MODIFY INQUIRY FORM TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] MODIFY INQUIRY FORM TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        elems = driver.find_elements_by_xpath('//i[@class="fa fa-edit fa-2x mr-2"]')

        for i in range(len(elems)):
            elems[i].click()
            time.sleep(2)

            driver.find_element_by_name('estmGroupName').clear()
            driver.find_element_by_name('estmGroupName').send_keys('Circle 수정')
            driver.find_element_by_id('estmDescription').send_keys(" 고쳣음")

            driver.find_element_by_xpath('//*[@id="tbBody"]/tr[1]/td[1]/input').click()
            # driver.find_element_by_xpath('//*[@id="tbBody"]/tr[2]/td[1]/input').click()
            driver.find_element_by_id('btnDeleteLine').click()

            driver.find_element_by_xpath('/html/body/div/div[6]/div/button[2]').click()
            time.sleep(2)
            if i == 0 :
                break

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] MODIFY INQUIRY FORM TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] MODIFY INQUIRY FORM TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def delete(driver,logger,logger_console):
        pass