import datetime
import time


class signin:
    def __init__(self):
        pass
    def signInTest(driver,logger,logger_console,err_logger):
        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SIGN-IN TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SIGN-IN TEST START" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        driver.find_element_by_id("btnSignIn").click()
        time.sleep(1)
        driver.find_element_by_id("userNm").send_keys("admin")
        driver.find_element_by_id("userPwd").send_keys("1234")
        driver.find_element_by_xpath('//*[@id="frmLogin"]/div[@class="form-group"]/button').click()
        time.sleep(3)

        """
        try:
            if driver.switch_to.alert.text == "fail":
                err_logger.debug("[Sign-in Fail] ajax failure : %s" % driver.switch_to.alert.text)
                logger_console.debug("[Sign-in Fail] ajax failure : %s" % driver.switch_to.alert.text)
            elif driver.switch_to.alert.text == "The username or password you entered is incorrect.":
                logger.debug("[Sign-in Success]")
                logger_console.debug("[Sign-in Success] ")
                print("sign-in 재시도")

            Alert(driver).accept()

        except NoAlertPresentException:
            logger.debug("[Sign-in Success]")
            logger_console.debug("[Sign-in Success] ")
        """

        now = datetime.datetime.now()
        logger.debug("[%d.%d.%d %d:%d:%d] SIGN-IN TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))
        logger_console.debug("[%d.%d.%d %d:%d:%d] SIGN-IN TEST END" % (
            now.year, now.month, now.day, now.hour, now.minute, now.second))

        time.sleep(3)