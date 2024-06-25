import sys
import os
from PIL import Image, ImageOps
def overlay_shirt(input_file, output_file):
    try:
        input_ext=os.path.splitext(input_file)[1].lower()
        output_ext=os.path.splitext(output_file)[1].lower()
        if input_ext not in ['.jpg', '.jpeg', '.png'] or output_ext not in ['.jpg', '.jpeg', '.png']:
            raise ValueError("Invalid output")
        if input_ext != output_ext:
            raise ValueError("Input and output have different extensions")
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' does not exist")
        input_image = Image.open(input_file)
        shirt_image = Image.open("shirt.png")
        input_image_resized = ImageOps.fit(input_image, shirt_image.size)
        input_image_resized.paste(shirt_image, (0,0), shirt_image)
        input_image_resized.save(output_file)
    except (ValueError, FileNotFoundError) as e:
        print(e)
        sys.exit(1)
if __name__ =="__main__":
    if len(sys.argv)<3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv)>3:
        print("Too many command-line arguments")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    overlay_shirt(input_file, output_file)



