
import os

# Read index.html to get the correct search CSS block
index_path = os.path.join(r'd:\work\my_web.io', 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the search CSS block from index.html
search_start = index_content.find('.search-box {')
tagline_start = index_content.find('.tagline {', search_start)
if search_start == -1 or tagline_start == -1:
    print("Error: Could not find search CSS block in index.html")
    exit(1)

new_search_css = index_content[search_start:tagline_start]

# Process all other HTML files
dir_path = r'd:\work\my_web.io'
files = [f for f in os.listdir(dir_path) if f.endswith('.html') and f != 'index.html']

for file in files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    search_box_start = content.find('.search-box {')
    if search_box_start != -1:
        tagline_index = content.find('.tagline {', search_box_start)
        if tagline_index != -1:
            new_content = content[:search_box_start] + new_search_css + content[tagline_index:]
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file}')

print('All files processed!')
