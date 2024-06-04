from matplotlib import pyplot as plt
import cv2

sun_filepath = 'images/flower.jpg'

sun = cv2.imread(sun_filepath)
sun = cv2.cvtColor(sun, cv2.COLOR_BGR2RGB)
sun_gray = cv2.imread(sun_filepath, cv2.IMREAD_GRAYSCALE)
ret, new_image = cv2.threshold(sun_gray, 0, 255, cv2.THRESH_OTSU)
plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.title('Original Flower Image')
plt.imshow(sun)
plt.subplot(1,2,2)
plt.title('New Image')
plt.imshow(new_image, cmap='gray')
plt.show()
