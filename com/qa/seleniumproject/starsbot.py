from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#################################
#				#
#   Author: Subhan Ibrahimli	#
#   Date: 1/3/2019		#
# 				#
#################################



#                                                                   #
#                       CHANGE ID AND PASSWORD                      #
#                                                                   #
#                                                                   #


# --------------- STARS IMPLEMENTATION -------------------
# open Chrome browser and enter the url
binary = FirefoxBinary()
driver = webdriver.Firefox(executable_path='[WRITE DRIVER PATH HERE]/geckodriver')
#driver = webdriver.Firefox(firefox_binary=binary)
driver.get("https://stars.bilkent.edu.tr/accounts/login/")
windows_before = driver.current_window_handle[0]

# put ID number to the given box
login = driver.find_element_by_name("LoginForm[username]")
login.clear()
login.send_keys("[WRITE YOUR STARS ID HERE]", Keys.TAB)
login.send_keys(Keys.TAB)

# put password to the given box
pwd = driver.find_element_by_xpath("//div[@class='input-prepend']//input[@value='']")
pwd.click()
pwd.send_keys(" [WRITE YOUR STARS PASSWORD HERE] ", Keys.TAB)

# submit authentication by clicking button
driver.find_element_by_xpath('//button[@type="submit"]').click()


# --------------- EMAIL IMPLEMENTATION -------------------
time.sleep(2)
#driver = webdriver.Chrome() #("D:\PycharmProjects\SeleniumProject\drivers")
# open new tab to enter email
driver.execute_script("window.open()")
window_after = driver.switch_to.window(driver.window_handles[1])
#driver.minimize_window()
driver.get("https://webmail.bilkent.edu.tr/")
#driver.minimize_window()

# enter email
email = driver.find_element_by_id("rcmloginuser")
email.clear()
email.send_keys("[WRITE YOUR EMAIL HERE] ", Keys.TAB)

# enter password
pswd = driver.find_element_by_xpath("//input[@autocomplete='off']")
pswd.click()
pswd.send_keys("[WRITE EMAIL PASSWORD HERE]", Keys.TAB)

# click Login button
driver.find_element_by_xpath('//input[@type="submit"]').click()

time.sleep(5)

# click the first email
dblClk = driver.find_element_by_xpath("//div[@id='messagelistcontainer']//td[@tabindex='0']")
actionChains = ActionChains(driver)
actionChains2 = ActionChains(driver)
actionChains3 = ActionChains(driver)
actionChains.double_click(dblClk).perform()
actionChains2.double_click(dblClk).perform()
#actionChains3.double_click(dblClk).perform()

# get source code
#source = driver.execute_script("return document.body.innerHTML;")
#print(source)

# click the bottom frame
#driver.find_element_by_xpath('//html[@class=" js mozilla"]').click()

# get the text
#text_inside = driver.find_elements_by_class_name("messagebody").text
#text_inside = driver.find_element_by_class_name("pre").getText();
#print(text_inside)

#txt = driver.execute_script("return arguments[0].innerHTML", "pre")

#email_list = driver.find_element_by_id("mailview-bottom")
#items = email_list.find_elements_by_css_selector("div.class > br")
#items = email_list.find_elements_by_tag_name("span")
#for item in items:
#    txt = item.text
#    print(txt)

time.sleep(5)

# get the verification code from email
email_list = driver.find_element_by_xpath("//div[@id='mainscreen']//div[@id='mainscreencontent']//div[@id='messagebody']")
txt = email_list.get_attribute('textContent')                      #email_list.find_element_by_tag_name("br").text
txt = txt[19:24]
print(txt)

# switch to stars tab
windows_before = driver.current_window_handle[0]
driver.switch_to.window(driver.window_handles[0])

time.sleep(2)

#fill verification code
submitLogin = driver.find_element_by_name("EmailVerifyForm[verifyCode]")
time.sleep(2)
submitLogin.send_keys(txt, Keys.ENTER)


#submit code
#driver.find_element_by_xpath("//div[@class='bilkent-form-actions form-actions']//button[@type='submit']").click()
#driver.find_element_by_xpath('//button[@type="submit"]').click()


