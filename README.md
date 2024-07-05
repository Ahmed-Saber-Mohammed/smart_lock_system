
# Smart Lock System using Raspberry Pi 5

  

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue)

  

## Description

This project implements a smart lock system using Raspberry Pi 5. It uses facial recognition to identify authorized users and unlocks the door using a servo motor controlled by a GPIO pin. The system leverages `OpenCV` for image processing and the `face_recognition` library for facial recognition using only one image for each person.

  

## Table of Contents

- [Installation](#installation)

- [Hardware Components](#hardware-components)

- [Code Overview](#code-overview)

- [Usage](#usage)

- [Features](#features)

- [Contact](#contact-information)

  

## Installation

Installing `dlib` and `face_recognition` can be challenging, so I wrote a blog for each library to explain the process in detail. Just click on the library names below to go to the respective blog posts:

- [Dlib](https://ahmed-saber.vercel.app/blogs/dlib-install)

- [Face recognition module](link)

- [gpiozero](link)

- [numpy](link)

- [openCV](link)

  

## Hardware Components

- Raspberry pi 5

- Servo motor

- Logic level converter 3.3v to 5v

- USB camera

  
  

## Code overview

Due to issues with the `gpiozero` library's servo implementation on Raspberry Pi 5, the servo control is manually handled using LED class [here](https://gist.github.com/Ahmed-Saber-Mohammed/59e9bdd5df5b0cfab5cef587f6c9406a).

  

## Usage

- **Set Up Database**: Add images of the faces you want to recognize in the Database directory.

- **Define Targeted Name**: Modify the script to include the targeted name you want the system to recognize and react to.

- **Run the Script**: Execute the script to start the real-time face recognition and servo control system.

  

## Features

-  **Facial Recognition**: Identifies authorized users based on pre-stored images.

-  **Servo Control**: Controls the servo motor to unlock the door.

-  **Real-Time Video Processing**: Processes video feed in real-time to detect faces.