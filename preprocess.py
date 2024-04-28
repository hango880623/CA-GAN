from clean import clean_file, build_crop_data
from MST import label_color, show_monk_skin_tone_distribution
import pandas as pd
import cv2
import os

from clean import clean_folder

def preprocess_folder(source_folder,target_folder):
    target_image_folder = target_folder + 'image/'
    if not os.path.exists(target_image_folder):
        os.makedirs(target_image_folder)
        print(f"Created directory: {target_image_folder}")

    attribute_list = clean_folder(source_folder+ 'image/')

    clean_file_names, dataset = label_color(attribute_list, source_folder+'image/')
    # Convert dataset list to pandas DataFrame
    df = pd.DataFrame(dataset, columns=['Filename', 'Lips_Color', 'Skin_Color', 'Lips_Color_RGB', 'Skin_Color_RGB', 'Monk_Skin_Tone', 'Monk_Skin_Tone_Color'])
    df.to_csv(os.path.join(target_folder, 'label.csv'), index=False)
    print('Dataset saved to', os.path.join(target_folder, 'label.csv'))

     # Write clean filenames to the new attribute file makeup_clean.txt
    with open(os.path.join(target_folder, 'clean.txt'), 'w') as file:
        for filename in clean_file_names:
            file.write(filename + '\n')
    
    show_monk_skin_tone_distribution(df,os.path.join(target_folder, 'monk.png'))


if __name__ == '__main__':
    base_dir = '/Users/kuyuanhao/Documents/Socialmedia/'
    target_dir = '/Users/kuyuanhao/Documents/Socialmedia/'
    preprocess_folder(base_dir,target_dir)
