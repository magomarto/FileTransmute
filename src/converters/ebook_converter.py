''' 
-- EBOOK   
    CHM Converter
    AZW Converter # kindleeunpack ou pydf
    AZW4 Converter # kindleeunpack ou pydf
    AZW3 Converter # kindleeunpack ou pydf
'''
import os
from ebooklib import epub
from pathlib import Path

class EbookConverter:
    def __init__(self, input_file):
        self.input_file = input_file

    def convert_to_epub(self): # epub convert
        output_file = f"{self.input_file.rsplit('.', 1)[0]}.epub"
        book = epub.read_epub(self.input_file)
        epub.write_epub(output_file, book)
        return output_file

    def convert_to_mobi(self): # mobi convert
        output_file = f"{self.input_file.rsplit('.', 1)[0]}.mobi"
        os.system(f"ebook-convert {self.input_file} {output_file}")
        return output_file

    def convert_to_fb2(self): # fb2 convert
        output_file = f"{self.input_file.rsplit('.', 1)[0]}.fb2"
        os.system(f"ebook-convert {self.input_file} {output_file}")
        return output_file
    
    def convert_to_lit(self): #lit convert
        output_file = f"{self.input_file.rsplit('.', 1)[0]}.lit"
        os.system(f"ebook-convert {self.input_file} {output_file}")
        return output_file
    