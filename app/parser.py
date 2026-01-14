from pypdf import PdfReader

WPM = 260  # average adult reading speed

def get_word_count(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:  
            text += page_text + " "

    words = text.split()
    return len(words)

def calculate_reading_time(pdf):
    return get_word_count(pdf) / WPM

pdf = ("Horne, J. Resume 2025.pdf")

word_count = get_word_count(pdf)
reading_time = calculate_reading_time(pdf)

print(f"Word count: {word_count}")
print(f"Estimated reading time: {reading_time:.2f} minutes")


