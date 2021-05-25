from selenium import webdriver
import time

def ui_converter(convert_from, convert_to, value):
    try:
        driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.metric-conversions.org/")
        driver.find_element_by_css_selector("#queryFrom").send_keys(convert_from)
        time.sleep(1)
        driver.find_element_by_id("queryTo").send_keys(convert_to)
        time.sleep(1)
        driver.find_element_by_class_name("argument").send_keys(value)
        time.sleep(2)
        driver.find_element_by_xpath("//body/div[1]/section[2]/div[1]/ol[1]/li[1]/div[1]/a[2]").click()
        time.sleep(2)
        return "All ok"
    except Exception("Something going wrong :("):
        return Exception


print(ui_converter("Celsius", "Fahrenheit", 32))
print(ui_converter("Meters", "Feet", 100))
print(ui_converter("Ounces", "Grams", 13))