#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import datetime
import os
import sys
import logging


# LOG 처리
# LOG_FILE_DIR = 'logs/tta'
LOG_FILE_DIR = 'sample'
if not os.path.exists(LOG_FILE_DIR):
    os.makedirs(LOG_FILE_DIR)
if not os.path.exists(os.path.join(LOG_FILE_DIR, 'deploy')):
    os.makedirs(os.path.join(LOG_FILE_DIR, 'deploy'))
logging.basicConfig(filename='operator_tta1_', level=logging.DEBUG)
now = datetime.datetime.now()
log_file_prefix = os.path.join(LOG_FILE_DIR, 'operator_tta1_')
log_file_suffix = '%d-%d-%d ' %(now.year, now.month, now.day)
engine_fileHandler = logging.FileHandler(log_file_prefix+log_file_suffix)
engine_fileHandler.setLevel(logging.DEBUG)
logger = logging.getLogger('file')
logger.addHandler(engine_fileHandler)
logger_console = logging.getLogger('console')
logger_console.setLevel('DEBUG')
consoleHandler = logging.StreamHandler()
logger_console.addHandler(consoleHandler)

# Driver 생성 처리
#driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome('C:\사용자\de2o\Downloads\chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://dev.de2o.com/test/')
REPETITION = 3
time.sleep(2)

def wait_resource():
    time.sleep(1)
    success = driver.find_element_by_id('success_deploy')
    error = driver.find_element_by_id('error_deploy')
    while True:
        rcv_msg = driver.find_element_by_id('receive_message')
        if success.is_displayed():
            logger.debug("[Deploy Success]")
            logger_console.debug("[Deploy Success] %s" % rcv_msg.get_attribute("value"))
            break
        if error.is_displayed():
            logger.debug("[Deploy Fail] %s" % rcv_msg.get_attribute("value"))
            logger_console.debug("[Deploy Fail] %s" % rcv_msg.get_attribute("value"))
            break
        logger_console.debug("Waiting for provisioning resource..")
        time.sleep(2)

def load_and_process():
    time.sleep(1)
    driver.find_element_by_id("btnDesignLoad").click()
    ready = driver.find_element_by_id('ready_deploy')
    while True:
        time.sleep(1)
        if ready.is_displayed():
            break
    driver.find_element_by_id("btnProcess").click()

    wait_resource()

def init():
    time.sleep(1)
    csp_comp = Select(driver.find_element_by_id("sel_csp"));
    csp_comp.select_by_value('aws')
    driver.find_element_by_id("btnInit").click()
    wait_resource()
    csp_comp.select_by_value('aliyun')
    driver.find_element_by_id("btnInit").click()
    wait_resource()
    csp_comp.select_by_value('gcp')
    driver.find_element_by_id("btnInit").click()
    wait_resource()
    csp_comp.select_by_value('azure')
    driver.find_element_by_id("btnInit").click()
    wait_resource()

def test_by_all_refer(resource, process, csp):

    now = datetime.datetime.now()
    logger.debug('[%d.%d.%d %d:%d:%d] Resource : %s, Process : %s, CSP : %s"' % (now.year, now.month, now.day, now.hour, now.minute, now.second, resource, process, csp))
    logger_console.debug('[%d.%d.%d %d:%d:%d] Resource : %s, Process : %s, CSP : %s"' % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, resource, process, csp))
    resource_comp = Select(driver.find_element_by_id("sel_resource"))
    resource_comp.select_by_value(resource)
    time.sleep(1)
    process_comp = Select(driver.find_element_by_id("sel_process"))
    process_comp.select_by_value(process)
    time.sleep(1)
    csp_comp = Select(driver.find_element_by_id("sel_csp"))
    csp_comp.select_by_value(csp)
    load_and_process()


def test_by_refer(resource, process):
    test_by_all_refer(resource, process, 'aws')
    test_by_all_refer(resource, process, 'aliyun')
    test_by_all_refer(resource, process, 'gcp')
    test_by_all_refer(resource, process, 'azure')

