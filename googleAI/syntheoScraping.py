from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Selenium WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://suno.com/me")


# Wait for the sign-in button to be clickable and click it
sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > div > div > div > div.cl-main.🔒️.cl-internal-xk295g > div > button.cl-socialButtonsIconButton.cl-socialButtonsIconButton__google.🔒️.cl-internal-855i1h"))
    )
sign_in_button.click()

# Wait for the username field to be visible and enter the username
username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#identifierId"))
    )
username_field.send_keys("asfasfasfgasdfasgfsag@gmail.com")

# Find the next button and click it
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"))
)
next_button.click()

# Find the password field and enter the password
password_field = driver.find_element(By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
password_field.send_keys("applebottom")

# Find the password button and click it
password_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#passwordNext > div > button > div.VfPpkd-RLmnJb"))
    )
password_button.click()

# Find the continue button and click it
continue_button = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div.JYXaTc.F8PBrb > div > div > div:nth-child(2) > div > div > button > div.VfPpkd-RLmnJb"))
    )
continue_button.click()

# Wait for the page to load after signing in
WebDriverWait(driver, 10).until(
        EC.url_contains("https://suno.com/me")
    )

print("Successfully signed in!")

driver.quit()