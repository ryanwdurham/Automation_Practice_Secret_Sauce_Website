from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ============================================================
# BROWSER SELECTION - CHANGE THIS TO TEST DIFFERENT BROWSERS
# ============================================================
BROWSER = "edge"  # Options: "chrome", "edge", "firefox", "safari"


# ============================================================

# Helper function to type text character by character (human-like typing)
def human_type(element, text, delay=0.1):
    """Types text character by character with a delay between each character"""
    for character in text:
        element.send_keys(character)
        time.sleep(delay)


# Helper function to highlight elements with a colored border
def highlight_element(driver, element, color="blue", duration=1):
    """Highlights an element with a colored border"""
    original_style = element.get_attribute('style')
    driver.execute_script(
        f"arguments[0].setAttribute('style', arguments[1] + 'border: 3px solid {color}; box-shadow: 0 0 10px {color};');",
        element, original_style
    )
    time.sleep(duration)
    driver.execute_script(
        f"arguments[0].setAttribute('style', arguments[1]);",
        element, original_style
    )


# Initialize browser driver based on selection
def initialize_browser(browser_name):
    """Initialize the selected browser with appropriate options"""
    browser_name = browser_name.lower()

    if browser_name == "chrome":
        print("🌐 Initializing Google Chrome...")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False
        })
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "edge":
        print("🌐 Initializing Microsoft Edge...")
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False
        })
        edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        driver = webdriver.Edge(options=edge_options)

    elif browser_name == "firefox":
        print("🌐 Initializing Mozilla Firefox...")
        firefox_options = webdriver.FirefoxOptions()
        # Firefox doesn't have the same password manager issues
        driver = webdriver.Firefox(options=firefox_options)

    elif browser_name == "safari":
        print("🌐 Initializing Safari...")
        # Safari requires enabling "Allow Remote Automation" in Develop menu
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}. Choose from: chrome, edge, firefox, safari")

    driver.maximize_window()
    return driver


# Initialize the selected browser
print(f"\n>>> Selected Browser: {BROWSER.upper()} <<<\n")
driver = initialize_browser(BROWSER)

