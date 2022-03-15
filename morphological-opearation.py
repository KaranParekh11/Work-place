import cv2
import numpy as np

def main():
    image = cv2.imread('demo.jpg', 0)
    if image is None:
        print("Error Opening Image")
        return -1

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(image, kernel, iterations=1)
    dilation = cv2.dilate(image, kernel, iterations=1)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


    show(erosion,"erosion")
    show(dilation,"dilation")
    show(opening,"opening")
    show(closing,"closing")

def show(image,name):
    cv2.imwrite(name+".jpg",image)
    img = cv2.imread(name + ".jpg")
    # cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    ims = cv2.resize(img,(540,540))
    cv2.imshow(name, ims)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
