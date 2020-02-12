from datetime import time


def whitelabel(driver,err_logger, name):
    try:
        a = driver.find_element_by_xpath('/html/body/h1')
        b = driver.find_element_by_xpath('/html/body/div[3]')
        err_logger.debug("[%s ERROR] %s %s" % (name, a.text, b.text))
        driver.back()
        time.sleep(3)
    except :
        pass