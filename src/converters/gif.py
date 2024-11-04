import os
from moviepy.editor import VideoFileClip
from PIL import Image
'''
-- GIF

    Video to GIF
    WEBM to GIF
    APNG to GIF
    GIF to APNG
    GIF Converter
    GIF to PS
    GIF to DOCX
    GIF to WORD
    GIF to DOC
    GIF to ICO
    GIF to SVG
    GIF to TIFF
    GIF to BMP
    GIF to PNG
    GIF to ODD
    GIF to PSD
    GIF to JPEG

'''
class GIFConverter:
    def __init__(self, input_file):
        self.input_file = input_file

    def mp4_to_gif(self, output_file):# MP4 to GIF
        clip = VideoFileClip(self.input_file)
        clip.write_gif(output_file)

    def gif_to_mp4(self, output_file):#  GIF to MP4
        clip = VideoFileClip(self.input_file)
        clip.write_videofile(output_file)

    def gif_to_png(self, output_file): #  GIF to PNG
        img = Image.open(self.input_file)
        img.save(output_file)

    def gif_to_jpg(self, output_file): # GIF to JPG
        img = Image.open(self.input_file)
        rgb_img = img.convert('RGB')
        rgb_img.save(output_file)

    def gif_to_webp(self, output_file): #  GIF to WebP
        img = Image.open(self.input_file)
        img.save(output_file, 'WEBP')

    def convert(self, output_format):
        output_path = f"{os.path.splitext(self.input_file)[0]}.{output_format}"
        if output_format.lower() == 'png':
            self.gif_to_png(output_path)
        elif output_format.lower() == 'jpg':
            self.gif_to_jpg(output_path)
        elif output_format.lower() == 'webp':
            self.gif_to_webp(output_path)

