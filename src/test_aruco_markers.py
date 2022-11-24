import cv2


# im lazy
def round_tuple(tuple):
    return (int(tuple[0]), int(tuple[1]))

def main():
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    # default detection params
    aruco_params = cv2.aruco.DetectorParameters_create()
    img1 = cv2.imread("test_images/photo1.jpg")
    img2 = cv2.imread("test_images/photo2.jpg")
    img3 = cv2.imread("test_images/photo3.jpg")
    test_images = [img1, img2, img3]
    # TODO open images and put them in test_images
    
    for img in test_images:
        # detect aruco markers
        (corners, ids, rejected) = cv2.aruco.detectMarkers(img, aruco_dict, parameters=aruco_params)
        if len(corners) > 0:
            ids = ids.flatten()
            for (marker_corner, marker_id) in zip(corners, ids):
                # extract the marker corners
                dc = marker_corner.reshape((4,2))
                (top_left, top_right, bottom_right, bottom_left) = dc
                top_left = round_tuple(top_left)
                top_right = round_tuple(top_right)
                bottom_left = round_tuple(bottom_left)
                bottom_right = round_tuple(bottom_right)
                # draw the bounding box of the ArUCo detection
                cv2.line(img, top_left, top_right, (0, 255, 0), 2) 
                cv2.line(img, top_right, bottom_right, (0, 255, 0), 2)
                cv2.line(img, bottom_right, bottom_left, (0, 255, 0), 2)
                cv2.line(img, bottom_left, top_left, (0, 255, 0), 2)
                # compute and draw the center (x, y)-coordinates of the ArUco marker
                cX = int((top_left[0] + bottom_right[0]) / 2.0)
                cY = int((top_left[1] + bottom_right[1]) / 2.0)
                cv2.circle(img, (cX, cY), 4, (0, 0, 255), -1)
                
                # show the output image
                cv2.imshow("Image", img)
                cv2.waitKey(0)
    
    cv2.destroyAllWindows()

main()