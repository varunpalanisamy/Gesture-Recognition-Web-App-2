# Gesture Recognition Web App

This project implements a gesture recognition system using a pre-trained model, integrated into a Flask web application. The application utilizes webcam input to capture images and predict gestures.

![Gesture Recognition Web App](screenshot.png)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Overview

This project provides a simple interface to recognize hand gestures using a webcam. The web app captures images and uses a machine learning model to predict gestures in real-time. It is inspired by existing web applications that perform similar tasks.

## Features

- Real-time gesture recognition using webcam input.
- Supports multiple hand gestures.
- User-friendly web interface.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **TensorFlow**: An open-source machine learning library used for training and inference of the model.
- **OpenCV**: For handling image capture and processing.
- **MediaPipe**: A framework for building multimodal applied machine learning pipelines.
- **NumPy**: Fundamental package for scientific computing in Python.

## Getting Started

To run this project locally, follow these steps:

### Prerequisites

Make sure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/varunpalanisamy/Gesture-Recognition-Web-App-2.git
   cd Gesture-Recognition-Web-App-2


2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install the required packages:

   ```bash
   pip install -r requirements.txt

### Running the Application

1. Start the Flask server:

   ```bash
   python app.py

2. Open your browser and navigate to http://127.0.0.1:5000 to access the web app.

## Usage
1. Click the Start Webcam button to begin capturing video.
2. Position your hand in front of the camera to predict the gesture.
3. The predicted gesture will be displayed on the screen.

## Credits
This project uses a pre-trained model from KelvinPuyam/Hand-Gesture-Recognition for real-time hand gesture recognition.
## License
This project is licensed under the MIT License. See the LICENSE file for details.# Gesture-Recognition-Web-App
