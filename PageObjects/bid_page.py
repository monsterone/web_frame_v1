# -*- coding: utf-8 -*-
# @Author : Monster
# @File : bid_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from PageLocators.bidpage_locators import BidPageLocator as BL
class BidPage:

    def __init__(self,driver):
        self.driver=driver

    #投资-按钮点的动
    def invest(self,mount):
        #在输入框当中，输入金额
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BL.invest_input))
        self.driver.find_element(*BL.invest_input).send_keys(mount)
        #点击投标按钮
        self.driver.find_element(*BL.do_invest_button).click()

    # 投资-按钮点不动
    def invest_no_click(self,mount):
        #在输入框当中，输入金额
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BL.invest_input))
        self.driver.find_element(*BL.invest_input).send_keys(mount)


    #获取用户余额(输入框)
    def get_uer_money(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BL.invest_input))
        # 返回，获取输入框用户余额
        # return self.driver.find_element(BL.invest_input).text()
        avalibute = self.driver.find_element(*BL.invest_input).get_attribute("data-amount")
        return float(avalibute)


    # 投资成功的提示框-点击查看并激活
    def click_activeButton_on_success_popup(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BL.click_activeButton))
        self.driver.find_element(*BL.click_activeButton).click()


    # 错误提示框-页面中间 (投标金额必须为100的倍数,请正确填写投标金额)
    def get_errorMsg_from_pageCenter(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BL.center_err_msg))
        # 获取文本内容
        msg = self.driver.find_element(*BL.center_err_msg).text
        # 关闭弹出框
        self.driver.find_element(*BL.center_err_msg_button).click()

        return msg

    # 获取提示信息投标按钮上的
    def get_errorMsg_from_investButton(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(BL.err_invest_msg_button))
        return self.driver.find_element(*BL.err_invest_msg_button).text