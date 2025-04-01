from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .test_base import BaseTest

class TestExample(BaseTest):
    def test_google_search(self, setup):
        driver = setup
        
        # Navigate to Google
        driver.get("https://www.google.com")
        
        # Find and fill the search box
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("Selenium with Python")
        search_box.submit()
        
        # Wait for results and verify
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )
        
        # Take screenshot
        driver.save_screenshot("test_results/google_search.png") 