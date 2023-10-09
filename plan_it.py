from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import check

# 발주계획(IT) 페이지 체크박스 검색수행
def plan(driver):
  # 발주계획(IT)페이지 이동
  request_order_tab = driver.find_element(By.PARTIAL_LINK_TEXT, "요청·발주계획")

  actions = ActionChains(driver)
  actions.move_to_element(request_order_tab).perform() # 요청·발주계획 탭 위로 마우스를 이동

  it_order_tab = driver.find_element(By.PARTIAL_LINK_TEXT, "발주계획 (IT분야)")
  it_order_tab.click() # "발주계획 (IT분야)" 탭을 찾아서 클릭

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
              check.check_and_go_back(driver) # 검색결과를 정상출력 했는지 확인