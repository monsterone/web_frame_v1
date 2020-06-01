# -*- coding: utf-8 -*-
# @Author : Monster
# @File : user_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.userpage_locators import UserPageLocator as UPL

from selenium import webdriver

class UserPage:

    def __init__(self,driver):
        self.driver = driver

    #获取可用余额 #6155217812.95元,并返回float格式余额
    def get_avabile_mount(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(UPL.avabile_mount_text))
        self.mount = self.driver.find_element(*UPL.avabile_mount_text).text.split('元')[0]
        # 返回float格式余额, a.split('元')[0]
        amount = float(self.mount)
        return amount



