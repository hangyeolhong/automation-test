def find_pre(driver,logger_console,err_logger):
    try:
        pre = driver.find_element_by_xpath('/html/body/pre')
        err_logger.debug(pre.text)
    except:
        pass