
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://localhost:8080")

print("Page Title:", driver.title)
print("Heading:", driver.find_element(By.TAG_NAME, "h1").text)

driver.quit()
