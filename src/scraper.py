from selenium import webdriver
from selenium.webdriver.common.by import By

def getProductDetails(url):
    """
    Expects product details url and returns product info as dictionary.
    
    Parameters:
    url (str): The URL of the product.

    Returns:
    dict: A dictionary containing product info (name, price, image).
    """
    product_info = {}
    with webdriver.Chrome() as driver:
        driver.get(url)
        try:
            name = driver.find_element(by = By.CLASS_NAME, value = "target_product_name")
            price = driver.find_element(by = By.CLASS_NAME, value = "pdp_price__now")
            image = driver.find_element(by = By.CLASS_NAME, value = "zoom-ico-image")

            product_info["name"] = name.text
            product_info["price"] = price.text
            product_info["image"] = image.get_attribute("href")
        except Exception as e:
            print(f"An error occurred: {e}")
    return product_info

while True:
    URL = input("Enter product URL or 'q' to quit: ")
    if URL.lower() == "q":
        break
    product_info = getProductDetails(URL)
    print(product_info)



