
const fs = require('fs');
const path = require('path');

const newSearchCSS = `        .search-box {
            position: relative;
            z-index: 10000;
        }

        .search-box input {
            padding: 10px 40px 10px 12px;
            border: 2px solid #ddd;
            border-radius: 25px;
            width: 280px;
            font-size: 14px;
            transition: border-color 0.3s;
        }

        .search-box input:focus {
            outline: none;
            border-color: #0066cc;
        }

        .search-box button {
            position: absolute;
            right: 8px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            cursor: pointer;
            font-size: 18px;
            transition: transform 0.2s;
        }

        .search-box button:hover {
            transform: translateY(-50%) scale(1.1);
        }

        .search-suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            max-height: 400px;
            overflow-y: auto;
            z-index: 9999;
            display: none;
            margin-top: 5px;
        }

        .search-suggestions.show {
            display: block;
        }

        .search-suggestion-item {
            padding: 12px 15px;
            cursor: pointer;
            border-bottom: 1px solid #f0f0f0;
            transition: background-color 0.2s;
        }

        .search-suggestion-item:last-child {
            border-bottom: none;
        }

        .search-suggestion-item:hover {
            background-color: #f5f8ff;
        }

        .search-suggestion-item .product-name {
            font-weight: 600;
            color: #333;
            font-size: 14px;
        }

        .search-suggestion-item .product-category {
            font-size: 12px;
            color: #888;
            margin-top: 3px;
        }

        .search-no-results {
            padding: 20px;
            text-align: center;
            color: #888;
            font-size: 14px;
        }`;

const dir = 'd:\\work\\my_web.io';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f !== 'index.html');

files.forEach(file => {
    const filePath = path.join(dir, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Replace search CSS from .search-box { ... } up to .tagline
    const searchBoxStart = content.indexOf('.search-box {');
    if (searchBoxStart !== -1) {
        const taglineIndex = content.indexOf('.tagline {', searchBoxStart);
        if (taglineIndex !== -1) {
            const oldSearchCSS = content.substring(searchBoxStart, taglineIndex);
            content = content.substring(0, searchBoxStart) + newSearchCSS + '\n' + content.substring(taglineIndex);
            fs.writeFileSync(filePath, content, 'utf8');
            console.log(`Updated ${file}`);
        }
    }
});

console.log('All files processed!');
