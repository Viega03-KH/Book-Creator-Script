from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time, os
from pathlib import Path
from PIL import Image

os.makedirs("screens", exist_ok=True)


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1280,720")


driver = webdriver.Chrome(service=Service(), options=options)
driver.get("https://archive.org/details/vzaimnaiapomoshc00krop/mode/2up?ref=ol&view=theater")

time.sleep(8)  

actions = ActionChains(driver)
total_pages = 578 


for i in range(1, total_pages + 1):
    filename = f"screens/page_{i:03}.png"
    driver.save_screenshot(filename)
    print(f"{i}-sahifa saqlandi: {filename}")

    actions.send_keys(Keys.ARROW_RIGHT).perform()
    time.sleep(2.2)  

driver.quit()


image_dir = Path("screens")
images = list(image_dir.glob("*.png"))
images.sort()

if images:
    image_list = [Image.open(img).convert("RGB") for img in images]
    output_pdf = "ebook.pdf"
    image_list[0].save(output_pdf, save_all=True, append_images=image_list[1:])
    print(f"\n✅ PDF yaratildi: {output_pdf}")
