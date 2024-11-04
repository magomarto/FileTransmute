'''
-- AUDIO

    ALAC pydub nao suporta
    raw-audio Converter
    WAVE Converter
    OGA Converter
    APE pydub nao suporta
    M4R pydub nao suporta
    MID / MIDI / RMI pydub nao suporta
    AIF Converter
    CAF Converter
    AIFC Converter
    raw Converter
    3GA : pydub nao suporta
    iPad Audio Converter
    Android Audio Converter
    Ipod Audio Converter
    iPhone Audio Converter

'''
from pydub import AudioSegment

class AudioConverter:
    def __init__(self, input_file):
        self.input_file = input_file
        
    def convert_audio(input_file, output_format):

        audio = AudioSegment.from_file(input_file)
        output_file = f"{input_file.rsplit('.', 1)[0]}.{output_format}"
        audio.export(output_file, format=output_format)

        return output_file
    
audio_formats = ['WMA','WAV','mp3','MP2','mp1','m4p','M4P','AMR','wav', 'ogg', 'flac', 'aiff', 'm4a','M4B', 'aac', 'OPUS']  