

from selenium.webdriver.common.by import By

# 用户页面元素定位
class UserPageLocator:

    # 元素定位
    # 可用余额文本
    avabile_mount_text = (By.XPATH,'//li[@class="color_sub"]')