# This line imports or includes the library we will need
from PIL import Image

#asks the user what images it would like to have as background and foreground
background = input('What image would you like to be the background? ')
green_screen = input('What image would you like to be infront of the background? ')

# This line opens the image and loads it into a variable called "image_green_screen"
image_green_screen = Image.open(f"{green_screen}.jpg")
image_background = Image.open(f"{background}.jpg")

# Create a new image in RGB format that is the same size as image_green_screen
image_new = Image.new("RGB", image_background.size)
pixels_new = image_new.load()

#give size
width, height = image_background.size

#pixel info
pixels_background = image_background.load()
pixels_green_screen = image_green_screen.load()
print(pixels_green_screen[1,1])

#do the if to see if r is less than x than do this if g is less/greater than y do this if b is less/greater than z do this
# color changing
for x in range(1, width):
    for y in range(1, height):
        r, g, b = pixels_green_screen[x,y]
        #this if tells if the pixel color is green then copy over the background
        if r <= 125 and g >= 125 and b <= 125:
            pixels_new[x,y] = pixels_background[x,y]
        #this if tells if the pixel color isn't green then copy over the foreground
        else:
            pixels_new[x,y] = pixels_green_screen[x,y]

# This line attempts to open a new window to display the image.
image_new.show()

#save file
image_new.save("new.jpg")
