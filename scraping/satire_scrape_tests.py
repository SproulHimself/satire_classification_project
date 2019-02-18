
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


driver.get('http://politics.theonion.com')




headlines = []
body = []
category = []
topic = []


first_art_link = driver.find_element_by_class_name("content-meta__headline__wrapper")
webdriver.ActionChains(driver).move_to_element(first_art_link).click(first_art_link).perform()


item_headline = item.find_element_by_tag_name('h1')
content-meta__headline__wrapper

/html/body/div[7]/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/div

//*[@id="post_1823468346"]/div[1] ./header/header/h1/a
.find_element_by_xpath(".//*h1")

element2.find_element_by_xpath(".//p[@class='test']").text 

.find_element_by_class("headline hover-highlight entry-title js_entry-title")

art = 

headlines = driver.find_elements_by_class_name("headline hover-highlight entry-title js_entry-title")

graphs = driver.find_elements_by_tag("p")

#skip element 0 
headline = element2.find_element_by_xpath(".//div[1]/header/header/h1/a").text

body = element2.find_element_by_tag_name('p').text

/html/body/div[9]/div[2]

"main"

.find_element_by_class_name('main')

/html/body/div[9]/div[2]
//*[@id="post_1823468346"]/div[1]/header/header/h1/a


def sign_in(username, password):

	driver.get('https://www.linkedin.com/')

	user_input = driver.find_element_by_id('login-email')
	password_input = driver.find_element_by_id('login-password')
	user_input.send_keys(username)
	password_input.send_keys(password)
	password_input.send_keys(Keys.ENTER)
	print("you should be logged in now")
	time.sleep(2)
	driver.get("https://www.linkedin.com/recruiter/smartsearch")

	#check for modal
	# 8qjJ70Z1

def start_search():

	# go to smartsearch page
	driver.get("https://www.linkedin.com/recruiter/smartsearch")
	time.sleep(3)

	# open up years of graduation field
	grad_button = driver.find_element_by_xpath("//*[@id='facet-eduYears']/div/ul/li/span")
	webdriver.ActionChains(driver).move_to_element(grad_button).click(grad_button).perform()
	time.sleep(2)

	#find and enter start year of 2017
	start_year = driver.find_element_by_xpath("//*[@id='eduYears-range-from']")
	webdriver.ActionChains(driver).move_to_element(start_year).double_click(start_year).perform()
	start_year.send_keys("20")
	start_year.send_keys("17")
	time.sleep(2)

	#find and enter end year of 2017 
	end_year = driver.find_element_by_xpath("//*[@id='eduYears-range-to']")
	webdriver.ActionChains(driver).move_to_element(end_year).double_click(end_year).perform()
	end_year.send_keys("2")
	end_year.send_keys("01")
	end_year.send_keys("7")
	time.sleep(2)

	#click on the "add" button to add filter 
	year_button = driver.find_element_by_xpath("//*[@id='facet-eduYears']/div/form[2]/div/div/p[2]/button[2]")
	webdriver.ActionChains(driver).move_to_element(year_button).click(year_button).perform()
	time.sleep(3)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(2)
	driver.execute_script("window.scrollTo(0, 0);")
	time.sleep(1)

	#find the first profile 
	first_profile = driver.find_element_by_xpath("//*/div/h3/a")
	time.sleep(1)

	# old code for getting all the profile links 
	# links_25 = driver.find_elements_by_xpath("//*/div/h3/a")
	# for link in links_25: 
	# 	grads[link.text] = link.get_attribute("href")
	# next_25 = driver.find_element_by_xpath("//*[@id='pagination']/div/ul/li[11]/a")
	# webdriver.ActionChains(driver).move_to_element(next_25).click(next_25).perform()
	# for link in links_25: 
	# 	grads[link.text] = link.get_attribute("href")

	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1)

	driver.get(first_profile.get_attribute('href'))
	time.sleep(3)

	for i in range(1,5002):
		body = ''
		try: 
			time.sleep(1)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			driver.execute_script("window.scrollTo(0, 0);")
			time.sleep(1)
			body = driver.find_element_by_xpath("//*[@id='primary-content']")
		except Exception as e: 
			print("in the profile loop  ", e, "  ", i)
			time.sleep(1)
			body = driver.find_element_by_xpath("//*[@id='primary-content']")
		if body: 
			filename = "batch2_" + str(i) + ".html"
			file = open(filename,"w+")
			html_string = body.get_attribute('innerHTML')
			file.write(html_string)
			time.sleep(2)
			print("saved a profile", i)

			if i <= 1: 
				next_profile = driver.find_element_by_xpath("//*[@id='profile-breadcrumbs']/div/ul/li/a/span[2]")
			else: 
				next_profile = driver.find_element_by_xpath('//a[@title="Next Page"]')

			webdriver.ActionChains(driver).move_to_element(next_profile).click(next_profile).perform()
			time.sleep(2)
		else: 
			print('body was empty ', i)

	print("that's all?")

