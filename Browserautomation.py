import time
import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# intializing web driver

driver = webdriver.Chrome(executable_path="C:\Driver\ChromeDriver\chromedriver.exe")

# Intialize and maximizing the window
driver.get("http://www.tutorialsninja.com/demo/")
driver.maximize_window()
phone = driver.find_element_by_xpath('//a[text()="Phones & PDAs"]')
phone.click()
iphone = driver.find_element_by_xpath('//a[text()="iPhone"]')
iphone.click()
time.sleep(1)

# first picture
first_pic = driver.find_element_by_xpath('//ul[@class="thumbnails"]/li[1]/a/img')
first_pic.click()
time.sleep(2)

# next picture
next_click = driver.find_element_by_xpath('//button[@title="Next (Right arrow key)"]')

for i in range(0, 5):
    next_click.click()
    time.sleep(2)

# save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')

#close pic
close_pic=driver.find_element_by_class_name("mfp-close")
close_pic.click()

#Adding Quantity
add_qty=driver.find_element_by_id("input-quantity")
add_qty.clear()
add_qty.send_keys(2)

#add to cart
Add_to_cart=driver.find_element_by_id("button-cart")
Add_to_cart.click()
time.sleep(2)

#Adding Laptops
laptops=driver.find_element_by_xpath('//a[text()="Laptops & Notebooks"]')
action=ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(3)
laptops_2=driver.find_element_by_xpath(('//a[text()="Show All Laptops & Notebooks"]'))
laptops_2.click()
time.sleep(1)

#Adding Laptop
HP=driver.find_element_by_xpath("//a[text()='HP LP3065']")
HP.click()

#add to button
add_button=driver.find_element_by_css_selector("#button-cart")
add_button.location_once_scrolled_into_view

#Clicking on calender symbol
calendar=driver.find_element_by_xpath('//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

next_click_calendar=driver.find_element_by_xpath('//th[@class="next"]')
month_year=driver.find_element_by_xpath('//th[@class="picker-switch"]')

#year:2022 month:december
while month_year.text != 'May 2022':
    next_click_calendar.click()
time.sleep(2)

#day 31
calendar_date=driver.find_element_by_xpath('//td[text()="31"]')
calendar_date.click()
time.sleep(2)

#add laptop Quantity to  cart

Qty_2=driver.find_element_by_css_selector("#input-quantity")
Qty_2.clear()
Qty_2.send_keys(1)
add_button.click()


#Clicking on final cart button
cart_total=driver.find_element_by_xpath('//div[@id="cart"]')
#go_to_cart=driver.find_element_by_id('cart-total')
#go_to_cart.click()
#time.sleep(1)
cart_total.click()
#\time.sleep(1)

#Clicking on cheackout button
checkout=driver.find_element_by_xpath('//p[@class="text-right"]/a[2]')
checkout=driver.find_elements_by_link_text("http://tutorialsninja.com/demo/index.php?route=checkout/checkout")
checkout.click()
time.sleep()

#Guest account
guest=driver.find_element_by_xpath('//input[@value="guest"]')
guest.click()

#Clicking on Continue button
continue_button=driver.find_element_by_xpath('//input[@value="Continue"]')
continue_button.click()
time.sleep(1)

#scrolling
step_2=driver.find_element_by_xpath('//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)

#first name
first_name=driver.find_element_by_id('input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('James')
time.sleep(1)

#Last_Name
last_name=driver.find_element_by_name("lastname")
first_name.click()
time.sleep()
last_name.send_keys("Gomes")
time.sleep(1)

#email
email=driver.find_element_by_id('input-payment-email')
email.click()
time.sleep(1)
email.send_keys('james@gmail.com')
time.sleep(1)

#telephone
telephone=driver.find_element_by_id('input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('012345678')
time.sleep(1)

#address
address=driver.find_element_by_id('input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('Delhi 187')
time.sleep(1)

#city
city=driver.find_element_by_id('input-payment-city')
city.click()
time.sleep(1)
city.send_keys('Frankfurt')
time.sleep(1)

#postcode
postcode=driver.find_element_by_id('input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('112233')
time.sleep(1)


#country
country=driver.find_element_by_id('input-payment-country')
dropdown_1=Select(country)
time.sleep(1)
dropdown_1.select_by_visible_text("Germany").click()
time.sleep(1)

#Region
region=driver.find_element_by_name("zone_id")
dropdown_2=Select(region)
time.sleep(1)
dropdown_1.select_by_visible_text("Angus").click()
time.sleep(1)

#continue click of Guest Account
click_continue=driver.find_element_by_xpath('//input[@id="button-guest"]')
click_continue.click()

#click continue 2
continue_3=driver.find_element_by_xpath('//input[@id="button-shipping-method"]')
continue_3.click()
time.sleep(1)

#click continue 4
continue_4=driver.find_element_by_xpath('//input[@id="button-payment-method"]')
continue_4.click()
time.sleep(3)

#click on the confirmation button
confirmation_button=driver.find_element_by_id('button-confirm')
confirmation_button.click()
time.sleep(2)


#success text
success_text=driver.find_element_by_xpath('//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(1)

driver.close()


