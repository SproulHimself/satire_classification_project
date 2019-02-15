import re
import requests
from bs4 import BeautifulSoup
import os
import pdb 
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')


# driver.get("https://www.newyorker.com/humor/borowitz-report")
def write_to_file(prep, arts_list):
	name = "squib_" + prep +  ".txt"
	outF = open(name, "w+")
	string_list = str(arts_list)
	outF.write(string_list) 
	outF.close()

# https://www.dailysquib.co.uk/world/30788-obama-oprah-orourke-ocasio-why-socialist-americans-love-o-so-much.html

driver.get("https://www.dailysquib.co.uk/world/29249-think-tank-the-goal-of-social-media.html")

articles = []

for i in range(1,700):
	time.sleep(1)
	article = []
	headline = driver.find_element_by_tag_name('h1').text
	article.append(headline)
	print("headline: ", headline, " # ", i)
	body = driver.find_element_by_class_name('td-post-content').text

	body_cleaned = re.sub(r"\s+", " ", body)

	article.append(body_cleaned)

	nav_left = driver.find_element_by_class_name('td-post-prev-post')
	link = nav_left.find_element_by_xpath(".//a")
	webdriver.ActionChains(driver).move_to_element(link).click(link).perform()

	articles.append(article)



