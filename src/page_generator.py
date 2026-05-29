import os
from block_markdown import markdown_to_html_node
from extract_markdown import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_contents = ""
    template_contents = ""
    with open(from_path) as file:
        markdown_contents = file.read()
    with open(template_path) as file:
        template_contents = file.read()

    title = extract_title(markdown_contents)
    content = markdown_to_html_node(markdown_contents).to_html()
    collected = template_contents.replace("{{ Title }}", title)
    collected = collected.replace("{{ Content }}", content)
    collected = collected.replace('href="/', f'href="{basepath}')
    collected = collected.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, "w") as file:
        file.write(collected)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, entry)):
            new_entry = entry.replace(".md", ".html") 
            generate_page(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, new_entry), basepath)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry), basepath)