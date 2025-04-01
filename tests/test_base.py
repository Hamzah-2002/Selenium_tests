from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
from datetime import datetime
from dotenv import load_dotenv

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Create test results directory if it doesn't exist
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.results_dir = f"test_results/{timestamp}"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Load environment variables
        load_dotenv()
        
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Initialize the Chrome WebDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        
        yield self.driver
        
        # Teardown
        self.driver.quit()
    
    def take_screenshot(self, name):
        """Helper method to take screenshots with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.results_dir}/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        return filename 