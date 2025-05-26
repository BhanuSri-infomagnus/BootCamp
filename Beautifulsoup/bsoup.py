from bs4 import BeautifulSoup
import requests
from fpdf import FPDF
from PIL import Image
import os
import io

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

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
for line in text_content.split('\n'):
    pdf.multi_cell(0, 10, line)


for src in soup.find_all('img'):
    image_url = src.get('src')
    if image_url:
        try:
            img_data = requests.get(image_url).content
            img_ext = os.path.splitext(image_url)[-1].lower()
            base_name = src.get('alt') or os.path.splitext(image_url.split('/')[-1])[0]
           
            if img_ext not in ['.jpg', '.jpeg', '.png']:
                img = Image.open(io.BytesIO(img_data)).convert('RGB')
                img_name = f'{base_name}.jpg'
                img.save(img_name, 'JPEG')
            else:
                img_name = f'{base_name}{img_ext if img_ext in [".jpg", ".jpeg", ".png"] else ".jpg"}'
                with open(img_name, 'wb') as handler:
                    handler.write(img_data)
            pdf.add_page()
            pdf.image(img_name, x=10, y=10, w=pdf.w - 20)
            print(f'Downloaded and added to PDF: {img_name}')
            os.remove(img_name)
        except Exception as e:
            print(f'Failed to download or convert {image_url}: {e}')

pdf.output('infomagnus.pdf')
print("✅ PDF saved: infomagnus.pdf")
