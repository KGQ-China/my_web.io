
import os

def process_file(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Step 1: Find what the correct leading whitespace is for CSS rules in this file.
    # Look for '.company-name' line, since that's right before the search block.
    leading_spaces = ''
    company_name_line_idx = -1
    for i, line in enumerate(lines):
        if '.company-name' in line:
            company_name_line_idx = i
            # Count how many leading spaces before '.company-name'
            leading_spaces = line.split('.company-name')[0]
            break
    if company_name_line_idx == -1:
        print("  Can't find .company-name line")
        return
    
    # Step 2: Find the start and end indices of the search CSS block
    search_start_idx = -1
    search_end_idx = -1
    tagline_idx = -1
    for i, line in enumerate(lines):
        if '.search-box {' in line:
            search_start_idx = i
        if '.tagline {' in line:
            tagline_idx = i
            if search_start_idx != -1 and search_end_idx == -1:
                search_end_idx = i
    if search_start_idx == -1 or search_end_idx == -1:
        print("  Can't find search block or .tagline line")
        return
    
    # Step 3: Define the correct search block with the right leading spaces
    correct_search_lines = [
        f"{leading_spaces}.search-box {{\n",
        f"{leading_spaces}    position: relative;\n",
        f"{leading_spaces}    z-index: 10000;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-box input {{\n",
        f"{leading_spaces}    padding: 10px 40px 10px 12px;\n",
        f"{leading_spaces}    border: 2px solid #ddd;\n",
        f"{leading_spaces}    border-radius: 25px;\n",
        f"{leading_spaces}    width: 280px;\n",
        f"{leading_spaces}    font-size: 14px;\n",
        f"{leading_spaces}    transition: border-color 0.3s;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-box input:focus {{\n",
        f"{leading_spaces}    outline: none;\n",
        f"{leading_spaces}    border-color: #0066cc;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-box button {{\n",
        f"{leading_spaces}    position: absolute;\n",
        f"{leading_spaces}    right: 8px;\n",
        f"{leading_spaces}    top: 50%;\n",
        f"{leading_spaces}    transform: translateY(-50%);\n",
        f"{leading_spaces}    background: none;\n",
        f"{leading_spaces}    border: none;\n",
        f"{leading_spaces}    cursor: pointer;\n",
        f"{leading_spaces}    font-size: 18px;\n",
        f"{leading_spaces}    transition: transform 0.2s;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-box button:hover {{\n",
        f"{leading_spaces}    transform: translateY(-50%) scale(1.1);\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-suggestions {{\n",
        f"{leading_spaces}    position: absolute;\n",
        f"{leading_spaces}    top: 100%;\n",
        f"{leading_spaces}    left: 0;\n",
        f"{leading_spaces}    right: 0;\n",
        f"{leading_spaces}    background: white;\n",
        f"{leading_spaces}    border: 1px solid #ddd;\n",
        f"{leading_spaces}    border-radius: 8px;\n",
        f"{leading_spaces}    box-shadow: 0 4px 12px rgba(0,0,0,0.15);\n",
        f"{leading_spaces}    max-height: 400px;\n",
        f"{leading_spaces}    overflow-y: auto;\n",
        f"{leading_spaces}    z-index: 9999;\n",
        f"{leading_spaces}    display: none;\n",
        f"{leading_spaces}    margin-top: 5px;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-suggestions.show {{\n",
        f"{leading_spaces}    display: block;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-suggestion-item {{\n",
        f"{leading_spaces}    padding: 12px 15px;\n",
        f"{leading_spaces}    cursor: pointer;\n",
        f"{leading_spaces}    border-bottom: 1px solid #f0f0f0;\n",
        f"{leading_spaces}    transition: background-color 0.2s;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-suggestion-item:last-child {{\n",
        f"{leading_spaces}    border-bottom: none;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-suggestion-item:hover {{\n",
        f"{leading_spaces}    background-color: #f5f8ff;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-suggestion-item .product-name {{\n",
        f"{leading_spaces}    font-weight: 600;\n",
        f"{leading_spaces}    color: #333;\n",
        f"{leading_spaces}    font-size: 14px;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-suggestion-item .product-category {{\n",
        f"{leading_spaces}    font-size: 12px;\n",
        f"{leading_spaces}    color: #888;\n",
        f"{leading_spaces}    margin-top: 3px;\n",
        f"{leading_spaces}}}\n",
        "\n",
        f"{leading_spaces}.search-no-results {{\n",
        f"{leading_spaces}    padding: 20px;\n",
        f"{leading_spaces}    text-align: center;\n",
        f"{leading_spaces}    color: #888;\n",
        f"{leading_spaces}    font-size: 14px;\n",
        f"{leading_spaces}}}\n",
        "\n"
    ]
    
    # Step 4: Replace the old search lines with correct lines
    new_lines = lines[:search_start_idx] + correct_search_lines + lines[search_end_idx:]
    
    # Step 5: Fix the .tagline line indentation in new_lines
    for i, line in enumerate(new_lines):
        if '.tagline {' in line:
            # Extract the actual .tagline part (without leading whitespace)
            tagline_content = line.lstrip()
            new_lines[i] = leading_spaces + tagline_content
            break
    
    # Step 6: Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("  Updated!")

# Process all .html files in current dir
dir_path = '.'
html_files = [f for f in os.listdir(dir_path) if f.lower().endswith('.html')]

for file in html_files:
    process_file(os.path.join(dir_path, file))

print("\nDone!")
