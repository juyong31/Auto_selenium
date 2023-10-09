from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import capture_save
from PIL import ImageGrab #이미지 캡쳐


# 크롬 브라우저를 실행하고 웹 페이지로 이동
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized") #창을 전체화면으로 설정하는 옵션
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.g2bplus.kr/member_pclogin.php")

#로그인
username = "actyoung31"
password = "^Hi69lA!" #임시비밀번호

username_input = driver.find_element(By.NAME, "user_id")
password_input = driver.find_element(By.NAME, "user_pw")

username_input.send_keys(username)
password_input.send_keys(password)

login_btn = driver.find_element(By.CSS_SELECTOR, "[value='로그인 (SIGN IN)']")
login_btn.click()


  
  # 검색결과가 나타나지 않았을 경우 capture후, driver.back() 하기위한 함수
def check_and_go_back():
  try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/center/table[1]/tbody/tr/td[1]/span")))
  except:
    # 캡쳐 후 저장폴더에 저장
    capture_save.capture_and_save()
    driver.back()
    
    
# 발주계획(IT)페이지 이동
request_order_tab = driver.find_element(By.PARTIAL_LINK_TEXT, "요청·발주계획")

actions = ActionChains(driver)
actions.move_to_element(request_order_tab).perform() # 요청·발주계획 탭 위로 마우스를 이동

it_order_tab = driver.find_element(By.PARTIAL_LINK_TEXT, "발주계획 (IT분야)")
it_order_tab.click() # "발주계획 (IT분야)" 탭을 찾아서 클릭
"""
reqPage_url = "https://www.g2bplus.kr/orderplan_search.php?bsnsDiv=ITALL"
driver.get(reqPage_url)
이 방법도 가능
"""

for _ in range(2):
  itAll_checkbox = driver.find_element(By.NAME, "check_it")
  itAll_checkbox.click()
  for _ in range(2):
    itDev_checkbox = driver.find_element(By.NAME, "check_app")
    itDev_checkbox.click()
    for _ in range(2):
      itMaintain_checkbox = driver.find_element(By.NAME, "check_maintain")
      itMaintain_checkbox.click()
      for _ in range(2):
        itInfra_checkbox = driver.find_element(By.NAME, "check_infra")
        itInfra_checkbox.click()
        for _ in range(2):
          itHid_checkbox = driver.find_element(By.NAME, "check_hidden")
          itHid_checkbox.click()
          for _ in range(2):
            comment_checkbox = driver.find_element(By.NAME, "check_comment")          
            search_button = driver.find_element(By.CSS_SELECTOR, "[type = 'SUBMIT']")
            comment_checkbox.click()
            search_button.click()
            check_and_go_back() # 검색결과를 정상출력 했는지 확인