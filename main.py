import pyttsx3
import PyPDF2

pdf_book=open("What-is-Enlightenment.pdf","rb")
pdf_reader=PyPDF2.PdfReader(pdf_book)
pages=len(pdf_reader.pages)
print(f"{pages} pages")

speaker=pyttsx3.init()
for index in range(0,pages):
    chosen_page=pdf_reader.pages[index]
    pdf_text=chosen_page.extract_text()
    speaker.say(pdf_text)
    speaker.runAndWait()