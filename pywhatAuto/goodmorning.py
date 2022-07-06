from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options


##Se le dice a selenium que tome los datos del Navegador como las Cookies etc...


options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Lenovo\\AppData\\Local\\Google\\Chrome\\User Data")
website='https://web.whatsapp.com/'
path="..\driver\chromedriver.exe"
head=Options()
head.headless=True

service=Service(executable_path=path)
driver =webdriver.Chrome(service=service,chrome_options=options,options=head)
driver.get(website)
wait=WebDriverWait(driver,100)

harryXPATH='//div[@id="pane-side"]//div[@class="_3OvU8"]//div[@class="zoWT4"]//span[contains(text(),"S A P O")]'

harry_contact=wait.until(EC.visibility_of_element_located((By.XPATH,harryXPATH)))
harry_contact.click()

input_Msg_path = '//div[@class="p3_M1"]//p'

messages=['No te creas we','Estoy automatizando whats','literal','todo lo que te estoy mandando ahorita','no soy yo','es un programa','que hace todo en automatico']

for i in range (100):
    for msg in messages:
        input_Msg = wait.until(
                EC.presence_of_element_located((By.XPATH, input_Msg_path)))
        input_Msg.send_keys("CHUPALOOOOOO"+Keys.ENTER)
        time.sleep(0.1)



