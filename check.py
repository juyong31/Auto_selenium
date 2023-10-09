from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import capture_save

# 정상출력여부 확인
def check_and_go_back(driver):
  keyword = "검색하신 자료는 존재하지 않습니다. 검색조건을 확인해 보시기 바랍니다."

  try:
    # 첫 번째 조건 평가
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'"+keyword+"')]"))
    )
  except:
    try:
      # 두 번째 조건 평가
      WebDriverWait(driver).until(
          EC.presence_of_element_located((By.XPATH, "/html/body/center/table[1]/tbody/tr/td[1]/span"))
      )
    except:
      capture_save.capture_and_save()
      driver.back()