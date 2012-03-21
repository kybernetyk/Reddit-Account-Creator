#!/usr/bin/env python

###################################################################
#
# Reddit Account Creator
#
# deps:
#		-selenium
#		-firefox
#		-de-captcher.com account
#
#	license: GPL3 (c) Leon Szpilewski
#
###################################################################
from selenium import webdriver
import captcha

username = "koksbanane2001"
password = "ficken"

# don't change anything below

browser = webdriver.Firefox()

browser.get('http://reddit.com');
browser.get(browser.find_element_by_class_name('login-required').get_attribute('href'))

browser.find_element_by_id('user_reg').click()
browser.find_element_by_id('user_reg').send_keys(username)

browser.find_element_by_id('passwd_reg').click()
browser.find_element_by_id('passwd_reg').send_keys(password)

browser.find_element_by_id('passwd2_reg').click()
browser.find_element_by_id('passwd2_reg').send_keys(password)

captcha_url = browser.find_element_by_class_name('capimage').get_attribute('src')

print "solving captcha: " + captcha_url
print "be patient ..."
solved_captcha = captcha.solve(captcha_url)
print "done."

browser.find_element_by_id('captcha_').click()
browser.find_element_by_id('captcha_').send_keys(solved_captcha)

for btn in browser.find_elements_by_class_name('button'):
	if btn.text == 'create account':
		btn.click()
		break

