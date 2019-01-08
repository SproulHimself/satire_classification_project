import re
import requests
from bs4 import BeautifulSoup
import os
import pdb 
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

base_url = "http://www.satirewire.com/content1/?cat="

url_dict = {'15': 'arts', '16':'sports', '24':'sci-tech', '14': 'business', '17': 'international', '13': 'authority'}

codes = list(url_dict.keys())

# for code in codes: 
# 	url = base_url + code 
# 	topic = url_dict[code]

driver.get("http://www.satirewire.com/content1/?p=6610")

# driver.get("http://www.satirewire.com/content1/?p=6371")
def write_to_file(arts_list):
	outF = open("satirewire_data.txt", "w+")
	string_list = str(arts_list)
	outF.write(string_list) 
	outF.close

articles = []
first_art = driver.find_element_by_tag_name('h2') 
webdriver.ActionChains(driver).move_to_element(first_art).click(first_art).perform()
for i in range(1,1000):
	time.sleep(1)
	article = []
	
	headline = driver.find_element_by_tag_name('h2').text 
	article.append("no-topic")
	article.append(headline)
	print(headline, "story # ", i)

	body = driver.find_element_by_class_name('entry').text
	body_cleaned = re.sub(r"\s+", " ", body)
	sep = 'Copyright ©'

	body_squeaky = body_cleaned.split(sep, 1)[0]
	article.append(body_squeaky)

	articles.append(article)

	nav_left = driver.find_element_by_class_name('bnavleft')
	link = nav_left.find_element_by_xpath(".//a")
	webdriver.ActionChains(driver).move_to_element(link).click(link).perform()


	# nav_right = driver.find_element_by_class_name('bnavleft')
	# webdriver.ActionChains(driver).move_to_element(nav_left).click(nav_left).perform()
	time.sleep(1)


def write_to_file(arts_list):
	outF = open("satirewire_data.txt", "w+")
	string_list = str(arts_list)
	outF.write(string_list) 
	outF.close






