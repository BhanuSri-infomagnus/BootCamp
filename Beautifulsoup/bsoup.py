from bs4 import BeautifulSoup
import requests
from fpdf import FPDF

html_file = requests.get('https://www.infomagnus.com/').text

soup= BeautifulSoup(html_file, 'html.parser')

title= soup.title
print('Title:', title.text)

text_content = ""
for tag in soup.find_all(['title', 'h1', 'h2', 'h3', 'h4', 'p', 'li', 'a', 'div', 'span']):
    text= tag.get_text(strip=True)
    if text:
        text_content += text + ' '
print('Text Content:', text_content)

# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# for line in text_content.split():
#     pdf.multi_cell(0, 10, line)
# pdf.output('infomagnus.pdf')