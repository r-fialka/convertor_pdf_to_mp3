import pdfplumber
from pathlib import Path
from gtts import gTTS

def to_mp3(file_path = 'test.pdf', language = 'en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'\nThank you for waiting....')

        with pdfplumber.PDF(open(file = file_path, mode = 'rb')) as pdf:

            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        this_mp3 = gTTS(text = text, lang = language, slow = False)
        this_name = Path(file_path).stem
        this_mp3.save(f'{this_name}.mp3')

        return f'\n{this_name}.mp3 saved successfully!\n'

    else:
        return "this file doesn't exist"

def main():
    print(f"\nConvertor pdf to mp3")
    file_path = input("\nEnter a file's path: ")
    print(f'\nYour file: {Path(file_path).name}')
    language = input("\nChose language, for example 'ru': ")
    print(to_mp3(file_path = file_path, language = language))

if __name__ == '__main__':
    main()