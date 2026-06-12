import urllib.request
import xml.etree.ElementTree as ET
import sys

def main():
    url = "https://kauntah-svg.vercel.app/counter.svg?asset=blue&offset=902"
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            svg_data = response.read()
    except Exception as e:
        print(f"Error fetching SVG: {e}")
        sys.exit(1)

    # Register the SVG namespace to prevent namespace prefixes in output
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    
    try:
        root = ET.fromstring(svg_data)
    except Exception as e:
        print(f"Error parsing SVG XML: {e}")
        sys.exit(1)

    # Define the CSS animation style block
    style_content = """
    @keyframes raiseHand {
      0% {
        transform: translateY(150px) scale(0.8);
        opacity: 0;
      }
      50% {
        transform: translateY(-20px) scale(1.05);
        opacity: 1;
      }
      70% {
        transform: translateY(5px) scale(0.98);
      }
      100% {
        transform: translateY(0) scale(1);
        opacity: 1;
      }
    }
    .digit {
      animation: raiseHand 0.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
      transform-origin: bottom center;
      opacity: 0;
    }
    """
    
    # Create the style element
    style_elem = ET.Element('style')
    style_elem.text = style_content
    
    # Insert the style element at the beginning of the SVG root
    root.insert(0, style_elem)
    
    # Find all 'use' elements and add classes/animations
    # In SVG, elements are usually namespace-prefixed during parsing if not registered,
    # but since we registered '', we can find them. We'll search both with and without namespace.
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    use_elements = root.findall('.//svg:use', namespaces) or root.findall('.//use')
    
    for idx, use_elem in enumerate(use_elements):
        # Set class
        use_elem.set('class', 'digit')
        # Set animation delay for staggering
        delay = idx * 0.08
        use_elem.set('style', f'animation-delay: {delay:.2f}s;')
        
    # Write the modified XML to counter.svg
    try:
        tree = ET.ElementTree(root)
        tree.write('counter.svg', encoding='utf-8', xml_declaration=True)
        print("Successfully generated animated counter.svg!")
    except Exception as e:
        print(f"Error writing counter.svg: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
