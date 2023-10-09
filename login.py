from selenium.webdriver.common.by import By

#로그인
def login_excute(driver):
  username = "actyoung31"
  password = "^Hi69lA!" #임시비밀번호

  username_input = driver.find_element(By.NAME, "user_id")
  password_input = driver.find_element(By.NAME, "user_pw")

  username_input.send_keys(username)
  password_input.send_keys(password)

  login_btn = driver.find_element(By.CLASS_NAME, "pjj-h14")
  login_btn.click()