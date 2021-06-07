from selenium import webdriver

chrome_driver_path = "/Users/nathanj/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

list_of_urls = [
    {"url": "https://www.amazon.com/Ethernet-Development-ARDUINO-ETHERNET-SHIELD/dp/B011PCMMM0",
     "lowest_price": 25,
     "name": "Arduino Ethernet Shield"}]
for group in list_of_urls:
    driver.get(group["url"])

    price = driver.find_element_by_id("price_inside_buybox")

    if float(price.text.replace("$", "")) < group["lowest_price"]:
        print(f"{group['name']}'s price is less than your lowest price, ${group['lowest_price']}.")

driver.quit()
