import time
import pyautogui
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.common.by import By

URL = 'https://registration.mfa.gov.ua/qmaticwebbooking/#/'
while True:
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	seti = webdriver.FirefoxOptions()
	seti.set_preference('dom.webdriver.enabled', False)
	seti.set_preference('dom.webnotifications.enabled', False)
	seti.set_preference('dom.volume_scale', '0.0')
	seti.set_preference('dom.useragent.override', 'nie')
	#seti.add_argument("--start-maximized")
	seti.add_argument("--private")
	seti.headless = True
	browser = webdriver.Firefox(options=seti)
	browser.set_window_size(1000, 10000)
	browser.get(URL)
	time.sleep(5)
	table = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div/ul')

	s = browser.find_element(By.XPATH, '//*[@id="branchBroup1"]').click()
	b1 = browser.find_element(By.XPATH, '/html/body/div/div/div/div/div/ul/li[1]/div[2]/div/div[2]/ul/li[1]/div[2]/div/div/div[1]/div/div/div/div').click()
	time.sleep(3)
	b2 = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[2]/div[2]/div/div[2]/div/div/ul/div[1]/div/div/div[1]/div/li[6]/div[1]/div[1]/div/div/div').click()
	b3 = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[3]/div[1]').click()
	time.sleep(3)
	def check():
		b4 = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/table')
		bb = b4.find_elements(By.TAG_NAME, "tr")
		for aa in bb:
			ab = aa.find_elements(By.TAG_NAME, "td")
			for aa in ab:
				try:
					o = aa.find_element(By.TAG_NAME, "button")
					to = o.get_attribute("class")
					if to == 'v-btn v-btn--flat v-btn--floating v-btn--disabled theme--light':
						pass
					else:
						o.text
				except:
					pass
		bebe = browser.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/ul/li[3]/div[2]/div/div[2]/div[1]/div/div/div[1]/button[2]').click()
		time.sleep(3)
	for x in range(3):
		check()

	print('пока ничего не обнаружено')
	time.sleep(30)
