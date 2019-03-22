from flask import Flask
from selenium import webdriver
import time
import facebook
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	driver=webdriver.Chrome(options=chrome_options)


	#driver=webdriver.Chrome()
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
	driver.find_element_by_xpath('//*[@id="unit_id_703958566405594"]/div[1]/a/header').click()




	time.sleep(2)
	names_list = []
	for t in range(10):
	    #driver.get('https://touch.facebook.com/events/593593431111787')
	    #driver.find_element_by_xpath('//*[@id="unit_id_703958566405594"]/div/div[2]/div[2]/a').click()
	    
	    #driver.get('https://touch.facebook.com/events/593593431111787/permalink/guests/?filter=others')
	    #time.sleep(2)
	    
	    aa= driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div['+str(t+1)+']/div/div[2]/div/h3/a').text
	    #print aa
	    names_list.append(aa)
	    
	print names_list





	time.sleep(2)
	url_list = []
	for t in range(10):
	    #driver.get('https://touch.facebook.com/events/593593431111787/permalink/guests/?filter=others')
	    driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div['+str(t+1)+']/div/div[2]/div/h3/a').click()
	    #time.sleep(1)
	    aaa=driver.current_url
	    url_list.append(aaa)
	    driver.back()
	print url_list   





	time.sleep(2)

	driver.find_element_by_partial_link_text('See more').click()

	time.sleep(2)

	for t in range(10,20):
	    #driver.get('https://touch.facebook.com/events/593593431111787')
	    #driver.find_element_by_xpath('//*[@id="unit_id_703958566405594"]/div/div[2]/div[2]/a').click()
	    
	    #driver.get('https://touch.facebook.com/events/593593431111787/permalink/guests/?filter=others')
	    #time.sleep(2)
	    
	    
	  
	    time.sleep(1)
	    ab=driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[3]/div[2]/div[11]/div['+str(t-10+1)+']/div/div[2]/div/h1/a').text
	    names_list.append(ab)
	    
	print names_list  




	time.sleep(2)
	driver.find_element_by_partial_link_text('See more').click()
	for t in range(10,20):
	    
	    #driver.get('https://touch.facebook.com/events/593593431111787/permalink/guests/?filter=others')
	    driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[3]/div[2]/div[11]/div['+str(t-10+1)+']/div/div[2]/div/h1/a').click()
	    #time.sleep(1)      
	    abb=driver.current_url
	    url_list.append(abb)
	    driver.back()
	print url_list   







	json_data2={
	    
	 "member": 
	 {
	     "id": None,
	     "name": None
	 },
	    
	 "source_site": "facebook",
	 
	 "venue":
	 {
	     "city":"Chandigarh",
	     "name":None
	 },
	    
	     "event":
	 {
	     "id": None,
	     "name": None
	 },
	    
	 "response": "yes"
	}




	

	graph = facebook.GraphAPI(access_token="EAAIkodRZBGZC0BALbYiiuVIypgbUzj1QlwTgpoQkxwB7FR8JWlZAkPMoCP03JJFbn2Kycra07cKnJ25mQrdjZBP082VjsWHtnOpFGX4ZAKdXL9ZB86rYpaGpzo12SVKa7t8BdIQDmbJnxD66Q7vao4OLCFYE9w15v3hsuu3t6Vd6ScrBjo2WkoF1pGqzPNcBNB1v7nJ7vkJwZDZD", version="2.12")



	post = graph.get_object(id='593593431111787', fields='id,name,place')
	print(post['id'])
	print(post['name'])
	print(post['place'])
	a = post['id']
	b = post['name']
	c = post['place']


	event = graph.get_object(id='593593431111787',
	                         fields='attending_count,declined_count')
	print(event['attending_count'])
	print(event['declined_count'])



	
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/aviraj/Downloads/eduwaivecommon-be26acf05dc1.json"


	from google.cloud import pubsub_v1


	publish_client = pubsub_v1.PublisherClient()

	topic = 'projects/eduwaivecommon/topics/event_subscribers'

	for t in range(20):
	    json_data2['member']['name'] = names_list[t]
	    json_data2['venue']['name'] = c
	    json_data2['event']['id'] = a
	    json_data2['event']['name']= b
	    json_data2['member']['id']=url_list[t]
	    print(json_data2)
	    data = json.dumps(json_data2).encode('utf-8')
	    publish_client.publish(topic,data=data)
	#print json_data




	return "Event attendees data pushed to pubsub queue, Cheers!"

if __name__ == '__main__':
    app.run(debug=True)
    