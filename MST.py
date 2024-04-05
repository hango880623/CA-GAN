import numpy as np
import math
import pandas as pd
from skimage.color import rgb2lab
import matplotlib.pyplot as plt

def find_nearest_color(input_color_lab, target_colors_lab):
    min_distance = float('inf')
    nearest_color_index = None
    for i, target_color_lab in enumerate(target_colors_lab):
        distance = color_distance(input_color_lab, target_color_lab.tolist())
        if distance < min_distance:
            min_distance = distance
            nearest_color_index = i
    
    return nearest_color_index, target_colors_lab[nearest_color_index]

def color_distance(color1, color2):
    color1 = [int(x) for x in color1.strip('[]').split(',')]
    l1, a1, b1 = int(color1[0]), int(color1[1]), int(color1[2])
    l2, a2, b2 = color2
    return math.sqrt((l2 - l1)**2 + (a2 - a1)**2 + (b2 - b1)**2)

def add_monk_skin_tone(df):
    # Create a new column to store the nearest Monk skin tone name
    df['Monk_Skin_Tone'] = ''

    target_colors_lab = [skin_tone['rgb'] for skin_tone in monk_skin_tones.values()]
    target_colors_lab = [rgb2lab([x / 255. for x in color]) for color in target_colors_lab]
    
    # Find nearest Monk skin tone for each row
    for index, row in df.iterrows():
        input_skin_color = row['Skin_Color']
        print(input_skin_color)
        nearest_monk_index, nearest_monk_color_lab = find_nearest_color(input_skin_color, target_colors_lab)
        nearest_monk_name = list(monk_skin_tones.keys())[nearest_monk_index]
        df.at[index, 'Monk_Skin_Tone'] = nearest_monk_name
        print(f"Nearest Monk skin tone for row {index + 1}: {nearest_monk_name}")
    df.to_csv('./data/mt/train_class.csv', index=False)
def show_monk_skin_tone_distribution(df):
    skin_tone_counts = df['Monk_Skin_Tone'].value_counts()
    print(skin_tone_counts)
    skin_tone_counts = skin_tone_counts.sort_index()
    # Create a bar plot
    plt.figure(figsize=(10, 6))
    skin_tone_counts.plot(kind='bar', color='skyblue')
    plt.title('Occurrences of Monk Skin Tones')
    plt.xlabel('Monk Skin Tone')
    plt.ylabel('Occurrences')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    train_file ="data/mt/train_class.csv"
    df = pd.read_csv(train_file)
    
    monk_skin_tones = {
        "Monk 01": {"hex": "#f6ede4", "rgb": [246, 237, 228]},
        "Monk 02": {"hex": "#f3e7db", "rgb": [243, 231, 219]},
        "Monk 03": {"hex": "#f7ead0", "rgb": [247, 234, 208]},
        "Monk 04": {"hex": "#eadaba", "rgb": [234, 218, 186]},
        "Monk 05": {"hex": "#d7bd96", "rgb": [215, 189, 150]},
        "Monk 06": {"hex": "#a07e56", "rgb": [160, 126, 86]},
        "Monk 07": {"hex": "#825c43", "rgb": [130, 92, 67]},
        "Monk 08": {"hex": "#604134", "rgb": [96, 65, 52]},
        "Monk 09": {"hex": "#3a312a", "rgb": [58, 49, 42]},
        "Monk 10": {"hex": "#292420", "rgb": [41, 36, 32]}
    }
    show_monk_skin_tone_distribution(df)
    

    