try:
    print("=" * 60)
    print(f"   SAUCEDEMO AUTOMATION - PROFESSIONAL DEMO MODE")
    print(f"   Browser: {BROWSER.upper()}")
    print("=" * 60)

    # Navigate to the website
    print("\n[1/15] Navigating to SauceDemo...")
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Wait for page to load
    wait = WebDriverWait(driver, 15)

    # Login
    print("[2/15] Logging in...")
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    # Highlight and type username
    highlight_element(driver, username_field, "green", 0.8)
    human_type(username_field, "standard_user", 0.08)
    time.sleep(0.5)

    # Highlight and type password
    highlight_element(driver, password_field, "green", 0.8)
    human_type(password_field, "secret_sauce", 0.08)
    time.sleep(0.5)

    # Highlight and click login button
    highlight_element(driver, login_button, "gold", 0.8)
    login_button.click()
    time.sleep(3)

    print("    ✓ Login successful - Page title:", driver.title)

    # Wait for products page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    time.sleep(1.5)

    # Click on Sauce Labs Backpack
    print("[3/15] Clicking on Sauce Labs Backpack...")
    backpack = wait.until(EC.element_to_be_clickable((By.ID, "item_4_title_link")))

    # Find the parent inventory item container for better highlighting
    backpack_container = backpack.find_element(By.XPATH, "./ancestor::div[@class='inventory_item_description']")

    # Hover over the element to trigger the green effect
    driver.execute_script("arguments[0].scrollIntoView(true);", backpack)
    driver.execute_script(
        "var event = new MouseEvent('mouseover', {bubbles: true}); arguments[0].dispatchEvent(event);", backpack)

    highlight_element(driver, backpack_container, "blue", 1)
    backpack.click()
    time.sleep(2.5)
    print("    ✓ Backpack product page opened")

    # Add backpack to cart
    print("[4/15] Adding Backpack to cart...")
    add_to_cart_backpack = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart")))
    highlight_element(driver, add_to_cart_backpack, "green", 1)
    add_to_cart_backpack.click()
    time.sleep(2.5)
    print("    ✓ Backpack added to cart")

    # Go back to products page
    print("[5/15] Returning to products page...")
    back_button = wait.until(EC.element_to_be_clickable((By.ID, "back-to-products")))
    highlight_element(driver, back_button, "orange", 1)
    back_button.click()
    time.sleep(2.5)
    print("    ✓ Back on products page")

    # Click on Sauce Labs Fleece Jacket
    print("[6/15] Clicking on Sauce Labs Fleece Jacket...")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    fleece_jacket = wait.until(EC.element_to_be_clickable((By.ID, "item_5_title_link")))

    # Find the parent inventory item container for better highlighting
    jacket_container = fleece_jacket.find_element(By.XPATH, "./ancestor::div[@class='inventory_item_description']")

    # Hover over the element to trigger the green effect
    driver.execute_script("arguments[0].scrollIntoView(true);", fleece_jacket)
    driver.execute_script(
        "var event = new MouseEvent('mouseover', {bubbles: true}); arguments[0].dispatchEvent(event);", fleece_jacket)

    highlight_element(driver, jacket_container, "blue", 1)
    fleece_jacket.click()
    time.sleep(2.5)
    print("    ✓ Fleece Jacket product page opened")

    # Add fleece jacket to cart
    print("[7/15] Adding Fleece Jacket to cart...")
    add_to_cart_jacket = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart")))
    highlight_element(driver, add_to_cart_jacket, "green", 1)
    add_to_cart_jacket.click()
    time.sleep(2.5)
    print("    ✓ Fleece Jacket added to cart")

    # Click cart button in upper right
    print("[8/15] Navigating to shopping cart...")
    cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    highlight_element(driver, cart_button, "purple", 1)
    cart_button.click()
    time.sleep(2.5)
    print("    ✓ Shopping cart opened")

    # Click checkout button
    print("[9/15] Proceeding to checkout...")
    checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    highlight_element(driver, checkout_button, "gold", 1)
    checkout_button.click()
    time.sleep(2.5)
    print("    ✓ Checkout page loaded")

    # Fill in checkout information
    print("[10/15] Filling in checkout information...")
    first_name = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    last_name = driver.find_element(By.ID, "last-name")
    zip_code = driver.find_element(By.ID, "postal-code")

    # Highlight and type first name
    highlight_element(driver, first_name, "green", 0.8)
    human_type(first_name, "Bryan", 0.1)
    time.sleep(0.8)

    # Highlight and type last name
    highlight_element(driver, last_name, "green", 0.8)
    human_type(last_name, "Green", 0.1)
    time.sleep(0.8)

    # Highlight and type zip code
    highlight_element(driver, zip_code, "green", 0.8)
    human_type(zip_code, "90210", 0.1)
    time.sleep(1.2)
    print("    ✓ Information entered: Bryan Green, 98012")

    # Click continue button
    print("[11/15] Clicking continue...")
    continue_button = driver.find_element(By.ID, "continue")
    highlight_element(driver, continue_button, "gold", 1)
    continue_button.click()
    time.sleep(2.5)
    print("    ✓ Moved to checkout overview")

    # Click finish button on overview page
    print("[12/15] Clicking finish to complete order...")
    finish_button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    highlight_element(driver, finish_button, "gold", 1.2)
    finish_button.click()
    time.sleep(3)
    print("    ✓ Order completed!")

    # Wait for complete page and click back home
    print("[13/15] Returning to home page...")
    back_home_button = wait.until(EC.element_to_be_clickable((By.ID, "back-to-products")))
    highlight_element(driver, back_home_button, "orange", 1)
    back_home_button.click()
    time.sleep(2.5)
    print("    ✓ Back on products page")

    # Wait for products page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    # Stay on products page for 5 seconds
    print("[14/15] Staying on products page for 5 seconds...")
    for i in range(5, 0, -1):
        print(f"    {i} seconds remaining...")
        time.sleep(1)

    print("[15/15] Demo complete! Closing browser...")
    time.sleep(2)

    print("\n" + "=" * 60)
    print("   AUTOMATION COMPLETED SUCCESSFULLY!")
    print("=" * 60)

except Exception as e:
    print(f"\n❌ ERROR OCCURRED: {e}")
    print("Waiting 5 seconds before closing...")
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
    print("\n✓ Browser closed - Demo finished")