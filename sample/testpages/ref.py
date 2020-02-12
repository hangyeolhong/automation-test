import datetime
import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from init import find_pre

class ref:
    def __init__(self):
        pass
    def refTest(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_id('userDropdown').click()
        driver.find_element_by_id('adminPage').click()
        time.sleep(1)
        driver.find_element_by_link_text('Reference').click()
        time.sleep(1)
        find_pre.find_pre(driver,logger_console,err_logger)

        #filtering test
        driver.find_element_by_xpath('//input[@type="search"]').send_keys("VINCOM")
        time.sleep(1)
        driver.find_element_by_link_text('Reference').click()
        time.sleep(2)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

    def newRef(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-REGISTER TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/button').click()
        time.sleep(1)
        find_pre.find_pre(driver,logger_console,err_logger)
        driver.find_element_by_id("prodRefNm").send_keys("ref register test")
        driver.find_element_by_id("prodRefDesc").send_keys("왕왕")
        driver.find_element_by_xpath('//*[@id="mainImageNm"]').send_keys("C:\\Users\de2o\Desktop\circle.png")
        postable = Select(driver.find_element_by_id("postable"))
        postable.select_by_value('N')  # specific company
        driver.find_element_by_xpath('//*[@id="frmNewRef"]/div[5]/div/div/div[3]/div[2]/p').send_keys("Summernote test")

        # 존재하지 않는 product search
        driver.find_element_by_xpath('//*[@id="prodNm"]').send_keys("xxx")
        driver.find_element_by_xpath('//*[@id="btnProdSearch"]').click()
        time.sleep(2)
        Alert(driver).accept()
        driver.find_element_by_xpath('//*[@id="prodNm"]').clear()

        # 존재하는 product search
        driver.find_element_by_xpath('//*[@id="prodNm"]').send_keys("cylinder")
        driver.find_element_by_xpath('//*[@id="btnProdSearch"]').click()

        products = driver.find_elements_by_xpath('//*[@id="divProdSearch"]/div[@class="row mb-1"]/div[@class="col"]/button') #Add
        for i in range(len(products)):
            products[i].click()
            time.sleep(2)

        #이미 추가했는데 또 add시도할 때
        products[0].click()
        time.sleep(3)
        Alert(driver).accept()

        driver.find_element_by_xpath('//*[@id="btnCreateRef"]').click() #Create
        time.sleep(3)
        find_pre.find_pre(driver, logger_console, err_logger)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-REGISTER TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        time.sleep(3)

    def modifyRef(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-MODIFY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-MODIFY TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        pages = driver.find_elements_by_xpath('//ul[@class="pagination pagination-rounded"]/li')
        for j in range(len(pages) - 2):
            time.sleep(1)
            elem = driver.find_elements_by_xpath('//i[@class="fa fa-edit fa-2x mr-2"]')

            # #전체 순회하면서 modify
            # for l in range(len(elem)) :
            #     now = datetime.datetime.now()
            #     logger.debug("[%d.%d.%d %d:%d:%d] REF-MODIFY TEST START : index[%d]" % (
            #         now.year, now.month, now.day, now.hour, now.minute, now.second, l))
            #     logger_console.debug("[%d.%d.%d %d:%d:%d] REF-MODIFY TEST START : index[%d]" % (
            #         now.year, now.month, now.day, now.hour, now.minute, now.second, l))
            #     elem[l].click()
            #     time.sleep(3)
            #     driver.find_element_by_id("prodRefNm").send_keys(" -> modify test")
            #     driver.find_element_by_id("prodRefDesc").send_keys("왕왕왕")
            #     postable = Select(driver.find_element_by_id("postable"))
            #     postable.select_by_value('Y')  # specific company
            #
            #     modify 추가부분(담은 product 삭제)
            #     products = driver.find_elements_by_xpath('//*[@id="divProdList"]/div[@class="row mb-1"]')
            #     dels = driver.find_elements_by_xpath('// *[ @ id = "divProdList"] / div[@class="row mb-1"] / div[2] / button[2]')
            #
            #     for i in range(len(products)):
            #         dels[0].click() # Delete
            #         time.sleep(3)
            #         Alert(driver).accept()
            #         time.sleep(3)
            #         dels = driver.find_elements_by_xpath(
            #             '// *[ @ id = "divProdList"] / div[@class="row mb-1"] / div[2] / button[2]')
            #     driver.find_element_by_xpath('//*[@id="btnUpdateRef"]').click()
            #     for k in range(j):
            #         driver.find_element_by_xpath('//*[@id="tbRefList_next"]/a').click()
            #         time.sleep(2)
            #
            #     k = 0
            #
            # #한 페이지 다 조회 후 다음 페이지로 넘어가기
            # if j < len(pages) - 3:
            #     driver.find_element_by_xpath('//*[@id="tbRefList_next"]/a').click()  # 다음 페이지로 이동
            #     time.sleep(2)

            elem[9].click()
            time.sleep(3)
            find_pre.find_pre(driver, logger_console, err_logger)
            driver.find_element_by_id("prodRefNm").clear()
            driver.find_element_by_id("prodRefNm").send_keys("ref Modify test")
            driver.find_element_by_id("prodRefDesc").send_keys("왕왕왕")
            postable = Select(driver.find_element_by_id("postable"))
            postable.select_by_value('Y')  # specific company

            #modify 추가부분(담은 product 삭제)
            products = driver.find_elements_by_xpath('//*[@id="divProdList"]/div[@class="row mb-1"]')
            dels = driver.find_elements_by_xpath('// *[ @ id = "divProdList"] / div[@class="row mb-1"] / div[2] / button[2]')

            for i in range(len(products)):
                dels[0].click() # Delete
                time.sleep(3)
                Alert(driver).accept()
                time.sleep(3)
                dels = driver.find_elements_by_xpath('// *[ @ id = "divProdList"] / div[@class="row mb-1"] / div[2] / button[2]')
            driver.find_element_by_xpath('//*[@id="btnUpdateRef"]').click()
            find_pre.find_pre(driver, logger_console, err_logger)
            time.sleep(3)

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-MODIFY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-MODIFY TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        time.sleep(3)

    def deleteRef(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-DELETE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-DELETE TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        pages = driver.find_elements_by_xpath('//ul[@class="pagination pagination-rounded"]/li')
        for j in range(len(pages) - 2):
            elem = driver.find_elements_by_xpath('//i[@class="fa fa-trash fa-2x"]')

            # # 전체 순회하면서 delete
            # for i in range(len(elem)) :
            #     now = datetime.datetime.now()
            #     logger.debug("[%d.%d.%d %d:%d:%d] REF-DELETE TEST START : index[%d]" % (
            #         now.year, now.month, now.day, now.hour, now.minute, now.second, i))
            #     logger_console.debug("[%d.%d.%d %d:%d:%d] REF-DELETE TEST START : index[%d]" % (
            #         now.year, now.month, now.day, now.hour, now.minute, now.second, i))
            #     elem[i].click()
            #     time.sleep(3)
            #     Alert(driver).accept()
            #     elem = driver.find_elements_by_xpath('//i[@class="fa fa-trash fa-2x"]')
            #
            #     now = datetime.datetime.now()
            #     logger.debug("[%d.%d.%d %d:%d:%d] REF-DELETE TEST END : index[%d]" % (
            #         now.year, now.month, now.day, now.hour, now.minute, now.second, i))
            #     logger_console.debug("[%d.%d.%d %d:%d:%d] REF-DELETE TEST END : index[%d]" % (
            #         now.year, now.month, now.day, now.hour, now.minute, now.second, i))
            #
            # if j < len(pages) - 3:
            #     driver.find_element_by_xpath('//*[@id="tbRefList_next"]/a').click()  # 다음 페이지로 이동
            #     time.sleep(2)
            # logger.debug("[Ref-Delete Success]")
            # logger_console.debug("[Ref-Delete Success]")

            time.sleep(3)
            elem[9].click()
            time.sleep(3)
            Alert(driver).accept()

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-DELETE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] ADMIN-REF-DELETE TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        time.sleep(3)

    def refDetail(driver,logger,logger_console,err_logger):
        pages = driver.find_elements_by_xpath('//ul[@class="pagination pagination-rounded"]/li')
        for j in range(len(pages) - 2):
            refs = driver.find_elements_by_xpath('// *[ @ id = "tbRefList"] / tbody / tr/ td/ a')
            for i in range(len(refs)):
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] REF-DETAIL-ADMIN TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] REF-DETAIL-ADMIN TEST START : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

                refs[i].click()
                time.sleep(2)
                find_pre.find_pre(driver, logger_console, err_logger)
                products = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/form/div[5]/div/div/div/a')

                if len(products) > 0 :
                    for l in range(len(products)):
                        products[l].click()
                        time.sleep(3)
                        find_pre.find_pre(driver, logger_console, err_logger)
                        driver.back()
                        time.sleep(2)
                        find_pre.find_pre(driver, logger_console, err_logger)
                        products = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/form/div[5]/div/div/div/a')

                driver.find_element_by_xpath('//*[@id="btnBack"]').click()  # Back
                find_pre.find_pre(driver, logger_console, err_logger)

                #Back 누르면 페이지1로 돌아오므로 j만큼 페이지 이동
                for k in range(j):
                    driver.find_element_by_xpath('//*[@id="tbRefList_next"]/a').click()
                    time.sleep(2)

                k=0

                time.sleep(2)
                refs = driver.find_elements_by_xpath('// *[ @ id = "tbRefList"] / tbody / tr/ td/ a')
                now = datetime.datetime.now()
                logger.debug("[%d.%d.%d %d:%d:%d] REF-DETAIL-ADMIN TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
                logger_console.debug("[%d.%d.%d %d:%d:%d] REF-DETAIL-ADMIN TEST END : index[%d]" % (
                    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

            if j < len(pages) - 3:
                driver.find_element_by_xpath('//*[@id="tbRefList_next"]/a').click() # 다음 페이지로 이동
                time.sleep(1)
