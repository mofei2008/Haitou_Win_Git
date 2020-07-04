from time import sleep

# class Login():
def login_mail(browser):
    u'''输入用户名和密码,点击登录'''
    browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/span").click()
    sleep(2)
    browser.find_element_by_css_selector("[type='text']").click()
    sleep(1)
    browser.find_element_by_css_selector("[type='text']").send_keys("lidetao@163.com")
    sleep(1)
    browser.find_element_by_css_selector("[placeholder = '请输入登录密码']").click()
    sleep(1)
    browser.find_element_by_css_selector("[placeholder = '请输入登录密码']").send_keys("Aa111111")
    sleep(1)
    browser.find_element_by_css_selector("[type='button']").click()
    sleep(3)

def login_mobile(browser):
    u'''输入用户名和密码,点击登录'''
    browser.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/span").click()
    sleep(2)
    browser.find_element_by_xpath("/html//div[@id='app']//div[@role='tablist']/div[2]/span[@class='van-tab__text']").click()
    sleep(1)
    browser.find_element_by_xpath("/html//div[@id='app']/div[@class='app']//div[@class='van-tabs__track']/div[2]//form//input[@type='text']").click()
    sleep(1)
    browser.find_element_by_xpath("/html//div[@id='app']/div[@class='app']//div[@class='van-tabs__track']/div[2]//form//input[@type='text']").send_keys("18610806332")
    sleep(1)
    browser.find_element_by_css_selector(".van-tabs__track .van-tab__pane-wrapper:nth-of-type(2) [placeholder='请输入登录密码']").click()
    sleep(1)
    browser.find_element_by_css_selector(".van-tabs__track .van-tab__pane-wrapper:nth-of-type(2) [placeholder='请输入登录密码']").send_keys("Aa111111")
    sleep(1)
    browser.find_element_by_css_selector(".van-tabs__track .van-tab__pane-wrapper:nth-of-type(2) [type='button']").click()
    sleep(3)

def login_jd(browser):
    u'''输入用户名和密码,点击登录'''
    browser.find_element_by_css_selector(".index.o2_window")
    sleep(2)
    browser.find_element_by_css_selector("[type='text']").click()
    sleep(1)
    browser.find_element_by_css_selector("[type='text']").send_keys("lidetao@163.com")
    sleep(1)
    browser.find_element_by_css_selector("[placeholder = '请输入登录密码']").click()
    sleep(1)
    browser.find_element_by_css_selector("[placeholder = '请输入登录密码']").send_keys("Aa111111")
    sleep(1)
    browser.find_element_by_css_selector("[type='button']").click()
    sleep(3)