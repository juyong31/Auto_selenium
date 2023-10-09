from selenium import webdriver

def driver():
  chrome_option = webdriver.ChromeOptions()
  chrome_option.add_argument("--start-maximized") #창을 전체화면으로 설정하는 옵션
  driver = webdriver.Chrome(options=chrome_option)
  return driver