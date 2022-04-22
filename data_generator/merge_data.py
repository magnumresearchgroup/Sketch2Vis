from os import listdir
from os.path import join
from constants import *
import pandas as pd


def merge_csv(data_dir, meta_dir, label_dir):
    merged_data = None


    for file in listdir(join(data_dir, meta_dir)):
        if file.endswith(".csv"):
            sub_data = pd.read_csv(join(data_dir, meta_dir, file))
            merged_data = sub_data if merged_data is None else merged_data.append(sub_data, ignore_index=True)
    merged_data.to_csv(join(data_dir,label_dir,DSL_FILE), index=False)