def search_from_profile(pref, limit=1000): 
	for i in range(1,limit+1):
		body = ''

		try: 
			time.sleep(1)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
			driver.execute_script("window.scrollTo(0, 0);")
			time.sleep(1)
			body = driver.find_element_by_xpath("//*[@id='primary-content']")
		except Exception as e: 
			print("in the profile loop  ", e, "  ", i)
			time.sleep(1)
			body = driver.find_element_by_xpath("//*[@id='primary-content']")

		if body: 
			filename = pref + "_" + str(i) + ".html"
			file = open(filename,"w+")
			html_string = body.get_attribute('innerHTML')
			file.write(html_string)
			time.sleep(2)
			print("saved a profile", i)
		else: 
			print('body was empty ', i)

		if i <= 1: 
			next_profile = driver.find_element_by_xpath("//*[@id='profile-breadcrumbs']/div/ul/li/a/span[2]")
		else: 
			next_profile = driver.find_element_by_xpath('//a[@title="Next Page"]')

		webdriver.ActionChains(driver).move_to_element(next_profile).click(next_profile).perform()
		time.sleep(2)


def like_all_unliked_from_user(user, limit=20):
	url = 'https://www.instagram.com/' + user 
	driver.get(url)
	current_count = 0
	driver.maximize_window()
	post_list = ""
	post_list2 = ""
	heart_like = ""
	time.sleep(1)

	try: 

		post_list = driver.find_element_by_class_name('Ln-UN')

	except Exception as e:

			print("post_list didn't work", e)

			try: 

				post_list2 = driver.find_element_by_class_name('eLAPa')

			except Exception as e:

				print("NoSuchElementException", e)

	time.sleep(1)

	if post_list: 
		webdriver.ActionChains(driver).move_to_element(post_list).click(post_list).perform()
	if post_list2: 
		webdriver.ActionChains(driver).move_to_element(post_list2).click(post_list2).perform()

	
	for like in range(limit): 
		# get the heart 

		like_xpath = "//section/span/button/span[@aria-label='Like']"
		unlike_xpath = "//section/span/button/span[@aria-label='Unlike']"

		try: 

			heart_like = driver.find_element_by_xpath("//section/span/button/span[@aria-label='Like']")

		except Exception as e:

			print(e)

		# heart_unlike = driver.find_element_by_xpath("//section/span/button/span[@aria-label='Unlike']")
		time.sleep(1)
		if heart_like: 

			webdriver.ActionChains(driver).move_to_element(heart_like).click(heart_like).perform()
		time.sleep(1)

		if like == 1: 		
			#next_button 
			first_right_arrow = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a')
			#click on next button 
			webdriver.ActionChains(driver).move_to_element(first_right_arrow).click(first_right_arrow).perform()
			print("did the first like!")
		elif like > 1: 
			next_right_arrow = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a[2]')
						#click on next button 
			webdriver.ActionChains(driver).move_to_element(next_right_arrow).click(next_right_arrow).perform()
			print("did the next like number", like)
		heart_like = ''
		time.sleep(1)
	print("that's all of 'em ")



	# images = driver.find_elements_by_tag_name('img')
	# first_pic = images[0]

	# try: 
	# 	poke_pic = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[4]/article")

	# 	poke_pic2 = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[4]/article/div/div")
	# except: 
	# 	print("it didn't work")

	# webdriver.ActionChains(driver).move_to_element(poke_pic).click(poke_pic).perform()
	# post_picture = driver.find_element_by_xpath('//*[@id='react-root']/section/main/div/div[2]/a[1]/span/span')

	# first_pic = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[4]/article/div/div/div[1]/div[1]/a/div")
	#click on first picture 
	# webdriver.ActionChains(driver).move_to_element(first_pic).click(first_pic).perform()

		# heart_unlike = driver.find_element_by_xpath("//section/span/button/span[@aria-label='Unlike']")
		# heart = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span")
		# heart_class = inner_heart.get_attribute('class') 
		# #check to see if the heart is grey - its red if already liked
		# if 'grey' in current_attribute:
		# 	webdriver.ActionChains(driver).move_to_element(inner_heart).click(inner_heart).perform()

		# "Like my recents?" is a common refrain amongst my teenage daughter's friends these days. Instagram like, comments, and follows have social currency for her and her friends in ways that older people can hardly understand. With good reason the current stereotypical image of a teenager is one that is absorbed by their smartphone screen. I get it. But lately I've noticed that much of that screen time is spent drudging through the semi-mechanical chore of "liking recents". Whenever I see a repetitive task being done with technology, I can't help but think that there has to be a way to automate it. And my daughter was game to do it with me. Enter Selenium.
