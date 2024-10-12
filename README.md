
# Advanced Video Analysis Platform

This repository contains a Flask-based web application designed for video summarization using computer vision techniques. The app processes videos to retain only key moments with significant movement, producing concise summaries of long videos.

## Table of Contents:
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Video Summarization Process](#video-summarization-process)
- [License](#license)

## Features:
- 🎥 **Video Summarization**: Extract and retain frames containing significant motion, creating concise summaries of long videos.
- 🔍 **Object Detection**: Future integration for detecting and tracking objects in the video.
- ⚡ **Video Skimming**: Quickly skim through video content, jumping to key moments.
- 📂 **Video Format Support**: Supports MP4, AVI, and MOV formats, with a maximum file size of 800MB.
- 📥 **Downloadable Results**: Users can download the summarized video after processing.

## Project Structure:
```
|-- app.py                # Main application logic
|-- templates/
    |-- index.html        # HTML for video upload and feature display
|-- static/
    |-- output_video.mp4  # Summarized video output saved here
|-- requirements.txt      # List of Python dependencies
```

## Technologies Used:
- **Flask**: For building the web interface.
- **OpenCV**: For video processing and motion detection.
- **HTML/CSS**: To design the frontend interface.
- **Bootstrap**: For responsive design and styling.

## Setup Instructions:

### 1. Clone the repository:
```bash
git clone https://github.com/ayan-yusuf/VIDEO-SUMMERIZATION.git
cd VIDEO-SUMMERIZATION
```

### 2. Install the dependencies:
Ensure you have Python 3.x installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask application:
```bash
python app.py
```
The app will start on `http://localhost:5000`.

## Usage:

1. **Upload a Video**: Use the form on the homepage to upload a video in MP4, AVI, or MOV format.
2. **Processing**: The backend processes the video, keeping only frames with significant movement.
3. **Download the Result**: Once the summarization is complete, the output video can be downloaded.

## Video Summarization Process:

The summarization process works by analyzing the difference between consecutive frames:
1. Convert each frame to grayscale.
2. Apply Gaussian blur to reduce noise.
3. Calculate the difference between consecutive frames.
4. If the difference exceeds a certain threshold (indicating significant movement), the frame is included in the summarized output.

## Future Enhancements:
- Add object detection and tracking using YOLO or similar frameworks.
- Include additional video analysis features like face detection, scene change detection, etc.
