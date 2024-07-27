# Tiff on Tech - Automating .. Life - NFG !!!
# Date: 2021-07-07
# https://www.youtube.com/watch?v=LXsdt6RMNfY

# ChatGPT example
# pip install PyPDF2 gtts

import PyPDF2
from gtts import gTTS
import os

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extract_text()
        return text
    except FileNotFoundError:
        print(f"Error: The file at {pdf_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to convert text to speech and save as MP3
def text_to_speech(text, mp3_path):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(mp3_path)
        print(f"MP3 file saved at {mp3_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def pdf_to_mp3(pdf_path, mp3_path):
    text = extract_text_from_pdf(pdf_path)
    if text:
        text_to_speech(text, mp3_path)

# Example usage
pdf_path = 'C:\\path\\to\\your\\example.pdf'  # Replace with your PDF file path
mp3_path = 'C:\\path\\to\\your\\output.mp3'  # Replace with desired MP3 file path

# Convert relative paths to absolute paths
pdf_path = os.path.abspath(pdf_path)
mp3_path = os.path.abspath(mp3_path)

pdf_to_mp3(pdf_path, mp3_path)



