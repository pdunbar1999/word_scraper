from selenium import webdriver
import sys
import time

#opens the page in firefox
browser = webdriver.Firefox(executable_path=r'/Users/peterdunbar/Downloads/geckodriver')
browser.get('https://www.thegamegal.com/word-generator/')
file = open('/Users/peterdunbar/Documents/word_list.txt', 'w')
file.close()
time.sleep(2)
return_count = 0

for x in range(0,200):
    browser.find_element_by_id('newword-button').click() #finds word button
    word = browser.find_element_by_id('gennedword').text #grabs text
    file = open('/Users/peterdunbar/Documents/word_list.txt', 'a')
    if return_count % 5 == 0:
        file.write('\n') #new line every 5 words
    return_count += 1
    file.write(str(word) + ',') #writes word to file
    file.close()
    
    
    




