from PIL import Image, ImageFilter
import sys
import os

# Enter the two folder name with \
input_folder = sys.argv[1]
output_folder = sys.argv[2]


# This will create output folder if its not exist

def folder_creator(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# This will convert JPEG images to PNG and save in the directory pass through argument


def jpeg_to_png(inputfolder, outputfolder):
    for filename in os.listdir(inputfolder):
        img = Image.open(f'{inputfolder}{filename}')
        cleaned_name = os.path.splitext(filename)[0]
        img.save(f'{outputfolder}{cleaned_name}.png', 'png')

if __name__ == '__main__':
    folder_creator(output_folder)
    jpeg_to_png(input_folder, output_folder)