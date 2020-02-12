import datetime
import logging
import os
import time

import tailer as tailer
from selenium import webdriver

from testpages import weAre, weMake, weInstalled, signin, inquiry, sales, notice, adminNotice, ref, product, inquiry_product, inquiryform, admininquiryitem

# LOG 처리
LOG_FILE_DIR = '../tta'
if not os.path.exists(LOG_FILE_DIR):
    os.makedirs(LOG_FILE_DIR)
if not os.path.exists(os.path.join(LOG_FILE_DIR, 'deploy')):
    os.makedirs(os.path.join(LOG_FILE_DIR, 'deploy'))
logging.basicConfig(filename='../operator_tta1_', level=logging.DEBUG)
now = datetime.datetime.now()
log_file_prefix = os.path.join(LOG_FILE_DIR, 'operator_tta1_')
log_file_suffix = '%d-%d-%d ' % (now.year, now.month, now.day)
engine_fileHandler = logging.FileHandler(log_file_prefix + log_file_suffix)
engine_fileHandler.setLevel(logging.DEBUG)
logger = logging.getLogger('file')
logger.addHandler(engine_fileHandler)
logger_console = logging.getLogger('console')
logger_console.setLevel('DEBUG')
consoleHandler = logging.StreamHandler()
logger_console.addHandler(consoleHandler)

# error 로그 기록하는 파일
logging.basicConfig(filename='../operator_tta1_error_', level=logging.DEBUG)
log_file_prefix = os.path.join(LOG_FILE_DIR, 'operator_tta1_error_')
log_file_suffix = '%d-%d-%d ' % (now.year, now.month, now.day)
engine_fileHandler = logging.FileHandler(log_file_prefix + log_file_suffix)
engine_fileHandler.setLevel(logging.DEBUG)
err_logger = logging.getLogger("operator_tta1_error_")
err_logger.addHandler(engine_fileHandler)

# Driver 처리
driver = webdriver.Chrome('C:\\Users\de2o\Desktop\chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://dev.de2o.com:8889/')
REPETITION = 3
time.sleep(2)

def find_error(start, end):
    with open('../tta/operator_tta1_%d-%d-%d' % (now.year, now.month, now.day)) as f:
        lines = "\n".join(tailer.tail(f, 5))

    # #
    # req = driver.current_url
    # res = requests.get(req)
    # if res.status_code >= 400:
    #     err_logger.debug(" >>>>> [%s] HTTPError code is %d <<<<< " % (start, res.status_code))
    # else :
    #     print(res.status_code)

    if start in lines and end in lines:
        pass
    else:
        err_logger.debug(start)
        logger_console.debug(start)
        # find_pre()


# data 기록할 파일
f = open('../datalist/datalist', mode='a', encoding='utf-8-sig')


#We Are Test
try:
    weAre.weAre.weAreTest(driver, logger, logger_console,err_logger)
except Exception as e:
    err_logger.debug(" [WeAre] Exception Occurred : %s" %(e))
    pass
find_error("WE-ARE TEST START","WE-ARE TEST END")

#We Make Test
try:
    weMake.weMake.weMakeTest(driver, logger, logger_console,err_logger)
except Exception as e:
    err_logger.debug(" [WeMake] Exception Occurred : %s" %(e))
    pass
find_error("WE-MAKE TEST START","WE-MAKE TEST END")

#We Make Detail Test
try:
    weMake.weMake.weMakeDetail(driver, logger, logger_console,err_logger)
except Exception as e:
    err_logger.debug(" [WeMakeDetail] Exception Occurred : %s" %(e))
    pass
find_error("WEMAKE-DETAIL TEST START","WEMAKE-DETAIL TEST END")

#We Installed Test
try:
    weInstalled.weInstalled.weInstalledTest(driver, logger, logger_console,err_logger)
except Exception as e:
    err_logger.debug(" [WeInstalled] Exception Occurred : %s" %(e))
    pass
find_error("WE INSTALLED DETAIL TEST START","WE INSTALLED DETAIL TEST END")

# Signin Test
try:
    signin.signin.signInTest(driver, logger, logger_console, err_logger)
except Exception as e:
    err_logger.debug(" [SignIn] Exception Occurred : %s" % (e))
    pass
find_error("SIGN-IN TEST START", "SIGN-IN TEST END")

