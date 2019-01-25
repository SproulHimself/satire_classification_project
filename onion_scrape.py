import os
import re
import pdb
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
grads = {}
profile_links = []

# on_topics = ['politics', 'sports', 'local', 'entertainment', 'opinion']

# driver.get('http://politics.theonion.com')
# driver.get('https://www.theonion.com/c/sports-news-in-brief')

driver.get('https://www.theonion.com/c/american-voices')

# <h1 class="headline entry-title">
# <a class="js_link sc-1out364-0 fKfMlG" data-ga="[[&quot;Story Type page click&quot;,&quot;stream post click - 0&quot;,&quot;https://sports.theonion.com/rejection-from-hall-of-fame-sends-roger-clemens-spirali-1831995798&quot;,{&quot;metric19&quot;:1}]]"
# href="https://sports.theonion.com/rejection-from-hall-of-fame-sends-roger-clemens-spirali-1831995798#_ga=2.258282882.965796592.1548359101-1410968877.1546880908" rel="nofollow">
# <div>Rejection From Hall Of Fame Sends Roger Clemens Spiraling Into Performance-Enhancing-Drug Binge</div></a></h1>


# <h1 class="headline
# href="https://sports.theonion.com/rejection-from-hall-of-fame-sends-roger-clemens-spirali-1831995798" rel="nofollow"><div>Rejection From Hall Of Fame Sends Roger Clemens Spiraling Into Performance-Enhancing-Drug Binge</div></a>
# onion_base_urls = ['https://www.theonion.com/c/news-in-brief',
#                    'https://www.theonion.com/c/american-voices',
#                    'https://www.theonion.com/c/sports-news-in-brief']


# headlines = []
# body = []
# category = []
# topic = []
# mega_articles = []

article_urls = []

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



def get_art_links():
    urls = []
    s_urls = driver.find_elements_by_class_name("headline")
    for a in s_urls:
        link = a.find_element_by_css_selector('a')
        urls.append(link.get_attribute('href'))
    return urls




    # for c in content:
    #     link = c.find_element_by_css_selector('a')
    #     urls.append(link.get_attribute('href'))

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
