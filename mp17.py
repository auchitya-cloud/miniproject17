# Mini Project 17

import cv2
def grayscale(input, output):
    # Opening the file to read
    video_capture = cv2.VideoCapture(input)

    #Getting the Frame width and height of the Video
    Fwidth = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    Fheight = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Creating a VideoWriter object in order to save the greyscale video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output, fourcc, 20.0, (Fwidth, Fheight), isColor=False)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        # Frame to Greyscale Conversion
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Writing the grayscale frame to the output video
        out.write(gray_frame)

    # Releasing the videio objects
    video_capture.release()
    out.release()

    print("The coloured video was successfully converted to Greyscale!")

input_video = 'D:\Coding\Python programmming\summer_school\color_vid.mp4'
output_video = 'BW_output.mp4'
grayscale(input_video, output_video)