# # Sales Test
# try:
#     sales.sales.salesTest(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [Sales] Exception Occurred : %s" % (e))
#     pass
#
# find_error("SALES TEST START", "SALES TEST END")

# # Sales Detail Test
# try:
#     sales.sales.details(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [SalesDetail] Exception Occurred : %s" % (e))
#     pass
# find_error("SALES-DETAILS TEST START", "SALES-DETAILS TEST END")
#
# # Sales Register Test
# try:
#     sales.sales.register(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [SalesRegister] Exception Occurred : %s" % (e))
#     pass
# find_error("SALES-REGISTER TEST START", "SALES-REGISTER TEST END")
#
# # Sales Register Back Test
# try:
#     sales.sales.register_back(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [SalesRegisterBack] Exception Occurred : %s" % (e))
#     pass
# find_error("SALES-REGISTER-BACK TEST START", "SALES-REGISTER-BACK TEST END")
#
# # Sales Modify Test
# try:
#     sales.sales.modify(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [SalesModify] Exception Occurred : %s" % (e))
#     pass
# find_error("SALES-MODIFY TEST START", "SALES-MODIFY TEST END")
#
# # Sales Delete Test
# try:
#     sales.sales.delete(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [SalesDelete] Exception Occurred : %s" % (e))
#     pass
# find_error("SALES-DELETE TEST START", "SALES-DELETE TEST END")

# # Notice Test
# try:
#     notice.notice.noticeTest(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [Notice] Exception Occurred : %s" % (e))
#     pass
# find_error("NOTICE TEST START", "NOTICE TEST END")
#
# # Notice Detail Test
# try:
#     notice.notice.noticeDetail(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [NoticeDetail] Exception Occurred : %s" % (e))
#     pass
# find_error("NOTICE-DETAIL TEST START", "NOTICE-DETAIL TEST END")

# # Admin Notice Test
# try:
#     adminNotice.adminNotice.adminNoticeTest(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [AdminNotice] Exception Occurred : %s" % (e))
#     pass
# find_error("ADMIN NOTICE TEST START", "ADMIN NOTICE TEST END")
#
# # Admin Notice Register Test
# try:
#     adminNotice.adminNotice.newNotice(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [AdminNoticeRegister] Exception Occurred : %s" % (e))
#     pass
# find_error("ADMIN NOTICE REGISTER TEST START", "ADMIN NOTICE REGISTER TEST END")
#
# # Admin Notice Modify Test
# try:
#     adminNotice.adminNotice.modifyNotice(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [AdminNoticeModify] Exception Occurred : %s" % (e))
#     pass
# find_error("ADMIN NOTICE MODIFY TEST START", "ADMIN NOTICE MODIFY TEST END")
#
# # Admin Notice Delete Test
# try:
#     adminNotice.adminNotice.deleteNotice(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [AdminNoticeDelete] Exception Occurred : %s" % (e))
#     pass
# find_error("ADMIN NOTICE DELETE TEST START", "ADMIN NOTICE DELETE TEST END")
#

# # Admin Notice Detail Test
# try:
#     adminNotice.adminNotice.noticeDetailAdmin(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [AdminNoticeDetail] Exception Occurred : %s" % (e))
#     pass
# find_error("NOTICE-DETAIL-ADMIN TEST START", "NOTICE-DETAIL-ADMIN TEST END")

# try:
#     driver.find_element_by_link_text("Home").click()
#     time.sleep(3)
# except Exception as e:
#     err_logger.debug(" Exception Occurred : %s" % (e))
#     pass
#
# # Ref Test
# try:
#     ref.ref.refTest(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [Ref] Exception Occurred : %s" % (e))
#     pass
# find_error("ADMIN-REF TEST START", "ADMIN-REF TEST END")
#
# # Ref Register Test
# try:
#     ref.ref.newRef(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [RefRegister] Exception Occurred : %s" % (e))
#     pass
# find_error("ADMIN-REF-REGISTER TEST START", "ADMIN-REF-REGISTER TEST END")
#
# # Ref Modify Test
# try:
#     ref.ref.modifyRef(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [RefModify] Exception Occurred : %s" % (e))
#     pass
# find_error("ADMIN-REF-MODIFY TEST START", "ADMIN-REF-MODIFY TEST END")
#
# # Ref Delete Test
# try:
#     ref.ref.deleteRef(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [RefDelete] Exception Occurred : %s" % (e))
#     pass
# find_error("ADMIN-REF-DELETE TEST START", "ADMIN-REF-DELETE TEST END")
#
# # Ref Detail Test
# try:
#     ref.ref.refDetail(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [RefDetail] Exception Occurred : %s" % (e))
#     pass
# find_error("REF-DETAIL-ADMIN TEST START", "REF-DETAIL-ADMIN TEST END")

