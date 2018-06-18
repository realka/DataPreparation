
from PIL import Image
import glob, os
name="explainer.jpg"
counter = 1
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.save(str(counter)+name+".jpg")
    counter = counter + 1
    

