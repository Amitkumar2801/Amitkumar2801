import xml.etree.ElementTree as ET
import json

def main():
    tree = ET.parse('counter.svg')
    root = tree.getroot()
    
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    images = root.findall('.//svg:image', namespaces) or root.findall('.//image')
    
    digit_images = {}
    for img in images:
        img_id = img.get('id')
        href = img.get('href')
        if img_id == 'image-0':
            digit_images[0] = href
        elif img_id == 'image-1':
            digit_images[1] = href
        elif img_id == 'image-2':
            digit_images[2] = href
        elif img_id == 'image-3':
            digit_images[3] = href
        elif img_id == 'image-4':
            digit_images[4] = href
        elif img_id == 'image-5':
            digit_images[5] = href
        elif img_id == 'image-6':
            digit_images[6] = href
        elif img_id == 'image-7':
            digit_images[7] = href
        elif img_id == 'image-8':
            digit_images[8] = href
        elif img_id == 'image-9':
            digit_images[9] = href
            
    with open('digits.json', 'w', encoding='utf-8') as f_out:
        json.dump(digit_images, f_out, indent=2)
    print("Successfully wrote digits.json!")

if __name__ == "__main__":
    main()
