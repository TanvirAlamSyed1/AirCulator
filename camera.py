import cv2

# Open a video capture object (0 for the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error opening  video stream")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If frame is read correctly
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # If q is pressed, break the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()