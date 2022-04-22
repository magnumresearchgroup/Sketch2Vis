from data_generator.style_transfer_generator.XKCD_Plot import XKCD_Plot
from random import randint, choice
from matplotlib import pyplot as plt
import numpy as np
import os

class XKCD_Box(XKCD_Plot):
    def assign_data(self):
        ran_gen = self.ran_gen
        colors = "bgrcmyk"
        markers = [
            ".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s",
            "p", "P", "*", "h", "H", "+", "x", "X", "D", "d", "|", "_"
        ]

        spread = np.random.rand(50) * 100
        center = np.ones(25) * 50
        flier_high = np.random.rand(10) * 100 + 100
        flier_low = np.random.rand(10) * -100

        self.data['data'] = np.concatenate((spread, center, flier_high, flier_low))
        self.data['notch'] = ran_gen.get_choice([True, False])
        self.data['marker'] = markers[randint(0, len(markers) - 1)]
        self.data['markerfacecolor'] = colors[randint(0, len(colors) - 1)]
        self.data['showfliers'] = ran_gen.get_choice([True, False])

        self.data['vert'] = self.params['vert']

    def plot(self, ax, plt):
        self.assign_params()
        self.assign_data()
        data = self.data
        plt.xticks([])
        plt.yticks([])
        ax.axis('off')
        green_diamond = dict(markerfacecolor=data['markerfacecolor'], marker=data['marker'])
        ax.boxplot(data['data'], flierprops=green_diamond,
                   # notch=data['notch'],
                   #                showfliers=data['showfliers'],
                   vert=data['vert'])


        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())
        a = data.copy()
        # a['data'] = list(a['data'])
        del a['data']
        return a, dsl

    def plot_and_save(self, index):
        font_name = self.ran_gen.get_random_hd_font()
        self.assign_params()
        self.assign_data()
        data = self.data

        plt.xkcd()
        fig = plt.figure()
        ax = plt.axes()
        plt.tight_layout(pad=3)

        green_diamond = dict(markerfacecolor=data['markerfacecolor'], marker=data['marker'])
        box_instance = ax.boxplot(data['data'], flierprops=green_diamond, notch=data['notch'],
                                  showfliers=data['showfliers'], vert=data['vert'])
        plt.xticks([])
        plt.yticks([])

        def random_xy():
            return choice([(0.2, 0.5), (0.08, 0.55), (0.5, 0.28), (0.5, 0.14)])

        anotation_instances = []
        box_style = [
            'circle',
            'round',
            'round4',
            'roundtooth',
            'sawtooth',
            'square'
        ]

        xytext = self.joggle_text_postion(random_xy())
        anotation_instances.append(
            ax.annotate(self.params['column_name'],
                        xy=(0.5, 0.5),
                        xytext=xytext,
                        fontsize=choice([18, 20, 25, 30]),
                        fontname=font_name,
                        bbox=dict(boxstyle=choice(box_style), fc="w"),
                        )
        )

        img_name, img_save_path, transfer_img_name = self.get_image_path(index)

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())

        del data['data']

        self.dsl_list['path'].append(transfer_img_name)
        self.dsl_list['dsl'].append(dsl)
        self.meta[img_name] = data

        plt.savefig(img_save_path, quality=30)
        plt.close()
