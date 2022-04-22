from data_generator.xkcd_generator.generate_xkcd import xkcd_generator
from data_generator.style_transfer_generator.generate_style_transfer_base import style_transfer_base_generator
from data_generator.merge_data import merge_csv
import argparse
from os.path import isfile, join
from pathlib import Path
from constants import *



photo_sketch_pretrain_files = ['checkpoints/PhotoSketch/pretrained/lastest_net_D.pth',
                  'checkpoints/PhotoSketch/pretrained/lastest_net_G.pth'
                  ]


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', type=str, default=TASK_MERGE)
    parser.add_argument('--plot_source', type=str, default=STYLE_TRANSFER)
    parser.add_argument('--output_dir', type=str, default=OUTPUT_DIR)
    parser.add_argument('--plot_number', type=int, default=200)

    return parser

def create_dir_str(args):
    # Create '/raw_data'
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    # Create '/raw_data/imgs'
    Path(join(args.output_dir, IMG_DIR)).mkdir(parents=True, exist_ok=True)
    # Create '/raw_data/meta'
    Path(join(args.output_dir, META_DIR)).mkdir(parents=True, exist_ok=True)
    # Create '/raw_data/label'
    Path(join(args.output_dir, LABEL_DIR)).mkdir(parents=True, exist_ok=True)
    Path(join(args.output_dir, STYLE_TRANSFER_TEMP_IMG_DIR)).mkdir(parents=True, exist_ok=True)

    # Create './checkpoints/PhotoSketch/pretrained/'
    Path('checkpoints/PhotoSketch/pretrained').mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    # Create output dir if not exists
    create_dir_str(args)

    if args.task == TASK_CREATE:
        if args.plot_source == XKCD:
            # Generate XKCD based images
            xkcd_generator(output_dir=args.output_dir,
                           img_dir = IMG_DIR,
                           meta_dir = META_DIR,
                           plot_number=args.plot_number,
                           )
        elif args.plot_source == STYLE_TRANSFER:
            # Generate XKCD based images and transfer them into based on PhotoSketch
            # Check if the pretrained model from PhotoSketch has been downloaded

            for file in photo_sketch_pretrain_files:
                if not isfile(file) :
                    print('Pretrained model for transferring style does not exist. Please follow the instructions')

            style_transfer_base_generator(output_dir=args.output_dir,
                                          img_dir=STYLE_TRANSFER_TEMP_IMG_DIR,
                                          meta_dir=META_DIR,
                                          plot_number=args.plot_number,
                                          )
            print('Base Image Created,Please run transfer_style.sh to transfer images you created')
            print('-------------------------****************-------------------------')
            print('CHECK dataDir AND OTHER PATH IN transfer_style.sh BEFORE YOU RUN IT!')
        elif args.plot_source == ROUGHVIZ:
            print('Please follow instructions in README to generate roughviz plots')
        else:
            print('UNSUPPORTED PLOTTING SOURCE.')
    elif args.task == TASK_MERGE:
        merge_csv(args.output_dir, META_DIR, LABEL_DIR)
    else:
        print('Unsupported task. Please check your input')






