import xml.etree.ElementTree as ET

tree = ET.parse("../CSV/library.xml")
root = tree.getroot()

print("Total Books:", len(root.findall("book")))

print("\nBooks written after 2020:")
for book in root.findall("book"):
    if int(book.find("year").text) > 2020:
        print(book.find("title").text)

print("\nBooks costing more than ₹500:")
for book in root.findall("book"):
    if float(book.find("price").text) > 500:
        print(book.find("title").text)