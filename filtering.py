from PIL import Image
from PIL import ImageFilter
from pylab import *

image = Image.open('images/moon.png')
figure(figsize =(15,15))

subplot(2, 3, 1)
imshow(image)
title('Original')

subplot(2, 3, 2)
image1 =  image.filter(ImageFilter.CONTOUR)
imshow(image1)
title('Contour')

subplot(2, 3, 3)
image2 =  image.filter(ImageFilter.DETAIL)
imshow(image2)
title('Detail')

subplot(2, 3, 4)
image3 = image.filter(ImageFilter.EMBOSS)
imshow(image3)
title('Emboss')

subplot(2, 3, 5)
image4 =  image.filter(ImageFilter.SMOOTH_MORE)
imshow(image4)
title('Smooth')

subplot(2, 3, 6)
image5 = image.filter(ImageFilter.SHARPEN)
imshow(image5)
title('Sharpen')


