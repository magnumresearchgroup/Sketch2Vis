from data_generator.xkcd_generator.XKCD_Plot import XKCD_Plot
from random import randint, choice
from matplotlib import pyplot as plt
import numpy as np
import os

class XKCD_Scatter(XKCD_Plot):



    def assign_data(self):
        ran_gen = self.ran_gen

        data_len =  ran_gen.get_int(5, 20)


        self.data['marker'] = self.params['marker']
        self.data['color'] = self.params['color']
        self.data['edgecolors'] = self.params['edgecolors']

        self.data['title'] = self.params['title']

        N = randint(5,30)
        x = np.random.rand(N)
        y = np.random.rand(N)
        area = (30 * np.random.rand(N)) ** 2

        self.data['x'] = x
        self.data['y'] = y
        self.data['area'] = area

    def plot(self, ax, plt):
        self.assign_params()
        self.assign_data()
        data = self.data
        ax.scatter(self.data['x'],
                    self.data['y'],
                    s=self.data['area'],
                    c=self.data['color'],
                    marker=self.data['marker'],
                    edgecolors=self.params['edgecolors']
                    )

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())

        del data['x']
        del data['title']
        del data['y']
        del data['area']

        return data, dsl

    def plot_and_save(self, index):
        self.assign_params()
        self.assign_data()
        data = self.data
        font_name = self.ran_gen.get_random_hd_font()
        plt.figure(dpi=300)
        plt.xkcd()
        fig = plt.figure()
        ax = plt.axes()
        plt.tight_layout(pad=5)

        title_instance = ax.set_title(self.params['title'], fontname=font_name,
                                      fontsize=choice([12, 15, 20, 25]))



        plt.scatter(self.data['x'],
                    self.data['y'],
                    s=self.data['area'],
                    c=self.data['color'],
                    marker=self.data['marker'],
                    edgecolors=self.params['edgecolors']
                    )
        img_name, img_save_path = self.get_image_path(index)

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())

        self.dsl_list['path'].append(img_name)
        self.dsl_list['dsl'].append(dsl)

        del data['x']
        del data['title']
        del data['y']
        del data['area']

        self.meta[img_name] = data
        plt.savefig(img_save_path, quality=30)
        plt.close()
