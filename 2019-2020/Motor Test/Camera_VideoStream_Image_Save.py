# Python program to save a
# video using Test-OpenCV
import cv2
import os

# Create an object to read
# from camera
video = cv2.VideoCapture(0)

# We need to check if camera
# is opened previously or not
if (video.isOpened() == False):
    print("Error reading video file")

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
#result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

path = ('/home/pi/Desktop/Videos/video_deneme.avi')
result = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
ph = 1
while (True):
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
ssssssssssss    frame = cv2.flip(frame, 0)

    if ret == True:

        # Write the frame into the
        # file 'filename.avi'
        result.write(frame)

        # Display the frame
        # saved in the file
        cv2.imshow('Frame', frame)

        # Press S on keyboard
        # to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        if cv2.waitKey(1) & 0xFF == ord('p'):
            cv2.imwrite(os.path.join('/home/pi/Desktop/Images', 'image%s.jpg' % ph), frame)
            ph += 1
            print("Image saved")
    # Break the loop
    else:
        break

# When everything done, release
# the video capture and video
# write objects
video.release()
result.release()

# Closes all the frames
cv2.destroyAllWindows()

print("The video was successfully saved")