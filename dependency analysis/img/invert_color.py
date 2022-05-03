from PIL import Image
import PIL.ImageOps    
import glob

def convert(filename):
    image = Image.open(filename)
    filename_no_ext=filename.split(".")[0]
    new_file_name="new_"+filename_no_ext+".png"
    if image.mode == 'RGBA':
        r,g,b,a = image.split()
        rgb_image = Image.merge('RGB', (r,g,b))

        inverted_image = PIL.ImageOps.invert(rgb_image)

        r2,g2,b2 = inverted_image.split()

        final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))

        final_transparent_image.save(new_file_name)

#    else:
#        inverted_image = PIL.ImageOps.invert(image)
#        inverted_image.save(new_file_name)


file_names=glob.glob('*.png')
print(file_names)
for file in file_names:
    convert(file)


