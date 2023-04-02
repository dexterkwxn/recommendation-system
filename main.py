import cv2

def main():
    image = cv2.imread('room.jpg')
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()