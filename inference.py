import os
import torch
import json
from fairseq import options, tasks, checkpoint_utils
from fairseq.data import encoders

import utils.data as data
from pathlib import Path
from os.path import join
from PIL import Image


IMG_DIR = 'raw_data/imgs'
OUTPUT_DIR = 'output'
OUTPUT_FILE = 'predictions.json'

def main(args):
    use_cuda = torch.cuda.is_available() and not args.cpu

    task = tasks.setup_task(args)
    captions_dict = task.target_dictionary

    models, _model_args = checkpoint_utils.load_model_ensemble([args.path], task=task)
    model = models[0]
    model.make_generation_fast_(
        beamable_mm_beam_size=None if args.no_beamable_mm else args.beam,
        need_attn=args.print_alignment,
    )

    if torch.cuda.is_available() and not args.cpu:
        model.cuda()

    generator = task.build_generator(models= models, args=args)
    tokenizer = encoders.build_tokenizer(args=args)
    bpe = encoders.build_bpe(args)

    def decode(x):
        if bpe is not None:
            x = bpe.decode(x)
        if tokenizer is not None:
            x = tokenizer.decode(x)
        return x

    transform = data.default_transform()

    with open(args.input) as f:
        sample_ids = [line.rstrip('\n') for line in f]

    preds = {}
    for sample_id in sample_ids:

        sample_path = os.path.join(IMG_DIR, sample_id)
        with Image.open(sample_path).convert('RGB') as img:
            img_tensor = transform(img).unsqueeze(0)

        src_tokens = torch.zeros(1, 0)

        if use_cuda:
            img_tensor = img_tensor.cuda()
            src_tokens = src_tokens.cuda()

        sample = {
            'net_input': {
                'src_tokens': src_tokens,
                'source': img_tensor,
            }
        }

        translations = task.inference_step(generator, models, sample)
        prediction = decode(captions_dict.string(translations[0][0]['tokens']))
        preds[sample_id] = prediction
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    with open(join(OUTPUT_DIR, OUTPUT_FILE), 'w') as f:
        json.dump(preds, f)

def cli_main():
    parser = options.get_generation_parser(interactive=True, default_task='captioning')
    args = options.parse_args_and_arch(parser)
    main(args)

if __name__ == '__main__':
    cli_main()
