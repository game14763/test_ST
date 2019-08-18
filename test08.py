import xml.etree.ElementTree as ET
from zipfile import ZipFile
from shutil import copyfile
import os

office = "{urn:oasis:names:tc:opendocument:xmlns:office:1.0}"
text = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"
tree1 = ET.parse('read/content.xml')
file_odt = tree1.getroot()
tree2 = ET.parse('read/document.xml')
file_docx = tree2.getroot()



n = 0
m = 1
for i in file_odt.findall(office + "body"):
    for j in i:
        all_p = 0
        for k in j.findall(text + "p"):
            all_p += 1
            if k.text is not None:
                print(k.text)
                n += 1
            # Use elif because if it is None  it will pass here instead
            elif k.findall(text + "a") != []:
                print("News Rank: " + str(m) + "   " + "Paragraph Count: " + str(n))
                r = ET.Element(text + "p")
                r.text = "News Rank: " + str(m) + "    " + "Paragraph Count: " + str(n)
                r.set(text + "style-name", "Standard")
                j.insert(all_p, r)
                all_p += 1
                n = 0
                m += 1

print("All news count is " + str(m-1))
tree1.write("content.xml")
copyfile('read/test-odt.zip', 'test-odt.zip')

with ZipFile('test-odt.zip', 'a') as zf:
    zf.write("content.xml")
os.rename('test-odt.zip', 'test-odt.docx')
