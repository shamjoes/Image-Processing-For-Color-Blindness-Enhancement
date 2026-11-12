# Real-Time Color Detection & Assistive Audio Guidance System

An assistive computer vision application designed to aid individuals with color vision deficiency by detecting and naming colors in real-time camera streams or static images, complete with voice narration.

## Features
- **Live Video Color Detection**: Instant RGB sampling and minimum Euclidean distance matching.
- **Speech Narration**: Speaks identified color names out loud using text-to-speech.
- **Extensive Color Palette**: Matches against comprehensive labeled RGB values.

## Quickstart

`ash
git clone https://github.com/shamjoes/Image-Processing-For-Color-Blindness-Enhancement.git
cd Image-Processing-For-Color-Blindness-Enhancement

pip install -r requirements.txt
python real_time_colordetection.py
`

## Tech Stack
- Python 3.8+
- OpenCV
- Pandas & NumPy
- pyttsx3