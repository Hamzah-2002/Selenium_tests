from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .test_base import BaseTest
import pytest
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TestAmazon(BaseTest):
    def test_amazon_homepage(self, setup):
        driver = setup
        logger.info("Starting Amazon homepage test")
        
        try:
            # Navigate to Amazon
            driver.get("https://www.amazon.com")
            logger.info("Navigated to Amazon homepage")
            
            # Verify Amazon logo is present
            logo = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "nav-logo-sprites"))
            )
            assert logo.is_displayed()
            logger.info("Amazon logo verified")
            
            # Take screenshot
            screenshot_path = self.take_screenshot("amazon_homepage")
            logger.info(f"Screenshot saved: {screenshot_path}")
            
        except TimeoutException:
            logger.error("Timeout while loading Amazon homepage")
            raise
        except Exception as e:
            logger.error(f"Error in test_amazon_homepage: {str(e)}")
            raise

    def test_search_product(self, setup):
        driver = setup
        logger.info("Starting product search test")
        
        try:
            # Navigate to Amazon
            driver.get("https://www.amazon.com")
            
            # Find and fill the search box
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            search_box.send_keys("laptop")
            search_box.send_keys(Keys.RETURN)
            logger.info("Searched for 'laptop'")
            
            # Wait for search results
            results = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-result-item"))
            )
            assert results.is_displayed()
            logger.info("Search results verified")
            
            # Take screenshot
            screenshot_path = self.take_screenshot("amazon_search_results")
            logger.info(f"Screenshot saved: {screenshot_path}")
            
        except TimeoutException:
            logger.error("Timeout while searching for product")
            raise
        except Exception as e:
            logger.error(f"Error in test_search_product: {str(e)}")
            raise

    def test_add_to_cart(self, setup):
        driver = setup
        logger.info("Starting add to cart test")
        
        try:
            # Navigate to Amazon
            driver.get("https://www.amazon.com")
            
            # Search for a product
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            search_box.send_keys("headphones")
            search_box.send_keys(Keys.RETURN)
            logger.info("Searched for 'headphones'")
            
            # Click on the first product
            first_product = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.s-result-item h2 a"))
            )
            first_product.click()
            logger.info("Selected first product")
            
            # Switch to the new window
            driver.switch_to.window(driver.window_handles[-1])
            
            # Wait for and click the "Add to Cart" button
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
            )
            add_to_cart_button.click()
            logger.info("Clicked add to cart button")
            
            # Wait for the confirmation message
            confirmation = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "huc-v2-order-row-confirm-text"))
            )
            assert "Added to Cart" in confirmation.text
            logger.info("Add to cart confirmation verified")
            
            # Take screenshot
            screenshot_path = self.take_screenshot("amazon_add_to_cart")
            logger.info(f"Screenshot saved: {screenshot_path}")
            
        except TimeoutException:
            logger.error("Timeout while adding product to cart")
            raise
        except Exception as e:
            logger.error(f"Error in test_add_to_cart: {str(e)}")
            raise

    def test_sign_in_button(self, setup):
        driver = setup
        logger.info("Starting sign in button test")
        
        try:
            # Navigate to Amazon
            driver.get("https://www.amazon.com")
            
            # Find and click the sign-in button
            sign_in_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "nav-link-accountList"))
            )
            sign_in_button.click()
            logger.info("Clicked sign in button")
            
            # Verify we're on the sign-in page
            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "ap_email"))
            )
            assert email_input.is_displayed()
            logger.info("Sign in page verified")
            
            # Take screenshot
            screenshot_path = self.take_screenshot("amazon_sign_in")
            logger.info(f"Screenshot saved: {screenshot_path}")
            
        except TimeoutException:
            logger.error("Timeout while accessing sign in page")
            raise
        except Exception as e:
            logger.error(f"Error in test_sign_in_button: {str(e)}")
            raise

    def test_department_navigation(self, setup):
        driver = setup
        logger.info("Starting department navigation test")
        
        try:
            # Navigate to Amazon
            driver.get("https://www.amazon.com")
            
            # Find and click the "All" menu button
            all_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "nav-hamburger-menu"))
            )
            all_menu.click()
            logger.info("Clicked department menu button")
            
            # Wait for the menu to expand and verify it's visible
            menu_items = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "hmenu-content"))
            )
            assert menu_items.is_displayed()
            logger.info("Department menu verified")
            
            # Take screenshot
            screenshot_path = self.take_screenshot("amazon_department_menu")
            logger.info(f"Screenshot saved: {screenshot_path}")
            
        except TimeoutException:
            logger.error("Timeout while accessing department menu")
            raise
        except Exception as e:
            logger.error(f"Error in test_department_navigation: {str(e)}")
            raise 