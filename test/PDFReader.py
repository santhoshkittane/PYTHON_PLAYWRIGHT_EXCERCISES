import re
from pypdf import PdfReader

def check_pdf_for_data(pdf_path, search_term):
    reader = PdfReader(pdf_path)
    print(f"Total Pages: {len(reader.pages)}")
    flag = 0
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

    # Context safety check in case a page is an image or empty
        if not text:
            continue

        if search_term.lower() in text.lower():
            flag = 1
            print(f"{search_term} found on page {page_num}")

    if flag == 0:
        print("No DATA found")


INP = input("Enter the PDF file with absolute path: ")
SearchTerm = input("Enter the search term to search for: ")

check_pdf_for_data(INP, SearchTerm)


