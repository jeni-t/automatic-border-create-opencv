import cv2
image = cv2.imread("nature.jpg", cv2.IMREAD_COLOR)

shapes = image.shape
shape_array = shapes[0]
shape_array2 = shapes[1]
start_point = (5, 5)
end_point = (shape_array2-5, shape_array-5)
color = (255, 0, 0)
thickness = 2
image = cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.imshow("image", image)

#filename = 'savedImage.jpg'
#cv2.imwrite(filename, img)
