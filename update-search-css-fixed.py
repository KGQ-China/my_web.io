
import os

# Read index.html to get the correct search CSS block
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the search CSS block from index.html (using fixed version!)
# The block starts at '.search-box {' and ends just before '.tagline {'
start_search = index_content.find('.search-box {')
end_search = index_content.find('.tagline {', start_search)
if start_search == -1 or end_search == -1:
    print("Error: Could not find search CSS block in index.html")
    exit(1)

correct_search_block = index_content[start_search:end_search]

# Process all other HTML files
dir_path = '.'
files = [f for f in os.listdir(dir_path) if f.endswith('.html') and f != 'index.html']

for file in files:
    print(f"Processing: {file}")
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the old search block
    old_search_start = content.find('.search-box {')
    if old_search_start == -1:
        print(f"  No .search-box found in {file}")
        continue
    
    old_search_end = content.find('.tagline {', old_search_start)
    if old_search_end == -1:
        print(f"  No .tagline found after .search-box in {file}")
        continue
    
    # Replace old block
    new_content = content[:old_search_start] + correct_search_block + content[old_search_end:]
    
    # Write back
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  Updated {file}")

print("\nAll files processed!")
