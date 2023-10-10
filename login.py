from selenium.webdriver.common.by import By
import os


#비밀번호 암호화
def password_encrypt():
  password_file = "password.txt"
  if os.path.exists(password_file):
    with open(password_file, "r") as file:
      password = file.readline().strip()
      return password
  else:
    raise FileNotFoundError("Password file not found")
  
  

#로그인
def login_excute(driver):
  username = "actyoung31"
  
  password = password_encrypt()

  username_input = driver.find_element(By.NAME, "user_id")
  password_input = driver.find_element(By.NAME, "user_pw")

  username_input.send_keys(username)
  password_input.send_keys(password)

  login_btn = driver.find_element(By.CLASS_NAME, "pjj-h14")
  login_btn.click()