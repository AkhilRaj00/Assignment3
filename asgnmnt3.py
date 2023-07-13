from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()

# Open the Amazon.ca website
driver.get("https://www.amazon.ca")
time.sleep(3)

signin_button = driver.find_element(By.ID, "nav-link-accountList")
signin_button.click()

email_input = driver.find_element(By.ID, "ap_email")
email_input.send_keys("6282569089")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys("230824sa")

signin_submit_button = driver.find_element(By.ID, "signInSubmit")
signin_submit_button.click()

# Wait for the login process to complete
driver.implicitly_wait(10)

search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("Apple iPhone 14 Pro, 128GB, Space Black")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "Apple iPhone 14 Pro, 128GB, Space Black" in driver.title

# Selecting a laptop from the search results
laptop_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[8]/div/div/div/div/div[1]/span/a/div/img")
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
laptop_link.click()



# Waiting for the laptop details page to load
time.sleep(5)

# Adding the laptop to the cart
add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

# Clicking on no thanks button
no_thanks_button= driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/span/a/div/img")
no_thanks_button.click()
time.sleep(2)

proceed_to_checkout= driver.find_element("xpath","/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[3]/div/div[1]/form/span/span/span/input")
proceed_to_checkout.click()
time.sleep(
    2)


# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
