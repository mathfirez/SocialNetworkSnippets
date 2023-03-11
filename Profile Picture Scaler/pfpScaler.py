from PIL import Image, ImageDraw


def imageMaker(x,y):

    #   Opens the image used for the circular mask in grayscale with the convert L parameter
    with Image.open('mask.png').convert('L') as mask:
        mask = mask.resize((x,y))

    #   Opens the image to be used as profile picture
    with Image.open('pfp.png') as im:
        im = im.resize((x, y))

    #   Creating a new image with 128x128 size
    finalImage = Image.new('RGB', (x,y),)

    #   Putting the mask on the image
    finalImage.paste(im, mask=mask)

    #   Making the mask the Alpha Layer
    finalImage.putalpha(mask)

    #   Saving the output in different sizes
    finalFileName = str(x) + 'image.png'
    finalImage.save(finalFileName)

imageMaker(128,128)
imageMaker(64,64)
imageMaker(32,32)


