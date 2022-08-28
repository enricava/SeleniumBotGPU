#PATH -- D:\Documents\BOT\chromedriver_win32

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import winsound         # for sound  
from colorama import init
from yaggi import avisame

init()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


PATH = "D:/Documents/BOT/chromedriver_win32/chromedriver.exe"

links = [
        ("3060 Ti Asus Tuf","https://www.neobyte.es/tarjeta-grafica-asus-tuf-rtx-3060-ti-8gb-gaming-7916.html", "NeoByte"),
        ("3060 Ti Asus Tuf Oc","https://www.neobyte.es/tarjeta-grafica-asus-tuf-rtx-3060-ti-oc-8gb-gaming-7912.html", "NeoByte"),
        ("3060 Ti Asus Dual","https://www.neobyte.es/tarjeta-grafica-asus-dual-rtx3060ti-8gb-7914.html", "NeoByte"),
        ("3060 Ti Asus Dual Mini Oc","https://www.neobyte.es/tarjeta-grafica-asus-dual-rtx3060ti-mini-oc-8gb-8469.html", "NeoByte"),
        ("3060 Ti Asus Dual Oc","https://www.neobyte.es/tarjeta-grafica-asus-dual-rtx-3060-ti-oc-8gb-7913.html", "NeoByte"),
        ("3060 Ti Gigabyte OC","https://www.neobyte.es/tarjeta-grafica-gigabyte-rtx-3060ti-gaming-oc-8gb-7917.html", "NeoByte"),
        ("3060 Ti Gigabyte Eagle","https://www.neobyte.es/aorus-geforce-rtx-3060-ti-eagle-8gb-7897.html", "NeoByte"),
        ("3060 Ti Gigabyte Vision","https://www.neobyte.es/tarjeta-grafica-gigabyte-rtx-3060ti-vision-8gb-8439.html", "NeoByte"),
        ("3060 Ti Asus Rog Strix","https://www.neobyte.es/tarjeta-grafica-asus-rog-strix-rtx-3060-ti-8gb-gaming-7915.html", "NeoByte"),
        ("3060 Ti Asus Rog Strix OC","https://www.neobyte.es/tarjeta-grafica-asus-rog-strix-rtx-3060-ti-oc-8gb-gaming-7911.html", "NeoByte"),
        ("3060 Ti Zotac Twin Edge","https://www.pccomponentes.com/zotac-geforce-rtx-3060-ti-d6-twin-edge-8gb-gddr6", "PcComps"),
        ("3060 Ti Zotac Twin Edge OC","https://www.pccomponentes.com/zotac-geforce-rtx-3060ti-d6-twin-edge-oc-8gb-gddr6", "PcComps"),
        ("3060 Ti Msi Gaming X","https://www.pccomponentes.com/msi-geforce-rtx-3060-ti-gaming-x-8gb-gddr6", "PcComps"),
        ("3060 Ti Gigabyte OC","https://www.pccomponentes.com/gigabyte-geforce-rtx-3060-ti-gaming-oc-8gb-gddr6", "PcComps"),
        ("3060 Ti Gigabyte OC Pro","https://www.pccomponentes.com/gigabyte-geforce-rtx-3060-ti-gaming-oc-pro-8gb-gddr6", "PcComps"),
        ("3060 Ti Gigabyte Eagle","https://www.pccomponentes.com/gigabyte-geforce-rtx-3060-ti-eagle-8gb-gddr6", "PcComps"),
        ("3060 Ti Gigabyte Aorus Master","https://www.pccomponentes.com/gigabyte-aorus-geforce-rtx-3060-ti-master-8gb-gddr6", "PcComps"),
        ("3060 Ti Msi Ventus 2X OC","https://www.coolmod.com/msi-geforce-rtx-3060-ti-ventus-2x-oc-8gb-gddr6-tarjeta-grafica-precio", "CoolMod"),
        ("3060 Ti Msi Ventus 3X OC","https://www.coolmod.com/msi-geforce-rtx-3060-ti-ventus-3x-oc-8gb-gddr6-tarjeta-grafica-precio", "CoolMod"),
        ("3060 Ti Asus ROG","https://www.coolmod.com/asus-rog-strix-geforce-rtx-3060-ti-gaming-8gb-gddr6-tarjeta-grafica-precio", "CoolMod"),
        ("3060 Ti Asus Dual Mini Oc","https://www.coolmod.com/asus-dual-rtx-3060-ti-mini-oc-8gb-gddr6-tarjeta-grafica-precio", "CoolMod")
         ]

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

#quitar imagenes
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)

while True:
    for x in links:
        try:
            driver.get(x[1])
        except:
            print(time.asctime() + bcolors.WARNING + " [" + x[0] + " - " + x[2]  + " - ] : NOT FOUND" + bcolors.ENDC)
            continue
        stck = True
        try:
            price = 0
            if x[2] == "PcComps":
                search = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, "priceBlock")))
                price = search.text.splitlines()[0][:-1].replace(',','.')
                search = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "action-bar-movil")))
            elif x[2] == "NeoByte":
                search = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, "our_price_display")))
                price = search.text.strip().strip('€').strip('.').replace(',','.')
                search = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "availability_value")))
                stck = search.text != "No disponible"
            elif x[2] == "CoolMod":
                search = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "text-price-total")))
                price = search.text
                search = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "product-availability")))
                stck = (search.text.strip() != "Agotado" and search.text.strip() != "Sin Stock")
        except TimeoutException:
            stck = False
            
        t = time.asctime()

        if stck:
            print(t + bcolors.OKGREEN + " [" + x[0] + " - " + x[2] + " - " + str(price) + "€] : IN STOCK" + bcolors.ENDC)
            for i in range (0,3): winsound.Beep(600, 300) # frequency, duration
            avisame(x[0], x[1], price)
        else:
            print(t + bcolors.WARNING + " [" + x[0] + " - " + x[2]  + " - " + str(price) + "€] : OUT OF STOCK" + bcolors.ENDC)
    print("Cooldown 40s")
    time.sleep(40)


#print(driver.page_source)


#search.send_keys("test")
#search.send_keys(Keys.RETURN)
