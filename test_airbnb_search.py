import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

def wait_and_find_element(driver, by, value, timeout=10):
    """Helper function to wait for and find an element"""
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        pytest.fail(f"Element not found: {value}")

def test_airbnb_search_basic(driver):
    """Test basic search functionality"""
    # Test case 1: Open Airbnb website
    driver.get("https://www.airbnb.com/")
    assert "airbnb" in driver.current_url.lower()
    
    # Wait for page to load
    time.sleep(5)

    # Test case 2: Search location
    search_box = wait_and_find_element(driver, By.XPATH, "//div[@id='search-tabpanel']/div/div/div/label/div/div")
    search_box.click()
    time.sleep(2)

    location_input = wait_and_find_element(driver, By.ID, "bigsearch-query-location-input")
    location_input.send_keys("Karachi")
    time.sleep(2)

    # Test case 3: Select location suggestion
    first_suggestion = wait_and_find_element(driver, By.ID, "bigsearch-query-location-suggestion-0")
    first_suggestion.click()
    time.sleep(2)

    # Test case 4: Select dates
    check_in_date = wait_and_find_element(driver, By.XPATH, "//div[@id='panel--tabs--0']/div/div/div[4]/div/div/div/button[34]")
    check_in_date.click()
    time.sleep(2)

    check_out_date = wait_and_find_element(driver, By.XPATH, "//div[@id='panel--tabs--0']/div/div/div[4]/div/div/div[2]/button[13]")
    check_out_date.click()
    time.sleep(2)

    # Test case 5: Select guests
    guests_button = wait_and_find_element(driver, By.XPATH, "//div[@id='search-tabpanel']/div/div[5]/div[2]/div/div/div[2]")
    guests_button.click()
    time.sleep(2)

    # Test case 6: Modify guest count
    adults_increase = wait_and_find_element(driver, By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Ages 13 or above'])[1]/following::*[name()='svg'][2]")
    adults_increase.click()
    time.sleep(1)

    # Test case 7: Click search button
    search_button = wait_and_find_element(driver, By.XPATH, "//div[@id='search-tabpanel']/div/div[5]/div[2]/div[3]/button/span/span")
    search_button.click()
    time.sleep(5)

    # Verify search results
    assert "search" in driver.current_url.lower()

def test_search_results_validation(driver):
    """Test search results validation"""
    # Perform basic search first
    test_airbnb_search_basic(driver)
    
    # Wait for results to load
    time.sleep(5)
    
    # Verify search parameters are displayed
    try:
        location_text = wait_and_find_element(driver, By.XPATH, "//div[contains(@class, 'search-header')]//span[contains(text(), 'Karachi')]")
        assert location_text is not None
    except NoSuchElementException:
        pytest.fail("Location not found in search results")
    
    # Verify results are displayed
    try:
        results = driver.find_elements(By.XPATH, "//div[@itemprop='itemListElement']")
        assert len(results) > 0, "No search results found"
    except NoSuchElementException:
        pytest.fail("No search results found")

def test_price_filter(driver):
    """Test price range filtering"""
    # Perform basic search first
    test_airbnb_search_basic(driver)
    
    # Wait for results to load
    time.sleep(5)
    
    # Click on price filter
    try:
        price_filter = wait_and_find_element(driver, By.XPATH, "//button[contains(@aria-label, 'Price')]")
        price_filter.click()
        time.sleep(2)
        
        # Set minimum price
        min_price = wait_and_find_element(driver, By.XPATH, "//input[@aria-label='Minimum price']")
        min_price.clear()
        min_price.send_keys("100")
        time.sleep(1)
        
        # Set maximum price
        max_price = wait_and_find_element(driver, By.XPATH, "//input[@aria-label='Maximum price']")
        max_price.clear()
        max_price.send_keys("200")
        time.sleep(1)
        
        # Apply filter
        apply_button = wait_and_find_element(driver, By.XPATH, "//button[contains(text(), 'Apply')]")
        apply_button.click()
        time.sleep(3)
        
        # Verify price filter is applied
        price_text = wait_and_find_element(driver, By.XPATH, "//button[contains(@aria-label, 'Price')]//span[contains(text(), '$100')]")
        assert price_text is not None
    except NoSuchElementException:
        pytest.fail("Price filter not applied successfully")

def test_property_type_filter(driver):
    """Test property type filtering"""
    # Perform basic search first
    test_airbnb_search_basic(driver)
    
    # Wait for results to load
    time.sleep(5)
    
    # Click on property type filter
    try:
        property_filter = wait_and_find_element(driver, By.XPATH, "//button[contains(@aria-label, 'Property type')]")
        property_filter.click()
        time.sleep(2)
        
        # Select "Entire home"
        entire_home = wait_and_find_element(driver, By.XPATH, "//input[@aria-label='Entire home']")
        entire_home.click()
        time.sleep(1)
        
        # Apply filter
        apply_button = wait_and_find_element(driver, By.XPATH, "//button[contains(text(), 'Apply')]")
        apply_button.click()
        time.sleep(3)
        
        # Verify property type filter is applied
        property_text = wait_and_find_element(driver, By.XPATH, "//button[contains(@aria-label, 'Property type')]//span[contains(text(), 'Entire home')]")
        assert property_text is not None
    except NoSuchElementException:
        pytest.fail("Property type filter not applied successfully") 