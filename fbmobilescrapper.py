from selenium import webdriver
import time



driver=webdriver.Chrome()
time.sleep(1)
driver.get('https://touch.facebook.com/')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="m_login_email"]').send_keys('contact@eduwaive.org')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="m_login_password"]').send_keys('contact_123')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="u_0_5"]').click()




time.sleep(5)
driver.get('https://touch.facebook.com/events/593593431111787')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="unit_id_703958566405594"]/div/div[2]/div[2]/a').click()




time.sleep(2)

for t in range(10):
    #driver.get('https://touch.facebook.com/events/593593431111787')
    #driver.find_element_by_xpath('//*[@id="unit_id_703958566405594"]/div/div[2]/div[2]/a').click()
    
	driver.get('https://touch.facebook.com/events/593593431111787/permalink/guests/?filter=others')
	time.sleep(2)
	contents = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div['+str(t+1)+']/div/div[2]/div/h3/a')
   #list.append(t.text)
	contents.click()
	time.sleep(2)
	driver.save_screenshot('test_shot'+str(t)+'.png')
	time.sleep(2)
	message_btn_new_tab= driver.find_element_by_partial_link_text('Message').click()
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="composer_form"]/div[2]/div[3]/div[2]/textarea').send_keys('yoyo')
	time.sleep(2)
	#driver.find_element_by_xpath('//*[@id="u_h_8"]').click()


for t in range(10,20):
    #driver.get('https://touch.facebook.com/events/593593431111787')
    #driver.find_element_by_xpath('//*[@id="unit_id_703958566405594"]/div/div[2]/div[2]/a').click()
    
    driver.get('https://touch.facebook.com/events/593593431111787/permalink/guests/?filter=others')
    time.sleep(2)
    
    driver.find_element_by_xpath('//*[@id="u_0_0"]/a/div/div/div/strong').click()
    time.sleep(1)
    contents = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[3]/div[2]/div[11]/div['+str(t-10+1)+']/div/div[2]/div/h1/a')
    
    
    #list.append(t.text)
    contents.click()
    time.sleep(2)
    driver.save_screenshot('test_shot'+str(t)+'.png')
    time.sleep(1)
    message_btn_new_tab= driver.find_element_by_partial_link_text('Message').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="composer_form"]/div[2]/div[3]/div[2]/textarea').send_keys('yoyo')