# VPC TEST
now = datetime.datetime.now()
logger.debug("[%d.%d.%d %d:%d:%d] TTA1 TEST START " % (now.year, now.month, now.day, now.hour, now.minute, now.second))
for i in range(REPETITION):
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] VPC TEST START [index : %d]" % (now.year, now.month, now.day, now.hour, now.minute, now.second,i))
    logger_console.debug("[%d.%d.%d %d:%d:%d] VPC TEST START [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
    test_by_refer('vpc', 'create')
    test_by_refer('vpc', 'update')
    test_by_refer('vpc', 'delete')
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] VPC TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
    logger_console.debug("[%d.%d.%d %d:%d:%d] VPC TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))

# Subnet TEST
test_by_refer('subnet', 'prepare')
for i in range(REPETITION):
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Subnet TEST START [index : %d]" % (now.year, now.month, now.day, now.hour, now.minute, now.second,i))
    test_by_refer('subnet', 'create')
    test_by_refer('subnet', 'update')
    test_by_refer('subnet', 'delete')
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Subnet TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
init()

# Security Group TEST
test_by_refer('security_group', 'prepare')
for i in range(REPETITION):
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Security Group TEST START [index : %d]" % (now.year, now.month, now.day, now.hour, now.minute, now.second,i))
    test_by_refer('security_group', 'create')
    test_by_refer('security_group', 'update')
    test_by_refer('security_group', 'delete')
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Security Group TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
init()

# Instance TEST
test_by_refer('instance', 'prepare')
for i in range(REPETITION):
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Instance TEST START [index : %d]" % (now.year, now.month, now.day, now.hour, now.minute, now.second,i))
    test_by_refer('instance', 'create')
    test_by_refer('instance', 'update')
    test_by_refer('instance', 'delete')
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Instance TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
init()

#Block Storage TEST
test_by_refer('block_storage', 'prepare')
for i in range(REPETITION):
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Block Storage TEST START [index : %d]" % (now.year, now.month, now.day, now.hour, now.minute, now.second,i))
    test_by_refer('block_storage', 'create')
    test_by_refer('block_storage', 'update')
    test_by_refer('block_storage', 'attach')
    test_by_refer('block_storage', 'detach')
    test_by_refer('block_storage', 'delete')
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Block Storage TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
init()

# Public IP TEST
test_by_refer('public_ip', 'prepare')
for i in range(REPETITION):
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Public IP TEST START [index : %d]" % (now.year, now.month, now.day, now.hour, now.minute, now.second,i))
    test_by_refer('public_ip', 'create')
    test_by_refer('public_ip', 'attach')
    test_by_refer('public_ip', 'detach')
    test_by_refer('public_ip', 'delete')
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Public IP TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
init()

# Router TEST
test_by_refer('router', 'prepare')
for i in range(REPETITION):
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Router TEST START [index : %d]" % (now.year, now.month, now.day, now.hour, now.minute, now.second,i))
    test_by_refer('router', 'create')
    test_by_refer('router', 'update')
    test_by_refer('router', 'delete')
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Router TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
init()

# Loadbalancer TEST
test_by_refer('loadbalancer', 'prepare')
for i in range(REPETITION):
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Loadbalancer TEST START [index : %d]" % (now.year, now.month, now.day, now.hour, now.minute, now.second,i))
    test_by_refer('loadbalancer', 'create')
    test_by_refer('loadbalancer', 'update')
    test_by_refer('loadbalancer', 'delete')
    now = datetime.datetime.now()
    logger.debug("[%d.%d.%d %d:%d:%d] Loadbalancer TEST END [index : %d]" % (
    now.year, now.month, now.day, now.hour, now.minute, now.second, i))
init()

# Finish
now = datetime.datetime.now()
logger.debug("[%d.%d.%d %d:%d:%d] TTA1 TEST END " % (now.year, now.month, now.day, now.hour, now.minute, now.second))

handlers = logger.handlers[:]
for handler in handlers:
    handler.close()
    logger.removeHandler(handler)
driver.close()
driver.quit()
