# AirCulator
A calculator that you can use in the air :)  This project will hopefully be using hand detection in order to calculate simple maths. 

### Steps in creating the customised model

Firstly, I searched up google's gesture recognisiton as a guide point (Link can be found here: https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer/python#video ) This led me to a link that allowed me to customise my own model using this link : https://ai.google.dev/edge/mediapipe/solutions/customization/gesture_recognizer.


## Current update on the project
Date - 30/08/24

I'm currently working on training my own model so that it can detect my own hand signals.
 I've finished collecting data and will now work on training the AI model. I'm thinking of either using Voice detection for the mathmatical symbols. OR a screen with the symbols 

 Date - 31/08/24

 wild ride today, I spent so much time on finding the right versions because of failed library installations. I have made a requirement folder that worked for me, but please do try and see what works for you. 

 Date - 2/09/24

 Don't try to attemp to to run the training code on your laptop as google.colab doesn't work unless you run it in the google colab environment. I recommend you upload your folder( that is structured similar to the sample folder provided in the repo )to to Google Drive, then run the code they provide here: https://colab.research.google.com/github/googlesamples/mediapipe/blob/main/examples/customization/gesture_recognizer.ipynb#scrollTo=sx8PsrwYjvgO. Edit the code they provide by adding the destination of your file from your google drive, and make sure the folder that is created at the end is also saved in your google drive. for each folder that is labelled, make sure to have 50-100 images to train the data.

 Date - 3/9/24
 I have got the code running and is showing some results when I put my hand in front of the screen. Next is to get a visual representation of the hand. I'm not sure if the actual model is good but I shall try next run.
