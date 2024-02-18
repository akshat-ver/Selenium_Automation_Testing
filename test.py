"""
In this program I have done automation to a website cubexo.in
The Automated Testing is done in other file named as main.py
"""


#---------------------------------------------------------------------
# Imports
#---------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#---------------------------------------------------------------------
# Initialising the driver
#---------------------------------------------------------------------
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()


#---------------------------------------------------------------------
# Opening the First web page
#---------------------------------------------------------------------

# Search Google
driver.get("https://www.google.com")

time.sleep(2)

google_in = driver.find_element(By.CLASS_NAME,"gLFyf")
google_in.send_keys("cubexo indore",Keys.ENTER)

time.sleep(2)

# Search Cubexo-------------------------------------------------------
link = driver.find_element(By.PARTIAL_LINK_TEXT,"CubexO")
link.click()

time.sleep(2)

contact = driver.find_element(By.XPATH,"//a[contains(text(),'Contact')]")
contact.click()

# Fetches address of office from website-------------------------------
add_div = driver.find_element(By.XPATH, "//div[@class='col-sm-4 col-xs-6 p-t-b-5']")

add_element = add_div.find_element(By.TAG_NAME, "p")
add_text = add_element.text.replace("\n"," ").replace(",","")

time.sleep(1)

# Clicks on notify button---------------------------------------------
notify_button = driver.find_element(By.XPATH,"//button[contains(text(),'Notify me')]")
notify_button.click()

time.sleep(2)

email_clk = driver.find_element(By.CLASS_NAME,"input-group")
email_clk.click()

time.sleep(2)

email_type = driver.find_element(By.ID,"email")
for i in "akshatv1420@gmail.com":
    email_type.send_keys(i)
#email_type.send_keys(Keys.ENTER)

time.sleep(5)


#---------------------------------------------------------------------
# Opens new window and search google map
#---------------------------------------------------------------------

driver.execute_script("window.open('');") 
driver.switch_to.window(driver.window_handles[1]) 
driver.get("https://maps.google.com") 

search = driver.find_element(By.CLASS_NAME,'xiQnY')
print(add_text)
search.send_keys(add_text,Keys.ENTER)

time.sleep(20)
#---------------------------------------------------------------------
# Quits the browser
#---------------------------------------------------------------------

driver.quit()
