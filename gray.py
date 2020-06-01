from pylab import *
from PIL import Image

START_INTERVAL = 100.0
END_INTERVAL = 255.0
NEGATION = 255.0

image = array(Image.open('images/dream.jpg').convert('L'))
gray()

negative = NEGATION - image
clamped = (START_INTERVAL / NEGATION) * image + START_INTERVAL

transformed = END_INTERVAL * (image / END_INTERVAL) ** 2

imshow(transformed)
