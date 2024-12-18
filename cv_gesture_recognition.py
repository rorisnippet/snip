# -*- coding: utf-8 -*-
"""CV:Gesture Recognition

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ginEx-GQ8TroGuIZy2k2l49z08kNg1WT
"""

!pip install deepface

import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

def display_image(frame):
    """Display image using matplotlib"""
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(12, 8))
    plt.imshow(rgb_frame)
    plt.axis('off')
    plt.show()

def analyze_image(image_path):
    """Analyze emotions in an image"""
    try:
        # Read image
        frame = cv2.imread(image_path)
        if frame is None:
            print("Error: Image not found or unable to load.")
            return

        # Analyze using DeepFace
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # Draw rectangles and labels for each detected face
        for face in result:
            x = face['region']['x']
            y = face['region']['y']
            w = face['region']['w']
            h = face['region']['h']

            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Add emotion label
            emotion = face['dominant_emotion']
            cv2.putText(frame, emotion,
                       (x, y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX,
                       0.9,
                       (0, 255, 0),
                       2)

            # Print detailed emotion analysis
            print("\nEmotion Analysis:")
            emotions = face['emotion']
            for emotion, score in emotions.items():
                print(f"{emotion}: {score:.2f}%")

        # Display the result
        display_image(frame)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    """Interactive menu for emotion detection"""
    while True:
        print("\nEmotion Detection Menu:")
        print("1. Load and Analyze Image")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            image_path = input("Enter the path to the image file: ")
            analyze_image(image_path)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# For Jupyter Notebook usage:
if __name__ == "__main__":
    main()