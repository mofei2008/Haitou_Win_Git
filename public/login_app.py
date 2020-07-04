from time import sleep
import uiautomator2 as u2
com = 'com.haitoutech.wealth'
act = '.activity.LandingPageActivity'
d = u2.connect('127.0.0.1:62001')

def login_app_mail():
    u'''输入用户名和密码,点击登录'''
    d(resourceId="com.haitoutech.wealth:id/tv_login").click()
    d(text='邮箱登录').click()
    d(resourceId="com.haitoutech.wealth:id/login_number").click()
    d(resourceId="com.haitoutech.wealth:id/login_number").set_text('lidetao@163.com')
    d(resourceId="com.haitoutech.wealth:id/login_password").click()
    d(resourceId="com.haitoutech.wealth:id/login_password").set_text('Aa111111')
    d(resourceId="com.haitoutech.wealth:id/login").click()
    sleep(2)
    d.make_toast("邮箱登录成功!", 3)

def login_app_mobile():
    d(resourceId="com.haitoutech.wealth:id/tv_login").click()
    d(text="手机号登录").click()
    d(resourceId="com.haitoutech.wealth:id/login_number").click()
    d(resourceId="com.haitoutech.wealth:id/login_number").set_text('18610806332')
    d(resourceId="com.haitoutech.wealth:id/login_password").click()
    d(resourceId="com.haitoutech.wealth:id/login_password").set_text('Aa111111')
    d(resourceId="com.haitoutech.wealth:id/login").click()
    sleep(2)
    d.make_toast("手机号登录成功!", 3)
