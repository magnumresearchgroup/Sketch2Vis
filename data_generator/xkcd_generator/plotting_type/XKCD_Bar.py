from data_generator.xkcd_generator.XKCD_Plot import XKCD_Plot
from random import randint, choice
from matplotlib import pyplot as plt
import os



class XKCD_Bar(XKCD_Plot):
    def assign_data(self):
        ran_gen = self.ran_gen
        self.data = {}
        self.data['width'] = randint(0, 10) * 0.1 + 0.5
        self.data['color'] = self.params['color']
        self.data['edgecolor'] = self.params['edgecolor']
        self.data['linewidth'] = randint(0, 10) * 0.1
        self.data['bar_number'] = ran_gen.get_int(2, 5)
        self.data['x'] = ran_gen.get_random_string(self.data['bar_number'])
        self.data['height'] = ran_gen.get_int_list(self.data['bar_number'])
        self.data['bottom'] = ran_gen.get_int(0, 15)

        self.data['align'] = self.params['align']

        while self.params['x_label'] in self.data  or self.params['y_label'] in self.data or self.params['x_label']==self.params['y_label']:
            self.assign_params()

        self.data[self.params['x_label']] = self.data['x']
        self.data[self.params['y_label']] = self.data['height']


    def plot(self, ax, plt):
        self.assign_params()
        self.assign_data()
        ax.axis('off')
        data = self.data
        font_name = self.ran_gen.get_random_hd_font()

        plt.xticks([])
        plt.yticks([])
        ax.bar(range(len(data['height'])),
               data['height'],
               bottom=data['bottom'],
               tick_label="",
               width=data['width'],
               align=data['align'],
               linewidth=data['linewidth'],
               edgecolor=data['edgecolor'],
               color=data['color']
               )

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())
        del data['x']
        del data['height']
        del data[self.params['x_label']]
        del data[self.params['y_label']]
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
        plt.xticks([])
        plt.yticks([])
        ylabel_instance = ax.annotate(self.params['y_label'], xy=self.joggle_text_postion((0.2, 0.5)),
                                      xycoords='figure fraction',
                                      fontsize=choice([12, 15, 20, 25]),
                                      fontweight='bold',
                                      fontname=font_name,
                                      xytext=self.joggle_text_postion((0.08, 0.55)), textcoords='figure fraction',
                                      arrowprops=dict(arrowstyle="->"),
                                      horizontalalignment='left',
                                      verticalalignment='bottom')

        xlabel_instance = ax.annotate(self.params['x_label'], xy=self.joggle_text_postion((0.5, 0.28)),
                                      xycoords='figure fraction',
                                      fontsize=choice([12, 15, 20, 25]),
                                      fontweight='bold',
                                      fontname=font_name,
                                      xytext=self.joggle_text_postion((0.5, 0.14)), textcoords='figure fraction',
                                      arrowprops=dict(arrowstyle="->"),
                                      horizontalalignment='left',
                                      verticalalignment='bottom')

        ax.bar(range(len(data['height'])),
                       data['height'],
            # height=data[self.params['y_label']],
            #    x=data[self.params['x_label']],
               bottom=data['bottom'], tick_label="",
               width=data['width'],
               align=data['align'],
               linewidth=data['linewidth'],
               edgecolor=data['edgecolor'],
               color=data['color'])


        img_name, img_save_path = self.get_image_path(index)

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())

        self.dsl_list['path'].append(img_name)
        self.dsl_list['dsl'].append(dsl)

        del data['x']
        del data['height']
        del data[self.params['x_label']]
        del data[self.params['y_label']]

        self.meta[img_name] = data
        plt.savefig(img_save_path, quality=30)
        plt.close()
