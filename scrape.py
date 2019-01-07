

import re
import requests
from bs4 import BeautifulSoup
import os
import pdb 
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
grads = {}
profile_links = []

on_topics = ['politics', 'sports', 'local', 'entertainment', 'opinion']

# driver.get('http://politics.theonion.com')


headlines = []
body = []
category = []
topic = []

mega_articles = []

# first_art_link = driver.find_element_by_class_name("content-meta__headline__wrapper")
# webdriver.ActionChains(driver).move_to_element(first_art_link).click(first_art_link).perform()


#button2

def scroll_down():
	for i in range(1,5):
		try:
			modal_button = driver.find_element_by_class_name("button2")
			webdriver.ActionChains(driver).move_to_element(modal_button).click(modal_button).perform()
		except: 
			pass 
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)


def get_onion_arts(): 
	articles = []
	for topic in on_topics: 
		url = "http://" + topic + ".theonion.com"
		if topic == 'opinion': 
			url = "https://www.theonion.com/tag/opinion"
		
		driver.get(url)

		try: 
			first_art_link = driver.find_element_by_class_name("content-meta__headline__wrapper")
		except: 
			first_art_link = driver.find_element_by_class_name("headline")

		webdriver.ActionChains(driver).move_to_element(first_art_link).click(first_art_link).perform()

		scroll_down()
		# time.sleep(1)
		get_more()
		# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		# time.sleep(1)

		all_arts = driver.find_elements_by_class_name('js_reading-list-item')

		for art in all_arts: 
			try:
				modal_button = driver.find_element_by_class_name("button2")
				webdriver.ActionChains(driver).move_to_element(modal_button).click(modal_button).perform()
			except: 
				pass

			article = []
			try:
				headline = art.find_element_by_xpath(".//div[1]/header/header/h1/a").text
				try: 
					body = art.find_element_by_tag_name('p').text
					article.append(topic)
					article.append(headline)
					article.append(body)
				except: 
					article.append("no body")
					print("no body!")
			except:
				print("no headline")

			if article: 
				articles.append(article)
	return articles 

def get_more(): 
	for i in range(1,5):
		try:
			next_b = driver.find_element_by_xpath("//*[contains(text(), 'Load next Politics story')]")
			webdriver.ActionChains(driver).move_to_element(next_b).click(next_b).perform()
			time.sleep(.5)
		except: 
			pass 

def get_all_arts(): 
	all_arts = driver.find_elements_by_class_name('js_reading-list-item')

	for art in all_arts: 
		try:
			modal_button = driver.find_element_by_class_name("button2")
			webdriver.ActionChains(driver).move_to_element(modal_button).click(modal_button).perform()
		except: 
			pass

		article = []
		try:
			headline = art.find_element_by_xpath(".//div[1]/header/header/h1/a").text
			try: 
				body = art.find_element_by_tag_name('p').text
				article.append(topic)
				article.append(headline)
				article.append(body)
			except: 
				article.append("no body")
				print("no body!")
		except:
			print("no headline")

		if article: 
			mega_articles.append(article)





# def extra_on(): 
# 	first_art_link = driver.find_element_by_class_name("content-meta__headline__wrapper")
# 	webdriver.ActionChains(driver).move_to_element(first_art_link).click(first_art_link).perform()

# 	scroll_down()

# 	all_arts = driver.find_elements_by_class_name('js_reading-list-item')

# 	for art in all_arts: 
# 		try:
# 			modal_button = driver.find_element_by_class_name("button2")
# 			webdriver.ActionChains(driver).move_to_element(modal_button).click(modal_button).perform()
# 		except: 
# 			pass

# 		article = []
# 		try:
# 			headline = art.find_element_by_xpath(".//div[1]/header/header/h1/a").text
# 			try: 
# 				body = art.find_element_by_tag_name('p').text
# 				article.append(topic)
# 				article.append(headline)
# 				article.append(body)
# 			except: 
# 				article.append("no body")
# 				print("no body!")
# 		except:
# 			print("no headline")

# 		if article: 
# 			articles.append(article)





