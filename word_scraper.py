from selenium import webdriver
import sys
import time

browser = webdriver.Firefox(executable_path=r'/Users/peterdunbar/Downloads/geckodriver')
browser.get('https://www.thegamegal.com/word-generator/')
file = open('/Users/peterdunbar/Documents/word_list.txt', 'w')
file.close()
time.sleep(2)
return_count = 0

for x in range(0,200):
    browser.find_element_by_id('newword-button').click()
    word = browser.find_element_by_id('gennedword').text
    file = open('/Users/peterdunbar/Documents/word_list.txt', 'a')
    if return_count % 5 == 0:
        file.write('\n')
    return_count += 1
    file.write(str(word) + ',')
    file.close()
    
    
    




