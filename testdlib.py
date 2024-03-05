import dlib
import cv2
import numpy as np
import os

from torchvision import transforms as T
from data_loader import MT

def get_skin_color(image_path):
    # Load the pre-trained face detector
    detector = dlib.get_frontal_face_detector()

    # Load the facial landmark predictor
    predictor = dlib.shape_predictor("./pretrained_model/shape_predictor_68_face_landmarks.dat")

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)

    for face in faces:
        # Predict facial landmarks
        landmarks = predictor(gray, face)
        
        # Extract face points (usually landmarks 1-15)
        facepts = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(1, 16)]

        # Create a mask for the face
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.fillPoly(mask, [np.array(facepts)], (255, 255, 255))

        # Exclude lips region (landmarks 48-60)
        lips = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(48, 61)]
        cv2.fillPoly(mask, [np.array(lips)], (0, 0, 0))
        
        # Compute average color of the face
        average_color = cv2.mean(image, mask=mask)

        # Convert to integer BGR values
        average_color_bgr = (int(average_color[0]), int(average_color[1]), int(average_color[2]))

        print("Average RGB color of the skin:", average_color_bgr)

        # Create a new image filled with the average color
        color_image = np.full_like(image, average_color_bgr, dtype=np.uint8)
        cv2.imwrite("./rgb_color_skin.jpg", color_image)

        # Draw the face contour on the image
        cv2.polylines(image, [np.array(facepts)], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.polylines(image, [np.array(lips)], isClosed=True, color=(0, 255, 0), thickness=2)

        # Save the image
        cv2.imwrite("./output_image_with_face.jpg", image)
    if len(faces) == 0:
        print("No face detected")
        # Get the dimensions of the image
        height, width = image.shape[:2]

        # Calculate the size of the square
        square_size = min(height, width) // 5

        # Calculate the coordinates of the square
        top_left_x = (width - square_size) // 2
        top_left_y = (height - square_size) // 2 
        bottom_right_x = top_left_x + square_size
        bottom_right_y = top_left_y + square_size
        # Extract the region of interest (ROI) corresponding to the square area
        square_roi = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
        # Draw the square on the image
        cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)
        cv2.imwrite("./output_image_with_face.jpg", image)

        # Compute the mean color of the ROI
        average_color = cv2.mean(square_roi)
        # Convert to integer RGB values
        average_color_bgr = (int(average_color[0]), int(average_color[1]), int(average_color[2]))
        # Create a new image filled with the average color
        color_image = np.full_like(image, average_color_bgr, dtype=np.uint8)
        cv2.imwrite("./rgb_color_skin.jpg", color_image)
            
    print(average_color_bgr)
    return average_color_bgr


def get_lips_color(image_path):
    # Load the pre-trained face detector
    detector = dlib.get_frontal_face_detector()

    # Load the facial landmark predictor
    predictor = dlib.shape_predictor("./pretrained_model/shape_predictor_68_face_landmarks.dat")

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)
    for face in faces:
        # Predict facial landmarks
        landmarks = predictor(gray, face)

        # Extract lip points (usually landmarks 48-60)
        lips = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(48, 61)]
        
        # Create a mask for the lips
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(lips)], (255, 255, 255))
        
        # Compute average color of the lips
        average_color = cv2.mean(image, mask=mask)

        # Convert to integer BGR values
        average_color_bgr = (int(average_color[0]), int(average_color[1]), int(average_color[2]))

        print("Average BGR color of the lips:", average_color_bgr)

        # Create a new image filled with the average color
        color_image = np.full_like(image, average_color_bgr, dtype=np.uint8)
        cv2.imwrite("./rgb_color_lips.jpg", color_image)

        # Draw the lips on the image
        cv2.polylines(image, [np.array(lips)], isClosed=True, color=(0, 255, 0), thickness=2)

        # Or save the image
        cv2.imwrite("./output_image_with_lips.jpg", image)

    if len(faces) == 0:
        print("No face detected")
        # Get the dimensions of the image
        height, width = image.shape[:2]

        # Calculate the size of the square
        square_size = min(height, width) // 5

        # Calculate the coordinates of the square
        top_left_x = (width - square_size) // 2
        top_left_y = (height - square_size) // 2 + square_size
        bottom_right_x = top_left_x + square_size//2
        bottom_right_y = top_left_y + square_size//2
        # Extract the region of interest (ROI) corresponding to the square area
        square_roi = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
        # Draw the square on the image
        cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (0, 255, 0), 2)
        cv2.imwrite("./output_image_with_lips.jpg", image)

        # Compute the mean color of the ROI
        average_color = cv2.mean(square_roi)
        # Convert to integer RGB values
        average_color_bgr = (int(average_color[0]), int(average_color[1]), int(average_color[2]))
        # Create a new image filled with the average color
        color_image = np.full_like(image, average_color_bgr, dtype=np.uint8)
        cv2.imwrite("./rgb_color_lips.jpg", color_image)
            
    print(average_color_bgr)
    return average_color_bgr

def save_filenames_to_txt(path, txt_file):
    # Get the list of filenames in the specified directory
    filenames = os.listdir(path)

    # Write the filenames to the text file
    with open(txt_file, 'w') as file:
        for filename in filenames:
            file.write(filename + '\n')

def test_MT():
    # Create a dataset object
    transform = []
    transform.append(T.RandomHorizontalFlip())
    transform.append(T.CenterCrop(256))
    transform.append(T.Resize(128))
    transform.append(T.ToTensor())
    transform.append(T.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)))
    transform = T.Compose(transform)
    dataset = MT(image_dir="./mtdataset/images/makeup", attr_path="./mtdataset/makeuptest.txt",transform = transform,mode = "train")
                 
if __name__ == '__main__':
    get_lips_color("./mtdataset/images/makeup/vHX118.png")
    get_skin_color("./mtdataset/images/makeup/vHX118.png")
    # save_filenames_to_txt("./mtdataset/images/makeup", "./mtdataset/makeup.txt")
    # save_filenames_to_txt("./mtdataset/images/non-makeup", "./mtdataset/non-makeup.txt")
    test_MT()