from PIL import Image
from pdf2image import convert_from_path
from os import listdir

arquivos = [f for f in listdir('.') if f.endswith('.pdf')]


def convert(path : str) -> Image:
    pdfs = convert_from_path(path, 500)
    width, height = pdfs[0].size[0], pdfs[0].size[1]
    image = Image.new('RGB', (width, height * len(pdfs)))
    for i in range(len(pdfs)):
        image.paste(pdfs[i], (0, height * i))
    return image
    


def save(path_to_save : str, image : Image):
    image.save(path_to_save, 'JPEG')

for arquivo in arquivos:
    save(f'{arquivo}.jpeg', convert(arquivo))
