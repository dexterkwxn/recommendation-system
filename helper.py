def show_image(filename):
    image = cv2.imread(filename)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

