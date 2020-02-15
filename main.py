#importing all the necessary packages
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

#Enter the input
search=input("Enter the video name")
driver = webdriver.Chrome('/home/tennyson/Desktop/mail/chromedriver')

#Send a get Request to the url
driver.get('https://www.youtube.com/results?search_query='+search);

#Click on the first recommended video
search_box1 = driver.find_element_by_id('dismissable')
search_box1.click()

try:
	#Wait for the advertisement skip button to display
	element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("ytp-ad-skip-button ytp-button"))
	element.click()
	element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("ytp-ad-skip-button ytp-button"))
	element.click()
except TimeoutException:
	pass
finally:
	#Play the video until remaining time is 1
	while(True):
		length_str=driver.find_element_by_class_name("ytp-time-duration").text
		current_time_str = driver.find_element_by_class_name("ytp-time-current").text
		import re
		length = re.findall(r'\d+', length_str) # convert ['2:24'] to ['2', '24']
		current_time = re.findall(r'\d+', current_time_str)
		if( len(length) >0 and  len(current_time)>0 ):
			length_sec = 60 * int(length[0]) + int(length[1])
			current_time_sec = (60 * int(current_time[0]) + int(current_time[1]))
			remaining_time = length_sec - current_time_sec
			if(remaining_time ==1):
				driver.close()
				break
