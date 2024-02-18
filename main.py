"""
I have performed some basic automation testing in this file on a website cubexo.in

Tests Are as follows: 
1.Valid Email Submission Test
2.Invalid Email Submission Test
3.Contact Button Click Test
4.LinkedIn Button Click Test
5.Support Button Interaction Test
6.Support Form Entry Test
"""

#---------------------------------------------------------------------
# Imports
#---------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
import time


#---------------------------------------------------------------------
# Initialize Chrome Driver
#---------------------------------------------------------------------
def initialize_driver():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

#---------------------------------------------------------------------
# Test Case 1 for valid email
#---------------------------------------------------------------------
def notify_button_test_1():
    driver = initialize_driver()
    # Open the website
    driver.get("https://www.cubexo.io")

    time.sleep(2)  

    notify_button = driver.find_element(By.XPATH,"//button[contains(text(),'Notify me')]")
    notify_button.click()

    time.sleep(2)

    email_clk = driver.find_element(By.CLASS_NAME,"input-group")
    email_clk.click()

    time.sleep(2)

    email_type = driver.find_element(By.ID,"email")

    for i in "akshatv1420@gmail.com":
        email_type.send_keys(i)
    email_type.send_keys(Keys.ENTER)

    time.sleep(5)

    if driver.current_url=="https://formsubmit.co/contact-us@cubexo.io":
        print("Test Passed For Valid Email")
    else:
        print("Test Failed For Valid Email")

    driver.quit()

#---------------------------------------------------------------------
# Test Case 2 for Invalid email
#---------------------------------------------------------------------
def notify_button_test_2():
    driver = initialize_driver()
    driver.get("https://www.cubexo.io")

    time.sleep(2)  

    notify_button = driver.find_element(By.XPATH,"//button[contains(text(),'Notify me')]")
    notify_button.click()

    time.sleep(2)

    email_clk = driver.find_element(By.CLASS_NAME,"input-group")
    email_clk.click()

    time.sleep(2)
    email_type = driver.find_element(By.ID,"email")
    email_type.send_keys("Akshat Verma")
    email_type.send_keys(Keys.ENTER)

    time.sleep(3)

    if driver.current_url=="https://formsubmit.co/contact-us@cubexo.io":
        print("Test Failed For Invalid Email")
    else:
        print("Test Passes For Invalid Email : Dialogue Box Displayed")
    driver.quit()

#---------------------------------------------------------------------
# Test Case 3 Clicking Contact Button
#---------------------------------------------------------------------
def click_contact():
    driver = initialize_driver()
    driver.get("https://www.cubexo.io")

    time.sleep(2)  
    
    contact = driver.find_element(By.XPATH,"//a[contains(text(),'Contact')]")
    contact.click()
    
    time.sleep(3)
    print("Test Passed For Contact Button \n Status: Button Interactable")
    driver.quit()

#---------------------------------------------------------------------
# Test Case 4 for clicking linkedin button
#---------------------------------------------------------------------
def click_linked():
    driver = initialize_driver()
    driver.get("https://www.cubexo.io")
    
    time.sleep(2)

    linkedin = driver.find_element(By.CLASS_NAME,"p-t-b-30")
    lbtn = linkedin.find_element(By.XPATH, "//i[@class='fa fa-linkedin']")
    lbtn.click()

    time.sleep(5)
    print("Test Passed For LinkedIn Button \n Status: Button Interactable")
    driver.quit()

#---------------------------------------------------------------------
# Test Case 5 for clicking support button
#---------------------------------------------------------------------
def support_test_click():
    # Test Case : Button Open Close 
    driver = initialize_driver()
    driver.get("https://www.cubexo.io")
    
    time.sleep(6)

    wait = WebDriverWait(driver, 10)
    support = driver.find_element(By.XPATH, "//div[@class='widget-visible']")
    button = support.find_element(By.XPATH,"//iframe[@title='chat widget']")
    button.click()
    time.sleep(3)
    button.click()

    print("Test Passed For Support Button \n Status: Button Interactable")
    time.sleep(3)
    driver.quit()

#---------------------------------------------------------------------
# Test Case 6 for testing entries in support 
#---------------------------------------------------------------------
def support_test_1(name,email,msg):
    # Test Case : All Field Entry
    driver = initialize_driver()
    driver.get("https://www.cubexo.io")
    
    time.sleep(4)

    wait = WebDriverWait(driver, 10)
    support = driver.find_element(By.XPATH, "//div[@class='widget-visible']")
    button = support.find_element(By.XPATH,"//iframe[@title='chat widget']")
    button.click()

    time.sleep(1)

    dialog = support.find_element(By.XPATH,"//iframe[@class='open']")
    driver.switch_to.frame(dialog)

    namef= driver.find_element(By.XPATH,"//input[@name='name']").send_keys(name)
    emailf= driver.find_element(By.XPATH,"//input[@name='email']").send_keys(email)
    msgf= driver.find_element(By.XPATH,"//textarea[@aria-placeholder='Message']").send_keys(msg)
    submit = driver.find_element(By.XPATH,"//button[@class='tawk-margin-small-top tawk-button-hover width-100 tawk-custom-color tawk-custom-border-color tawk-button']").click()

    time.sleep(2)

    if driver.find_element(By.XPATH, "//p[contains(text(), 'Your message was sent successfully!')]"):
        print("Test Passes For All Field Entries")
    elif driver.find_element(By.XPATH,"//small[@class='tawk-text-red-1 tawk-text-regular-1']"):
        print("Test Success for Empty Field")
    else:
        print("Test Failed For Empty Field")


    time.sleep(6)

    print("Test Passed")

    driver.quit()


#---------------------------------------------------------------------
# Main Execution
#---------------------------------------------------------------------
if __name__ == "__main__":
    
    notify_button_test_1()
    notify_button_test_2()
    click_contact()
    click_linked()
    support_test_click()
    support_test_1("Akshat","akshatv1420@gmail.com","Hello Cubexo")
