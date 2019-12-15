from  selenium import webdriver
import time
'''
1.打开浏览器
2.输入百度网站:http://www.baidu.com
3.在搜索框中输入 美女
4.点击搜索按钮
5.查看页面
'''
driver = webdriver.Firefox()#实例化浏览器
driver.get("http://www.baidu.com")#输入要打开的网站
aa =driver.find_element_by_id("cp").text #获得文本
print(aa)
driver.find_element_by_id("kw").send_keys("鸣人")#找到输入框并输入查找内容
time.sleep(4)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("鸣人")
driver.find_element_by_id("su").click()#点击百度一下
driver.close()#关闭当前
driver.quit()#关闭打开的所有页面

# 基本操作 get(打开网页),send_keys,click,close,quit,clear(清除).text(文本) back()(返回上一级)
# driver.current.url 判断访问是否有效
# a =webdriver.Firefox()#实例化浏览器
# a.get("http://www.baidu.com")
# a.find_element_by_id("kw").send_keys("我最爱蜗牛")
# a.find_element_by_id('su').click()
# time.sleep(5)
# a.find_element_by_id('kw').clear()
# a.find_element_by_id('kw').send_keys('手机')
# time.sleep(3)
# a.find_element_by_id('su').click()
# b=a.find_element_by_class_name("nums").text
# print(b)
# a.find_elements_by_tag_name('input')[7].send_keys('标签')
# 八种元素查找器 :
# id ,classname ,link(链接全匹配,)partial_link(链接模糊匹配) name=id
# tag_name,xpath,css_selector
# 万能查找器:find_element()
# 频率最多 : id - name - xpath--partial_link_text--link_text--class_name
# 1.弹出框的处理：
# driver.switch_to.alert.dismiss()   #取消
# driver.switch_to.alert.accept()    #确认'''
# # print(driver.switch_to.alert.text)#打印弹出框内容
# driver.find_element_by_id("username").send_keys("admin")
# driver.find_element_by_id("password").send_keys("admin")
# driver.find_element_by_id("login").click()
