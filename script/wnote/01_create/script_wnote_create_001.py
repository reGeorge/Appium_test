#coding=utf-8
from appium import webdriver
import time

# 1、获取当前界面的activity:adb shell dumpsys window | findstr "mFocusedWindow"
# 2、获取包名&界面元素:AndroidSDK\tools\bin\uiautomatorviewer.bat
# 3、查看python模块方法:python -m pydoc -p 4567	http://localhost:4567/appium.webdriver.webdriver.html

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.regeorge.wnote'
desired_caps['appActivity'] = 'com.regeorge.wnote.activity.MainActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# adb shell am start -n com.regeorge.wnote/com.regeorge.wnote.activity.MainActivity
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("new_btn").click()

# driver.find_element_by_id("a_edtext").set_text('1')
# driver.find_element_by_id("a_edtext").send_keys('adb')

# 报错
# driver.find_element_by_id("a_edtext").set_value(u'中文')

# 不报错，但无输入(将键盘隐藏后可以输入)
driver.find_element_by_id("a_edtext").set_text(u'中文')
# driver.find_element_by_id("a_edtext").send_keys(u'中文')

# driver.find_element_by_id("a_edtext").set_text('中文'.decode('utf-8'))
# driver.find_element_by_id("a_edtext").send_keys('中文'.decode('utf-8'))

driver.find_element_by_id("check").click()

time.sleep(10)

driver.quit()