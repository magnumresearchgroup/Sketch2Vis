from matplotlib import pyplot as plt
import random
from random import randint
from data_generator.xkcd_generator.random_data_generator import RandomDataGenerator
import pandas as pd
import os
import json

class XKCD_Plot(object):
    def __init__(self, opt, output_dir, img_dir, meta_dir):
        self.ran_gen = RandomDataGenerator()
        self.output_dir = output_dir
        self.img_dir = img_dir
        self.meta_dir = meta_dir
        self.opt = opt
        self.params = {}
        self.data = {}
        self.dsl_list = {'path':[], 'dsl':[]}
        self.meta = {}
        assert 'save_dir' in opt
        assert 'cat_params' in opt
        assert 'text_params' in opt
        assert 'dsl_template' in opt
        assert 'meta_file' in opt
        assert 'dsl_file' in opt


    def joggle_text_postion(self, xy):
        """
        :param xy: Tuple of xy coordinate (0.2, 0.1)
        :return: Updated Annotation Instance
        """
        x, y = xy
        x += 0.01 * randint(0, 10)
        x -= 0.01 * randint(0, 10)
        y += 0.01 * randint(0, 10)
        y -= 0.01 * randint(0, 10)
        xy = (x, y)
        return xy

    def assign_params(self):
        self.params = {}
        for p in self.opt['cat_params']:
            self.params[p] = random.choice(self.opt['cat_params'][p])

        for p in self.opt['text_params']:
            random_text = ' '.join([self.ran_gen.get_random_string(length=randint(1,2))])
            if p == 'title':
                random_text = ' '.join([self.ran_gen.get_random_string(length=randint(2,4))])
            self.params[p] = random_text

    def assign_data(self):
        raise NotImplementedError()

    def generate_dsl(self):
        return self.opt['dsl_template'].format_map(self.params)

    def plot_and_save(self, index):
        raise NotImplementedError()


    def get_image_path(self, index, ):
        img_name =  '%s_%d.png' % (self.opt['img_prefix'], index)
        img_save_path = os.path.join(self.output_dir, self.img_dir, img_name)
        return img_name, img_save_path



    def save_meta_and_dsl(self):
        self.dsl_list['dsl'] = ['<plot> %s </plot>'%(d) for d in self.dsl_list['dsl']]

        data = pd.DataFrame.from_dict(self.dsl_list)

        data.to_csv( os.path.join(self.output_dir, self.meta_dir, self.opt['dsl_file']), index=False)

        with open(os.path.join(self.output_dir, self.meta_dir, self.opt['meta_file']), 'w', encoding='utf-8') as f:
            json.dump(self.meta, f, ensure_ascii=False, indent=4)



