import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

@pytest.fixture(scope="function")
def driver():
    """Fixture to initialize and quit the WebDriver"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    driver.quit()

def wait_and_find_element(driver, by, value, timeout=10):
    """Helper function to wait for an element and return it"""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except TimeoutException:
        pytest.fail(f"Element not found: {value}")

def test_airbnb_search_basic(driver):
    """Test basic search functionality"""
    driver.get("https://www.airbnb.com/")
    assert "airbnb" in driver.current_url.lower()

    # Wait for search box and click
    search_box = wait_and_find_element(driver, By.XPATH, "//label[contains(@for,'bigsearch-query-location-input')]")
    search_box.click()

    # Enter location
    location_input = wait_and_find_element(driver, By.ID, "bigsearch-query-location-input")
    location_input.send_keys("Karachi")

    # Select first suggestion dynamically
    try:
        first_suggestion = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(@id, 'bigsearch-query-location-suggestion')]"))
        )
        first_suggestion.click()
    except TimeoutException:
        pytest.fail("Location suggestion did not appear in time")

    # Select check-in and check-out dates
    try:
        check_in_date = wait_and_find_element(driver, By.XPATH, "//td[@aria-label='Choose Monday, April 15, 2024']")
        check_in_date.click()

        check_out_date = wait_and_find_element(driver, By.XPATH, "//td[@aria-label='Choose Saturday, April 20, 2024']")
        check_out_date.click()
    except TimeoutException:
        pytest.fail("Date selection failed")

    # Click search button
    search_button = wait_and_find_element(driver, By.XPATH, "//button[@type='submit']")
    search_button.click()

    # Validate search results
    WebDriverWait(driver, 10).until(EC.url_contains("search"))
    assert "search" in driver.current_url.lower()

def test_search_results_validation(driver):
    """Test search results validation"""
    test_airbnb_search_basic(driver)

    # Verify search results contain the location
    try:
        location_text = wait_and_find_element(driver, By.XPATH, "//div[contains(@class, 'search-header')]//span[contains(text(), 'Karachi')]")
        assert location_text is not None
    except NoSuchElementException:
        pytest.fail("Location not found in search results")

    # Verify that at least one result is displayed
    try:
        results = driver.find_elements(By.XPATH, "//div[@itemprop='itemListElement']")
        assert len(results) > 0, "No search results found"
    except NoSuchElementException:
        pytest.fail("No search results found")
