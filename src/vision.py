import cv2.aruco


def main():
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
    # default detection params
    aruco_params = cv2.aruco.DetectorParameters_create()
    test_images = []
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
