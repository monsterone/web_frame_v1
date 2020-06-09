

import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageLocators.indexpage_locators import IndexPageLocator as IL
from Common.basepage import BasePage
BASE_DIR=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

class IndexPage(BasePage):


    #断言
    def isExist_logout_ele(self):
        #如果存在就返回True,如果不存在，就返回False
        try:
            doc = "首页页面_断言登录"
            self.wait_eleVisible(IL.index_logout,doc=doc)
            return True
        except:
            return False

    # 选标操作-默认选第一个=元素定位的时候，过滤掉不可以投的标。
    def click_first_bid(self):
        self.driver.find_elements(*IL.invest_button)[0].click()


    # 随机选一个标   //a[text()="抢投标"]
    def click_bid_by_random(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_any_elements_located(IL.invest_button))
        # 找到所有符合的标
        eles = self.driver.find_elements(*IL.invest_button)
        # 随机数
        index = random.randint(0,len(eles)-1)
        eles[index].click()


