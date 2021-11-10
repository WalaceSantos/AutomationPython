from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

name = "Walace Santos"
email = "takehome@test.com"
password = "Teachable"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://takehome.zeachable.com/")

# GO TO SIGNUP PAGE
driver.find_element(By.ID, "header-sign-up-btn").click()

# TYPE NAME
name_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.ID, "user_name")))
name_field.send_keys(name)

# TYPE EMAIL
email_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.ID, "user_email")))
email_field.send_keys(email)

# TYPE PASSWORD
password_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.ID, "password")))
password_field.send_keys(password)

# CLICK SIGNUP BUTTON
driver.find_element(By.NAME, "commit").click()

# GET ERROR MESSAGE
message = driver.find_element(By.XPATH, "/html/body/main/div/div").text
print(message)

# VALIDATE MESSAGE
if message == "Email is already in use. Please log in to your account.":
    print(r"SUCCESS!!")
else:
    print(r"FAILLED!!")

driver.close()