# # Home Product Test
# try:
#     product.product.productTest(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [HomeProduct] Exception Occurred : %s" % (e))
#     pass
# find_error("PRODUCT-HOME TEST START", "PRODUCT-HOME TEST END")
#
# # Home Product Register Test
# try:
#     product.product.newProduct(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [HomeProductRegister] Exception Occurred : %s" % (e))
#     pass
# find_error("PRODUCT-REGISTER TEST START", "PRODUCT-REGISTER TEST END")
#
# # Home Product Modify Test
# try:
#     product.product.modifyProduct(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [HomeProductModify] Exception Occurred : %s" % (e))
#     pass
# find_error("PRODUCT-MODIFY TEST START", "PRODUCT-MODIFY TEST END")
#
# # Home Product Delete Test
# try:
#     product.product.deleteProduct(driver, logger, logger_console, err_logger)
# except Exception as e:
#     err_logger.debug(" [HomeProductDelete] Exception Occurred : %s" % (e))
#     pass
# find_error("PRODUCT-DELETE TEST START", "PRODUCT-DELETE TEST END")

# #Inquiry Product Test
# try:
#     inquiry_product.inquiry_product.productTest(driver,logger,logger_console)
# except Exception as e :
#     err_logger.debug(" [InquiryProductTest] Exception Occurred : %s " % (e))
#     pass
# find_error("PRODUCT-INQUIRY TEST START","PRODUCT-INQUIRY TEST END")
#
# #Inquiry Product Register Test
# try:
#     inquiry_product.inquiry_product.newProduct(driver,logger,logger_console)
# except Exception as e:
#     err_logger.debug(" [InquiryProductRegister] Exception Occurred : %s" % (e))
#     pass
# find_error("PRODUCT-INQUIRY TEST START","PRODUCT-INQUIRY TEST END")
#
# try:
#     inquiry_product.inquiry_product.modifyProduct(driver,logger,logger_console)
# except Exception as e:
#     err_logger.debug(" [InquiryProductModify] Exception Occurred : %s" % (e))
#     pass
# find_error("PRODUCT-INQUIRY-MODIFY TEST START","PRODUCT-INQUIRY-MODIFY TEST END")
#
# try:
#     inquiry_product.inquiry_product.deleteProduct(driver,logger,logger_console)
# except Exception as e:
#     err_logger.debug(" [InquiryProductDelete] Exception Occurred : %s" % (e))
#     pass
# find_error("PRODUCT-INQUIRY-DELETE TEST START","PRODUCT-INQUIRY-DELETE TEST END")

# Inquiry Test
#
# driver.find_element_by_link_text("Inquiry").click()
# time.sleep(2)
#
#
# try:
#     inquiry.inquiry.newInquiry(driver,logger,logger_console,err_logger)
# except Exception as e:
#     err_logger.debug(" [ New Inquiry ] Exception Occurred : %s" % (e))
#     pass

# try:
#     inquiry.inquiry.detail(driver,logger,logger_console,err_logger)
# except Exception as e:
#     err_logger.debug(" [Inquiry Detail] Exception Occurred : %s" % (e))
#     pass

# Inquiry Form Test
try:
    inquiryform.inquiryform.newForm(driver,logger,logger_console)
except Exception as e :
    err_logger.debug(" [Inquiry Form Test] Exception Occurred : %s " % (e))
    pass
find_error("NEW INQUIRY FORM TEST START","NEW INQUIRY FORM TEST END")

try:
    inquiryform.inquiryform.modify(driver,logger,logger_console)
except Exception as e:
    err_logger.debug(" [Inquiry Form Modify Test] Exception Occurred : %s " % (e))
    pass
find_error("MODIFY INQUIRY FORM TEST START","MODIFY INQUIRY FORM TEST END")

#
# # admin inquiry item test
# try:
#     admininquiryitem.admininquiry.inquiryTest(driver,logger,logger_console)
# except Exception as e :
#     err_logger.debug(" [Admin Inquiry Test] Exception Occurred : %s " % (e))
#     pass

# f.close()
# driver.close()
# driver.quit()
# exit(0)