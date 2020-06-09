# -*- coding: utf-8 -*-
# @Author : Monster
# @File : user_page.py

import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from PageLocators.userpage_locators import UserPageLocator as UPL
from Common.basepage import BasePage


class UserPage(BasePage):



    #获取可用余额 #6155217812.95元,并返回float格式余额
    # def get_avabile_mount(self):
    #     WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(UPL.avabile_mount_text))
    #     self.mount = self.driver.find_element(*UPL.avabile_mount_text).text.split('元')[0]
    #     # 返回float格式余额, a.split('元')[0]
    #     amount = float(self.mount)
    #     return amount

    def get_avabile_mount(self):
        doc = "用户页面_获取可用余额"
        self.wait_eleVisible(UPL.avabile_mount_text,doc=doc)
        self.mount = self.get_text(UPL.avabile_mount_text,doc).split('元')[0]
        # 返回float格式余额, a.split('元')[0]
        amount = float(self.mount)
        return amount



