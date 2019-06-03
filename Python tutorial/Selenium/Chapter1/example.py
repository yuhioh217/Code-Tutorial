#!/usr/local/bin/python3
from selenium import webdriver

'''
	Latest version selenium module doesn't support PhantomJS any more.
	Firefox and google chrome now support no header mode, so we can select one of both to use.
'''
def selenium_test():
	# 指定 chromedriver 路徑, 以下為與python檔案同資料夾下的路徑
  path = './chromedriver'
  webDriver = webdriver.Chrome(path)

  # 設定你想要操作的網頁的網址
  test_url = 'http://google.com.tw'
  webDriver.get(test_url)

  # find_element_by_link_text()
  # find_element_by_name()
  # find_element_by_id()
  # find_element_by_tag_name()
  # find_element_by_partial_link_text()
  # find_element_by_css_selector()
  



if __name__ == '__main__':
  # call function
	selenium_test()