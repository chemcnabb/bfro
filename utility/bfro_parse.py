import xml.etree.ElementTree as ET
tree = ET.ElementTree(file="doc.xml")

for elem in tree.iter():
    print elem