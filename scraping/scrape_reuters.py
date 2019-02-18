import re
import requests
from bs4 import BeautifulSoup
import os
import pdb
import time
from url_data import mega_list

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(10)

driver.get('https://uk.reuters.com/news/archive/worldnews?view=page&page=1&pageSize=10')

heads = []
urls = []
bodies = []


def click_accept_cookies():
    cookie_button = driver.find_element_by_class_name('evidon-banner-acceptbutton')
    webdriver.ActionChains(driver).move_to_element(cookie_button).click(cookie_button).perform()

click_accept_cookies()

def next_page():
    next_button = driver.find_element_by_class_name('control-nav-next')
    webdriver.ActionChains(driver).move_to_element(next_button).click(next_button).perform()
# <button id="_evidon-accept-button" class="evidon-banner-acceptbutton"


def get_reuters_arts():
    headers = driver.find_elements_by_class_name('story-title')
    stories = driver.find_elements_by_class_name('story')
    content = driver.find_elements_by_class_name('story-content')

    for header in headers:
        heads.append(header.text)

    for c in content:
        link = c.find_element_by_css_selector('a')
        urls.append(link.get_attribute('href'))


def get_bodies():
    for i in urls:
        print(str(i + 1))
        body = []
        driver.get(i)
        time.sleep(2)
        bods = driver.find_elements_by_css_selector('p')
        for bod in bods:
            body.append(bod.text)
        body = ' '.join(body)
        bodies.append(body)


def run_reuters_scrape():
    click_accept_cookies()
    time.sleep(1)

    for i in range(77):
        print(str(i + 1))
        get_reuters_arts()
        time.sleep(2)
        next_page()
        time.sleep(2)

    get_bodies()


listyy = ['https://uk.reuters.com/article/uk-china-military/chinas-xi-calls-on-army-to-be-battle-ready-idUKKCN1OZ043', 'https://uk.reuters.com/article/uk-usa-shutdown/trump-threatens-years-long-government-shutdown-emergency-powers-to-build-wall-idUKKCN1OY0D5', 'https://uk.reuters.com/article/uk-mexico-politics/mexican-president-owns-no-cars-or-real-estate-but-his-wife-does-idUKKCN1OZ01W', 'https://uk.reuters.com/article/uk-washington-state-marijuana/washington-governor-to-pardon-pot-crimes-six-years-after-legalisation-idUKKCN1OZ01N', 'https://uk.reuters.com/article/uk-usa-congress-investigations/newly-powerful-u-s-house-democrats-hold-off-on-trump-subpoena-flurry-idUKKCN1OY1YD', 'https://uk.reuters.com/article/uk-venezuela-politics/mexico-urges-regional-bloc-not-to-meddle-in-venezuela-idUKKCN1OY1R2', 'https://uk.reuters.com/article/uk-usa-immigration-border/central-american-migrants-protest-closure-of-tijuana-shelter-idUKKCN1OZ00Z', 'https://uk.reuters.com/article/uk-nigeria-election/nigerias-buhari-says-electoral-commissioner-is-related-by-marriage-idUKKCN1OZ00T']

bodytest = []

def get_body(list_of_urls):
    for idx, val in enumerate(list_of_urls):
        count = idx + 1
        body = []
        driver.get(val)
        time.sleep(3)
        bods = driver.find_elements_by_css_selector('p')
        for bod in bods:
            body.append(bod.text)
        body = ' '.join(body)
        print(body[:50], "count: ", count)
        bodytest.append(body)
    print(len(bodytest))

def get_all_articles(list_of_urls):
    for idx, val in enumerate(list_of_urls):
        count = idx + 1
        article = []
        body = []
        driver.get(val)
        headline = driver.find_element_by_tag_name('h1').text
        article.append(headline)
        print(headline, " count: ", count)
        bods = driver.find_elements_by_css_selector('p')
        for bod in bods:
            body.append(bod.text)
        body = ' '.join(body)
        article.append(body)
        bodytest.append(article)
    print(len(bodytest))

def write_to_file(u_list):
	outF = open("url_data.txt", "w+")
	string_list = str(u_list)
	outF.write(string_list)
	outF.close




def remove_footer(dirty_string):
   sep = " (Reuters) - "
   if sep in dirty_string:
       clean = dirty_string.split(sep, 1)[0]
   else:
       clean = dirty_string
   return clean

# filename = "reuters_body_list.txt"
# file = open("reuters_body_list.txt","w+")
# reuters_string = str(bodytest)
# file.write(reuters_string)
# file.close

    # for link in content:
        # print(link.get_attributes('a'))

        # htmls.append(link)

#
# el = driver.find_element_by_css_selector("a.link")
# if el:
#     url = el.get_attribute("href")


#######################################################################################################
