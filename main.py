from selenium import webdriver
import pandas as pd
from time import sleep
from selenium.webdriver.common.keys import Keys
from copy import deepcopy
driver = webdriver.Chrome("./chromedriver.exe")

data = pd.read_csv("Item_Bill_Aishah.csv")

# driver.get("https://www.google.com/search?q=gastrescory")
# x = driver.find_elements_by_class_name("gL9Hy")

# search = driver.find_element_by_class_name("gLFyf")
# search.send_keys("gastrescory")
# search.send_keys(Keys.ENTER)
# x = driver.find_element_by_id("fprsl")

# for i in x:

for i in range (len(data)):
    query = deepcopy(data.loc[i,'Item'])
    driver.get(f"https://www.google.com/search?q={query}")
    sleep(2)
    print(f"Correcting index {i + 1}")
    try:
        x = driver.find_elements_by_class_name("gL9Hy")
        print(x[1].text)
        data.loc[i, 'Corrected Item'] = x[1].text
    except :
        print("No Suggestion")
        data.loc[i, 'Corrected Item']  = query

data.to_csv("result.csv")

