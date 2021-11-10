from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

name = "Walace Santos 3"
email = "walace3@test.com"
password = "Test123"

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

# VERIFY SIGNUP
assert driver.find_element(By.ID, "search-courses").is_displayed()
print(r"SIGNUP Completed!")

# CLICK PROFILE PHOTO
driver.find_element(By.XPATH, "//a[@href ='#']").click()

# GO TO LOGOUT
driver.find_element(By.XPATH, "//a[@href ='/sign_out']").click()

# GO TO LOGIN PAGE
driver.find_element(By.XPATH, "//a[@href ='/sign_in']").click()

# TYPE EMAIL
email_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.ID, "email")))
email_field.send_keys(email)

# TYPE PASSWORD
password_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.ID, "password")))
password_field.send_keys(password)

# CLICK LOGIN BUTTON
driver.find_element(By.NAME, "commit").click()

# VERIFY LOGIN
assert driver.find_element(By.ID, "search-courses").is_displayed()
print(r"SUCCESS!!")

driver.close()
