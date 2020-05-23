from selenium import webdriver
from docx import Document
from selenium.webdriver.chrome.options import Options 
import os

print(os.path.realpath('./'))

#1. Adding extension
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\ThinkKING\\AppData\\Local\\Google\\Chrome\\User Data")

#C:\Users\ThinkKING\AppData\Local\Google\Chrome\User Data\Default

# create new Chrome driver object with Chrome extension
browser = webdriver.Chrome(options=options)

browser.get("https://nhadieukhacanhtranghuyenthoai.blogspot.com/2015/04/tap-1-chuong-1-su-ra-oi-cua-1-dark-gamer.html")

elem = browser.find_elements_by_css_selector("#Blog1 > div.blog-posts.hfeed > div > div > div > div.post.hentry > h3")
print(elem.text)
#2. Find the section we want to copy and download

#3. Create a doc file if it is not exist

document = Document("The Legendary Moonlight Sculptor.docx")
#4. Copy to that doc file

#5. Save
document.save('The Legendary Moonlight Sculptor.docx')
