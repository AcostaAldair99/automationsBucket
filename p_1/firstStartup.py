from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd 

website='https://listado.mercadolibre.com.mx/tables'
path="..\driver\chromedriver.exe"


service=Service(executable_path=path)
driver =webdriver.Chrome(service=service)
driver.get(website)


##GET ALL THE ELEMENTS IN THE PAGE, ALL LIST ITEMS
containers=driver.find_elements(by="xpath",value='(//ol)[2]//li')

titles=[]
prices=[]
imgs=[]

for item in containers:
    title=item.find_element(by='xpath',value='//h2').text
    price=item.find_element(by="xpath",value='//div[@class="ui-search-price__second-line"]//span[@class="price-tag-fraction"]').text
    img=item.find_element(by="xpath",value='//img').get_attribute("width")
    prices.append(price)
    titles.append(title)
    imgs.append(imgs)

my_data={'Articulo':titles,'Precios':prices,'Altura de Imagen':imgs}

df_productos=pd.DataFrame(my_data)

df_productos.to_csv("Productos_de_Mercado.csv")


driver.quit()





