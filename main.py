import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import cv2

model_path = './exported_model/gesture_recognizer.task'

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    print('results: {}'.format(result))

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result,num_hands = 1)

with GestureRecognizer.create_from_options(options) as recognizer:
    cap = cv2.VideoCapture(0)
    timestamp = 0

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error opening,video stream")
        exit()

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        timestamp += 1
        
        # If frame is read correctly
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break
        # Display the resulting frame
        #cv2.imshow('frame', frame)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        processed_image = recognizer.recognize_async(mp_image,timestamp)
        print(processed_image)

        # If q is pressed, break the loop
        if cv2.waitKey(1) == ord('q'):
            break
            

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()


   

        
  
  