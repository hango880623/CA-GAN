from clean import clean_file, build_crop_data
from MST import label_color, add_monk_skin_tone, show_monk_skin_tone_distribution
import pandas as pd

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

if __name__ == '__main__':
    # base_path = '/Users/kuyuanhao/Documents/LABImage/'
    # clean_file(base_path)
    # attr_path = base_path + 'clean.txt'

    # target_dir = '/Users/kuyuanhao/Documents/LABImage_cropped/'
    
    # build_crop_data(attr_path, base_path, target_dir)
    # image_dir = base_path
    # label_path = base_path + 'label.csv'

    # df = pd.read_csv(label_path)
    # save_dir = base_path + 'class.csv'
    # add_monk_skin_tone(df,save_dir)
    # show_monk_skin_tone_distribution(df)

    df1 = pd.read_csv('/Users/kuyuanhao/Documents/LABImage/class.csv')
    df2 = pd.read_csv('/Users/kuyuanhao/Documents/Customized/class.csv')
    merged_df = pd.concat([df1, df2], ignore_index=True)

    merged_df.to_csv('/Users/kuyuanhao/Documents/Data0421/class.csv', index=False)