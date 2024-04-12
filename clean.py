import os
import dlib
import cv2
import numpy as np
from tqdm import tqdm

def get_lips(image_path):
    # Load the pre-trained face detector
    detector = dlib.get_frontal_face_detector()
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    if len(faces) == 0:
        # print('No face detected in image:', image_path)
        return False
    return True

def crop_lips(image_dir, target_dir, file_name):
    # Load the pre-trained face detector
    detector = dlib.get_frontal_face_detector()

    # Load the facial landmark predictor
    predictor = dlib.shape_predictor("./pretrained_model/shape_predictor_68_face_landmarks.dat")

    # Read the image
    image_path = image_dir + '/' + file_name
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
        # Separate x and y coordinates
        x_coords = [point[0] for point in lips]
        y_coords = [point[1] for point in lips]

        # Calculate the average x and y coordinates
        avg_x = np.mean(x_coords) + 5
        avg_y = np.mean(y_coords)

        # Create a mask for the lips
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.fillPoly(mask, [np.array(lips)], (255, 255, 255))
        
        # Compute average color of the lips
        average_color = cv2.mean(image, mask=mask)

        # Convert to integer BGR values
        average_color_bgr = (int(average_color[0]), int(average_color[1]), int(average_color[2]))

        # Create a new image filled with the average color
        color_image = np.full_like(image, average_color_bgr, dtype=np.uint8)

        # Draw the square on the image
        x1 = int(avg_x) - 64
        y1 = int(avg_y) - 32
        x2 = int(avg_x) + 64
        y2 = int(avg_y) + 32
        cropped_image = image[y1:y2, x1:x2]
        cv2.imwrite(target_dir + '/' + file_name, cropped_image)
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        # Or save the image
        # Draw the lips on the image
        # cv2.polylines(image, [np.array(lips)], isClosed=True, color=(0, 255, 0), thickness=2)
        # cv2.imwrite("./output_image_with_lips.jpg", image)
    return [y1,y2,x1,x2]

def clean_file(image_dir, attribute_path = None):
    if attribute_path is None:
        all_file_names = os.listdir(image_dir)
    else:
        all_file_names = [line.rstrip() for line in open(attribute_path, 'r')]
    clean_file_names = []
    for i, filename in enumerate(tqdm(all_file_names)):
        image_path = image_dir+'/'+filename
        if get_lips(image_path):
            clean_file_names.append(filename)
        else:
            print('Lips not detected in image:', image_path)
            os.remove(image_path)

    # Write clean filenames to the new attribute file makeup_clean.txt
    with open(image_dir+'clean.txt', 'w') as file:
        for filename in clean_file_names:
            file.write(filename + '\n')

def build_crop_data(attribute_path, image_dir, target_dir):
    all_file_names = [line.rstrip() for line in open(attribute_path, 'r')]
    crop_file_coordinate = {}
    for i, filename in enumerate(tqdm(all_file_names)):
        coordinate = crop_lips(image_dir, target_dir, filename)
        crop_file_coordinate[filename] = coordinate

    # Write coordinates to a text file
    with open('./data/mt/makeup_crop_coordinate.txt', 'w') as file:
        for filename, coordinate in crop_file_coordinate.items():
            file.write(f"{filename}: {coordinate}\n")

if __name__ == '__main__':
    # image_dir = './data/mt/images/makeup'
    # attribute_path = './data/mt/makeup_clean.txt'
    image_dir = '/Users/kuyuanhao/Documents/Crawl/face'
    clean_file(image_dir)

    # image_dir = './data/mt/images/makeup'
    # attribute_path = './data/mt/makeup_clean.txt'
    # target_dir = './data/mt/images/makeup_cropped'
    # build_crop_data(attribute_path, image_dir,target_dir)
    


             