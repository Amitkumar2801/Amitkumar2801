module.exports = async (req, res) => {
  const url = "https://kauntah-svg.vercel.app/counter.svg?asset=blue&offset=902";
  
  try {
    const response = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0'
      }
    });
    
    if (!response.ok) {
      throw new Error(`Failed to fetch: ${response.statusText}`);
    }
    
    let svg = await response.text();
    
    // Define the CSS animation style block with a special animation for the last digit
    const styleBlock = `
    <style>
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
      
      @keyframes highlightLastDigit {
        0% {
          transform: translateY(150px) scale(0.7) rotate(-12deg);
          opacity: 0;
        }
        50% {
          transform: translateY(-40px) scale(1.2) rotate(6deg);
          opacity: 1;
        }
        75% {
          transform: translateY(10px) scale(0.95) rotate(-3deg);
        }
        100% {
          transform: translateY(0) scale(1) rotate(0deg);
          opacity: 1;
        }
      }
      
      .digit {
        animation: raiseHand 0.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
        transform-origin: bottom center;
        opacity: 0;
      }
      
      .last-digit {
        animation: highlightLastDigit 1.2s cubic-bezier(0.18, 0.89, 0.32, 1.28) forwards;
        transform-origin: bottom center;
        opacity: 0;
      }
    </style>
    `;
    
    // Insert style block right after the opening <svg> tag
    svg = svg.replace(/<svg ([^>]+)>/, `<svg $1>${styleBlock}`);
    
    // Find all <use> tags and modify them
    const useRegex = /<use\s+([^>]+)>/g;
    const matches = [...svg.matchAll(useRegex)];
    const totalUses = matches.length;
    
    let matchCount = 0;
    svg = svg.replace(/<use\s+([^>]+)>/g, (match, attributes) => {
      const delay = (matchCount * 0.08);
      let className = 'digit';
      let finalDelay = delay;
      
      // If it is the last element, apply the special last-digit animation
      if (matchCount === totalUses - 1) {
        className = 'last-digit';
        finalDelay = delay + 0.1;
      }
      
      matchCount++;
      // Check if style attribute already exists
      if (attributes.includes('style=')) {
        return `<use class="${className}" ${attributes.replace(/style="([^"]*)"/, `style="$1 animation-delay: ${finalDelay.toFixed(2)}s;"`)}>`;
      } else {
        return `<use class="${className}" style="animation-delay: ${finalDelay.toFixed(2)}s;" ${attributes}>`;
      }
    });
    
    res.setHeader('Content-Type', 'image/svg+xml');
    res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate');
    res.setHeader('Pragma', 'no-cache');
    res.setHeader('Expires', '0');
    res.status(200).send(svg);
    
  } catch (error) {
    res.status(500).send(`Error generating animated counter: ${error.message}`);
  }
};
