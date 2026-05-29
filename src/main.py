import sys
from source_transfer import static_to_public
from extract_markdown import extract_title
from page_generator import generate_pages_recursive

def Main():
    static_to_public()
    arg = "/"
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    basepath = arg
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)
Main()