import pandas as pd
from sklearn.model_selection import train_test_split
from os.path import join
from constants import *
from pathlib import Path
import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dsl_file', type=str, default=join(OUTPUT_DIR,LABEL_DIR, DSL_FILE))
    parser.add_argument('--data_dir', type=str, default=DATA_DIR)
    parser.add_argument('--src_train', type=str, default=SRC_TRAIN)
    parser.add_argument('--src_val', type=str, default=SRC_VAL)
    parser.add_argument('--src_test', type=str, default=SRC_TEST)
    parser.add_argument('--tgt_train', type=str, default=TGT_TRAIN)
    parser.add_argument('--tgt_val', type=str, default=TGT_VAL)
    parser.add_argument('--tgt_test', type=str, default=TGT_TEST)


    return parser


def save_to_text(x, y, x_path, y_path):
    imgs, dsls = [], []
    for img, dsl in zip(x, y):
        imgs.append(img)
        dsls.append(' '.join(dsl.split()))
    with open(x_path, 'w') as f:
        for img in imgs:
            f.write(img)
            f.write('\n')
    with open(y_path, 'w') as f:
        for d in dsls:
            f.write(d)
            f.write('\n')
    print('Saved!')

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    Path(args.data_dir).mkdir(parents=True, exist_ok=True)

    print("Start to split data and save to txt file")

    data = pd.read_csv(args.dsl_file)

    print(' %d records in total '%(data.shape[0]))
    X, y = data['path'], data['dsl']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=RANDOM_STATE)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=RANDOM_STATE)

    print(' %d records in train ' % (X_train.shape[0]))
    print(' %d records in val ' % (X_val.shape[0]))
    print(' %d records in test ' % (X_test.shape[0]))


    save_to_text(X_train,
                 y_train,
                 join(args.data_dir, args.src_train),
                 join(args.data_dir, args.tgt_train))
    save_to_text(X_val,
                 y_val,
                 join(args.data_dir, args.src_val),
                 join(args.data_dir, args.tgt_val))
    save_to_text(X_test,
                 y_test,
                 join(args.data_dir, args.src_test),
                 join(args.data_dir, args.tgt_test))
    print('Finished.......')
    print('Start to process data in fairseq....')



