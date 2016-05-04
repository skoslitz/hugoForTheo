#!/usr/bin/env python
# Batch thumbnail generation script using PIL
# For PIL jpeg options see @ http://www.effbot.org/imagingbook/format-jpeg.htm

#!/usr/bin/env python
import os.path
from PIL import ImageFile
from PIL import Image


# The top argument for walk.
topdir = '.'

# The arg argument for walk, and subsequently ext for step
exten =  ('.jpg', '.JPG')

# TODO: user input sets correct img_file_name
# img_file_name = 'theo_05_2016_'

def step(ext, dirname, names):

    for name in names:

        # check if file extension equals defined ones in var exten
        if name.endswith(ext):
            filepath = os.path.join(dirname, name)
            try:
                image = Image.open(filepath)
                basewidth = 480

                if image.size[0] < basewidth:
                    basewidth = image.size[0]

            except IOError, e:
                # Report error, and then skip to the next argument
                print "Problem opening", filepath, ":", e
                continue

            width_ratio = (basewidth/float(image.size[0]))
            height = int((float(image.size[1])*float(width_ratio)))

            absolute_filepath = os.path.basename(filepath)
            # Split the original filename into name and extension
            (filename, extension) = os.path.splitext(absolute_filepath)

            #new_name = filename[:9] + file_suffix + filename[9:]

            # Resize the image with maintained aspect ration
            # and ANTIALIAS downsampling filter
            image = image.resize((basewidth,height), Image.ANTIALIAS)

            print "Image " + filename + " ... is in processing"

            # set buffer properly for saving image
            ImageFile.MAXBLOCK = 2 * image.size[0] * image.size[1]
            # Save image with renamed filepath, set jpeg options
            new_filepath = os.path.join(dirname, filename)
            image.save(new_filepath + '.JPG', progressive=True, quality=90)

            print (new_filepath + ".JPG was saved")


# Start the walk through folders
os.path.walk(topdir, step, exten)
