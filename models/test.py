import os
import json
import pandas as pd
from sacremoses import MosesTokenizer
import tqdm

def split_file(split):
    return os.path.join('splits', f'karpathy_{split}_images.txt')

def read_split_image_ids_and_paths(split):
    split_df = pd.read_csv(split_file(split), sep=' ', header=None)
    return split_df.iloc[:, 1].to_numpy(), split_df.iloc[:, 0].to_numpy()
def read_split_image_ids(split):
    return read_split_image_ids_and_paths(split)[0]
def select_captions(annotations, image_ids):
    """Select captions of given image_ids and return them with their image IDs.
    """
    # for fast lookup
    image_ids = set(image_ids)
    captions = []
    caption_image_ids = []
    for annotation in annotations:
        image_id = annotation['image_id']
        if image_id in image_ids:
            captions.append(annotation['caption'].replace('\n', ''))
            caption_image_ids.append(image_id)
    return captions, caption_image_ids
def tokenize_captions(captions, lang='en'):
    """Tokenizes captions list with Moses tokenizer.
    """
    return captions

def read_txt_file(file):
    with open(file, 'r') as f:
        content = f.readlines()
        content = [i.replace('\n', '') for i in content]
        content = [i for i in content if i != '']
    return content

def write_captions(captions, filename):
    with open(filename, 'w') as f:
        for caption in captions:
            f.write(caption + '\n')
def write_image_ids(image_ids, filename):
    with open(filename, 'w') as f:
        for image_id in image_ids:
            f.write(f'{image_id}\n')

if __name__ == '__main__':
    output_dir = 'data/fairseq_data'
    data_dir = 'data'
    os.makedirs(output_dir, exist_ok=True)
    splits = ['train', 'valid', 'test']

    for split in splits:

        captions = read_txt_file(os.path.join(data_dir, 'tgt_%s.txt'%split))
        caption_image_ids = read_txt_file(os.path.join(data_dir, 'src_%s.txt'%split))

        print('Tokenize captions ...')
        captions = tokenize_captions(tqdm.tqdm(captions))
        captions_filename = os.path.join(output_dir, f'{split}-captions.tok.en')
        caption_image_ids_filename = os.path.join(output_dir, f'{split}-ids.txt')
        write_image_ids(caption_image_ids, caption_image_ids_filename)
        write_captions(captions, captions_filename)
        print(f'Wrote tokenized captions to {captions_filename}.')


