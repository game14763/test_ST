import xml.etree.ElementTree as ET

office = "{urn:oasis:names:tc:opendocument:xmlns:office:1.0}"
text = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"
tree1 = ET.parse('content.xml')
file_odt = tree1.getroot()
tree2 = ET.parse('document.xml')
file_docx = tree2.getroot()

n = 0
for i in file_odt.findall(office+"body"):
    for j in i:
        for k in j.findall(text+"p"):
            if k.text != None:
                #print(k.text)
                n += 1
print("All Indentation: " + str(n))

