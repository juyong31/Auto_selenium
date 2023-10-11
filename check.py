from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import capture_save

# 정상출력여부 확인
def check_and_go_back(driver):
  try:
    wait = WebDriverWait(driver, 5)
    wait.until(lambda driver: driver.find_elements(By.XPATH,"/html/body/center/table[2]/tbody/tr[1]/td[1]") or driver.find_elements(By.XPATH,"/html/body/center/font"))
  except:
    capture_save.capture_and_save()
    driver.back()