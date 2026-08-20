from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/')
browser.maximize_window()
title =browser.title
print(title)


