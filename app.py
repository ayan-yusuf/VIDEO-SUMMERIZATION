from flask import Flask, render_template, request, send_file
import os
import cv2
import numpy as np

app = Flask(__name__)

# Video summarization logic - keeps only frames with movement
def summarize_video(input_video_path):
    cap = cv2.VideoCapture(input_video_path)
    
    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec and create a VideoWriter object for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('static/output_video.mp4', fourcc, fps, (frame_width, frame_height))

    ret, prev_frame = cap.read()  # Read the first frame
    if not ret:
        return  # No frame read, exit the function

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale for movement detection
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)  # Apply Gaussian blur to reduce noise

    # Loop through each frame in the video
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the current frame to grayscale and blur it
        curr_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        curr_gray = cv2.GaussianBlur(curr_gray, (21, 21), 0)

        # Compute the absolute difference between the current frame and the previous frame
        frame_diff = cv2.absdiff(prev_gray, curr_gray)

        # Apply a binary threshold to the difference image
        _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

        # Dilate the threshold image to fill in holes and find contours
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Calculate the total movement in the frame
        movement_amount = np.sum(thresh)

        # Define a movement threshold; adjust as needed
        movement_threshold = 5000

        # If the movement is above the threshold, write the frame to the output video
        if movement_amount > movement_threshold:
            out.write(frame)

        # Update the previous frame for the next iteration
        prev_gray = curr_gray

    # Release the video objects
    cap.release()
    out.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/videosumm.html')
def video_summarization():
    return render_template('videosumm.html')  # Route for Video Summarization

@app.route('/object.html')
def object_detection():
    return render_template('object.html')  # Route for Object Detection

@app.route('/videoskimm.html')
def video_skimming():
    return render_template('videoskimm.html')  # Route for Video Skimming

@app.route('/upload', methods=['POST'])
def upload_video():
    
    if 'video' not in request.files:
        return "No video uploaded", 400

    video = request.files['video']
    input_video_path = os.path.join('static', video.filename)
    video.save(input_video_path)

    # Call the summarize_video function to process the video
    summarize_video(input_video_path)

    # Send the summarized video as a downloadable file
    return send_file('static/output_video.mp4', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
