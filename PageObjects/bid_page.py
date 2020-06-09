# -*- coding: utf-8 -*-
# @Author : Monster
# @File : bid_page.py


import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from Common.basepage import BasePage
from PageLocators.bidpage_locators import BidPageLocator as BL
class BidPage(BasePage):



    #投资-按钮点的动
    def invest(self,mount):
        #在输入框当中，输入金额
        doc = "投资页面_投资操作"
        self.wait_eleVisible(BL.invest_input,doc=doc)
        self.input_text(BL.invest_input,mount,doc)
        #点击投标按钮
        self.click_element(BL.do_invest_button,doc)

    # 投资-按钮点不动
    def invest_no_click(self,mount):
        # 在输入框当中，输入金额
        doc = "投资页面_投资操作"
        self.wait_eleVisible(BL.invest_input, doc=doc)
        self.input_text(BL.invest_input, mount, doc)


    #获取用户余额(输入框)
    def get_uer_money(self):
        doc = "投资页面_获取用户余额(输入框)"
        self.wait_eleVisible(BL.invest_input,doc=doc)
        # 返回，获取输入框用户余额
        avalibute = self.get_element_attribute(BL.invest_input,"data-amount",doc=doc)
        return float(avalibute)


    # 投资成功的提示框-点击查看并激活
    def click_activeButton_on_success_popup(self):
        doc = "投资页面_投资成功的提示框"
        self.wait_eleVisible(BL.click_activeButton,doc=doc)
        self.click_element(BL.click_activeButton,doc)


    # 错误提示框-页面中间 (投标金额必须为100的倍数,请正确填写投标金额)
    def get_errorMsg_from_pageCenter(self):
        doc = "投资页面_错误提示框-页面中间"
        self.wait_eleVisible(BL.center_err_msg, doc=doc)
        # 获取文本内容
        msg = self.get_text(BL.center_err_msg,doc)
        # 关闭弹出框
        self.click_element(BL.center_err_msg_button, doc)
        return msg

    # 获取提示信息投标按钮上的
    def get_errorMsg_from_investButton(self):
        doc = "投资页面_获取提示信息投标按钮上的"
        self.wait_eleVisible(BL.err_invest_msg_button, doc=doc)
        # 获取文本内容
        return self.get_text(BL.err_invest_msg_button, doc)
