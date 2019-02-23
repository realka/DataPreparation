from PIL import Image
import glob, os
import sys
#name="explainer.jpg"
name= sys.argv[1]
counter = 351
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.save(name+str(counter)+".jpg")
    counter = counter + 1


