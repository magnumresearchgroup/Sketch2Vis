from random import randint
from matplotlib import pyplot as plt
import pandas as pd
import os
import json
from data_generator.xkcd_generator.plotting_type.XKCD_Bar import XKCD_Bar
from data_generator.xkcd_generator.plotting_type.XKCD_Line import XKCD_Line
from data_generator.xkcd_generator.plotting_type.XKCD_Pie import XKCD_Pie
from data_generator.xkcd_generator.plotting_type.XKCD_Box import XKCD_Box
from data_generator.xkcd_generator.plotting_type.XKCD_Scatter import XKCD_Scatter
from data_generator.xkcd_generator.opts import bar_opts, line_opts, pie_opts,box_opts, scatt_opts

class XKCD_Multi_Plot():
    def __init__(self,
                 output_dir,
                 img_dir,
                 meta_dir,
                 dsl_file = 'xkcd_mul_dsl.csv',
                 meta_fle = 'xkcd_mul_meta.json',

                 ):
        self.gen_list = {
            'bar':  XKCD_Bar(bar_opts,output_dir, img_dir, meta_dir),
            'line':XKCD_Line(line_opts,output_dir, img_dir, meta_dir),
            'pie': XKCD_Pie(pie_opts,output_dir, img_dir, meta_dir),
            'box': XKCD_Box(box_opts,output_dir, img_dir, meta_dir),
            'scatt':XKCD_Scatter(scatt_opts,output_dir, img_dir, meta_dir),
        }
        self.dsl_list = {'path': [], 'dsl': []}
        self.meta = {}

        self.dsl_file = dsl_file
        self.meta_file = meta_fle
        self.output_dir = output_dir
        self.img_dir = img_dir
        self.meta_dir = meta_dir

    def get_image_path(self, index):
        img_name = 'xkcd_mul_%d.png' % (index)
        img_save_path = os.path.join(self.output_dir, self.img_dir, img_name)
        return img_name, img_save_path


    def plot_and_save(self, index, plotting_choice=None):
        assert plotting_choice is not None
        plot_num = len(plotting_choice)
        assert plot_num <= 4 and plot_num>1


        hor_num = randint(1, plot_num)
        ver_num = int(plot_num/hor_num + plot_num%hor_num)
        # TODO: THIS BLOCK IS USED TO AVOID A SPECIFIC CASE
        if hor_num ==3 and ver_num == 2:
            hor_num = 2
            ver_num = 2

        fig, axs = plt.subplots(hor_num, ver_num, figsize=(5*ver_num, 5*hor_num))
        plt.xkcd()
        img_name, img_save_path = self.get_image_path(index)


        self.dsl_list['path'].append(img_name)
        if img_name not in self.meta:
            self.meta[img_name] = []
        all_dsl = ''

        for i in range(len(plotting_choice)):
            plot_type = plotting_choice[i]
            h = int(i/ver_num)
            v = i%ver_num
            if len(axs.shape) == 1:
                ax = axs[i]
            else:
                ax = axs[h][v]
            #
            gen = self.gen_list[plot_type]
            meta, dsl = gen.plot(ax, plt)

            self.meta[img_name].append(meta.copy())
            all_dsl += ' ' + dsl

        if hor_num*ver_num>plot_num:
            if len(axs.shape) == 1:
                axs[-1].axis('off')
            else:
                axs[-1][-1].axis('off')
        self.dsl_list['dsl'].append(all_dsl)
        plt.savefig(img_save_path, quality=30)
        plt.close()

    def save_meta_and_dsl(self):
        #TODO: Everytime save to dsl, <plot> will be added into every dsl, rewrite this
        self.dsl_list['dsl'] = ['<plot> %s </plot>'%(d) for d in self.dsl_list['dsl']]
        data = pd.DataFrame.from_dict(self.dsl_list)
        data.to_csv(os.path.join(self.output_dir, self.meta_dir, self.dsl_file), index=False)

        with open(os.path.join(self.output_dir, self.meta_dir, self.meta_file), 'w', encoding='utf-8') as f:
            json.dump(self.meta, f, ensure_ascii=False, indent=4)





