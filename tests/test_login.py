# tests/test_login.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_sucesso():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)  # Espera para visualização
    assert "inventory" in driver.current_url

    # Salvar evidência
    driver.save_screenshot("reports/login_sucesso.png")

    driver.quit()
