import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="function")
def driver():
    # Set Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

def test_airbnb_search(driver):
    # Test case 1: Open Airbnb website
    driver.get("https://www.airbnb.com/")
    assert "airbnb" in driver.current_url.lower()
    
    # Wait for page to load
    time.sleep(5)

    # Test case 2: Search location
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='search-tabpanel']/div/div/div/label/div/div"))
    )
    search_box.click()
    time.sleep(2)

    location_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bigsearch-query-location-input"))
    )
    location_input.send_keys("Karachi")
    time.sleep(2)

    # Test case 3: Select location suggestion
    first_suggestion = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "bigsearch-query-location-suggestion-0"))
    )
    first_suggestion.click()
    time.sleep(2)

    # Test case 4: Select dates
    check_in_date = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='panel--tabs--0']/div/div/div[4]/div/div/div/button[34]"))
    )
    check_in_date.click()
    time.sleep(2)

    check_out_date = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='panel--tabs--0']/div/div/div[4]/div/div/div[2]/button[13]"))
    )
    check_out_date.click()
    time.sleep(2)

    # Test case 5: Select guests
    guests_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='search-tabpanel']/div/div[5]/div[2]/div/div/div[2]"))
    )
    guests_button.click()
    time.sleep(2)

    # Test case 6: Modify guest count
    adults_increase = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Ages 13 or above'])[1]/following::*[name()='svg'][2]"))
    )
    adults_increase.click()
    time.sleep(1)

    # Test case 7: Click search button
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='search-tabpanel']/div/div[5]/div[2]/div[3]/button/span/span"))
    )
    search_button.click()
    time.sleep(5)

    # Verify search results
    assert "search" in driver.current_url.lower() 