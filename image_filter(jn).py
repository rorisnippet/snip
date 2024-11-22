# -*- coding: utf-8 -*-
"""image_filter(JN)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1elVG5YFhh1YivNbABcRkNf55Qn1SnXf_
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

class ImageFilterApp:

    def __init__(self, image_path):
        self.image = cv2.imread('/content/7d2f7975-e0c1c5a7.jpg',0)
        if self.image is None:
            raise ValueError(f"Error: Could not load the image.")
        self.filtered_image = None

    def show_images(self, title1, image1, title2, image2):
        plt.subplot(121)
        plt.title(title1)
        plt.imshow(image1)
        plt.axis('off')

        plt.subplot(122)
        plt.title(title2)
        plt.imshow(image2)
        plt.axis('off')

        plt.show(block=False)
        plt.pause(3)
        plt.close()


    def apply_median_filter(self, kernel_size):
        self.filtered_image = cv2.medianBlur(self.image, kernel_size)
        self.show_images("Original", self.image, "Median Filter", self.filtered_image)

    def apply_sobel_filter(self):
        sobelx = cv2.Sobel(self.image, cv2.CV_64F, 1, 0, ksize = 3)
        sobely = cv2.Sobel(self.image, cv2.CV_64F, 0, 1, ksize = 3)
        self.filtered_image = cv2.magnitude(sobelx, sobely)
        self.show_images("Original", self.image, "Sobel Filter", self.filtered_image)

    def apply_gaussian_filter(self, kernel_size, sigma):
        self.filtered_image = cv2.GaussianBlur(self.image, kernel_size, sigma)
        self.show_images("Original", self.image, "Gaussian Filter", self.filtered_image)

    def apply_averaging_filter(self, kernel_size):
        self.filtered_image = cv2.blur(self.image, kernel_size)
        self.show_images("Original", self.image, "Averaging Filter", self.filtered_image)


def menu():
    print("\nImage Filtering Application")
    print("1.Apply Median Filter")
    print("2.Apply Sobel FIlter")
    print("3.Apply Gaussian Filter")
    print("4.Apply Averaging Filter")
    print("5.Exit")

if __name__ == '__main__':

    image_path = "/content/7d2f7975-e0c1c5a7.jpg "

    try:
        app = ImageFilterApp(image_path)

        while True:
            menu()
            choice = input("Enter your choice:")
            if choice == '1':
               kernel_size = int(input("Enter the kernel size (odd number):"))
               app.apply_median_filter(kernel_size)

            elif choice == '2':
                app.apply_sobel_filter()

            elif choice == '3':
                kernel_size = int(input("Enter the kernel size (odd number):"))
                sigma = float(input("Enter the sigma value (eg. 0):"))
                app.apply_gaussian_filter((kernel_size, kernel_size), sigma)

            elif choice =='4':
                kernel_size = int(input("Enter the kernel size (odd number):"))
                app.apply_averaging_filter((kernel_size, kernel_size))

            elif choice == '5':
               print("Exiting...")
               break

            else:
               print("Invalid Choice")


    except ValueError as e:
            print(e)