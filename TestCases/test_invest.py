# -*- coding: utf-8 -*-
# @Author : Monster
# @File : test_invest.py

#独立的测试账号


#正常用例
#前提条件：
####################（尽量不要依赖测试环境的数据，如果没有，就自己造环境）#########
#1、用户已登陆
#2、有能够投资的标#如果没有标，则先加标。#接口的方式加标。
#3、用户有余额可以投资
    #1、1个亿
    #2、接口方式：查询当前用户还有多少钱。>6000不用充值。如果小于用例中投资的金额，那就充值。


#步骤
#1、在首页选标—不根据标名，根据抢投标。默认第一个标。
###标页面-获取一下投资前的用户余额
#2、标页面-输入投资金额、点击投资按钮
#3、标页面-点击投资成功的弹出框-查看并激活，进入个人页面

#断言
#钱投资后的金额，是不是少了投资的量。
#个人页面-获取投资后的金额
# 投资前的金额一投资后的金额=投资金额

#投资记录对不对


# -------------------


#异常用例：非常好创造环境，非常好写的。

#不考虑自动化实现
#异常用例：全投操作？标的可投金额〉个人余额    （异常复杂可以不要自动化，手工验证就好）
            #投资金额〉标的可投金额#满足这种条件标、用户



import unittest

import pytest
from selenium import webdriver
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from PageObjects.login_page import LoginPage
from PageObjects.user_page import UserPage

from TestDatas import common_datas as CD
from TestDatas import invest_datas as IDs
from Common.logger import Logger
import ddt
import time
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
logger = Logger(__name__).getlog()

@pytest.mark.usefixtures("access_invest")
@pytest.mark.usefixtures("refresh_page")
@pytest.mark.invest
class TestInvest():
    # logger = Logger(__name__).getlog()
    # @classmethod
    # def setUpClass(cls):
    #     # 初始化浏览器会话
    #     logger.info("======用例类前置：初始化浏览器会话，登录XXX系统======")
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.get(CD.web_login_url)
    #     LoginPage(cls.driver).login(CD.user, CD.passwd)
    #     #首页-选一个标来投资，直接选第一个标/随机选一个标
    #     IndexPage(cls.driver).click_bid_by_random()
    #     ## 投标页面
    #     cls.bid_page = BidPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     logger.info("======用例类后置：关闭浏览器会话，清理环境======")
    #     cls.driver.quit()
    #
    # def setUp(self):
    #    pass
    #
    # def tearDown(self):
    #     logger.info("======每一个用例后置：刷新当前页面======")
    #     self.driver.refresh()
    #     time.sleep(0.5)

    # #进入投标页面函数
    # def into_inverst(self):
    #     ## 首页面
    #     self.ig = IndexPage(self.driver)
    #     # 点击抢投标，进入投标页面
    #     self.ig.click_bid_by_random()
    #     ## 投标页面
    #     self.bg = BidPage(self.driver)


    # # 正常用例 - 投标成功
    # def test_invest_success(self):
    #     # 步骤
    #     # 1、在首页选标—不根据标名，根据抢投标。默认第一个标。
    #     ###标页面-获取一下投资前的用户余额
    #     # 2、标页面-输入投资金额、点击投资按钮
    #     # 3、标页面-点击投资成功的弹出框-查看并激活，进入个人页面
    #     # 断言
    #     # 钱投资后的金额，是不是少了投资的量。
    #     # 个人页面-获取投资后的金额
    #     # 投资前的金额一投资后的金额=投资金额
    #
    #     # 调用进入投标页面函数
    #     self.into_inverst()
    #     #获取输入框资前的用户余额
    #     befor_amount = self.bg.get_uer_money()
    #
    #     #正常投资
    #     self.bg.invest(IDs.inverst_success["money"])
    #     #点击投资成功的弹出框-查看并激活
    #     self.bg.click_activeButton_on_success_popup()
    #
    #     ## 用户页面
    #     self.ug = UserPage(self.driver)
    #     # 获取投资后的金额
    #     after_amount = self.ug.get_avabile_mount()
    #     #断言：
    #     self.assertEqual(befor_amount-after_amount,IDs.inverst_success["check"])


    #正常投资-成功


    # 异常用例 - 弹框提示
    # @ddt.data(*IDs.inverst_fail_alert)
    @pytest.mark.parametrize("data",IDs.inverst_fail_alert)
    def test_invest_0_failed_nol00(self,data,access_invest):
        logger.info("******投资用例：异常场景-投标金额不是 100的整数倍、错误格式 ******")

        # 标页面 - 获取投资前的个人余额
        userMoney_beforeInvest = access_invest[1].get_uer_money()
        # 标页面 - 输入投标金额，点击投标按钮
        access_invest[1].invest(data["money"])
        # 获取提示信息
        errorMsg = access_invest[1].get_errorMsg_from_pageCenter()
        # 刷新
        access_invest[0].refresh()
        # 标页面 - 获取用户余额（输入框）
        userMoney_afterInvest = access_invest[1].get_uer_money()

        #断言
        assert errorMsg == data["check"]
        assert userMoney_afterInvest == userMoney_beforeInvest


    # 异常用例 - 按钮提示
    # @ddt.data(*IDs.inverst_fail_button)
    @pytest.mark.parametrize("data",IDs.inverst_fail_button)
    def test_invest_1_failed_noButton(self, data,access_invest):
        logger.info("******投资用例：异常场景-投标金额不是10的整数倍-按钮可不点击 ******")

        # 标页面 - 获取投资前的个人余额
        userMoney_beforeInvest = access_invest[1].get_uer_money()
        # 标页面 - 输入投标金额不是 10的整数倍，按钮可不点击
        access_invest[1].invest_no_click(data["money"])
        # 获取提示信息
        errorMsg = access_invest[1].get_errorMsg_from_investButton()
        # 刷新
        access_invest[0].refresh()
        # 标页面 - 获取用户余额（输入框）
        userMoney_afterInvest = access_invest[1].get_uer_money()

        # 断言
        assert errorMsg == data["check"]
        assert userMoney_afterInvest == userMoney_beforeInvest

    @pytest.mark.smoke
    def test_invest_2_success(self, access_invest):
        logger.info("******投资用例：正常场景-投资成功 ******")
        # 标页面 - 获取投资前的个人余额
        userMoney_beforeInvest = access_invest[1].get_uer_money()
        # 标页面 - 输入投标金额，点击投标按钮
        access_invest[1].invest(IDs.inverst_success["money"])
        # 标页面 - 投资成功的弹出框,点击查看并激活
        access_invest[1].click_activeButton_on_success_popup()
        ## 断言
        # 个人页面 - 获取用户当前余额
        userMoney_afterInvest = UserPage(access_invest[0]).get_avabile_mount()
        # 余额，投资前后对比
        # self.assertEqual(userMoney_beforeInvest - userMoney_afterInvest, IDs.inverst_success["check"])
        # 在数据没有在page页面float处理的情况，可以参考下面的断言，更简洁
        # assert IDs.inverst_success["check"] == int(float(userMoney_beforeInvest)-float(userMoney_afterInvest))
        assert IDs.inverst_success["check"] == (userMoney_beforeInvest - userMoney_afterInvest)







