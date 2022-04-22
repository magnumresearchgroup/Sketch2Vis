from data_generator.xkcd_generator.XKCD_Plot import XKCD_Plot
from random import choice
from matplotlib import pyplot as plt
import os

class XKCD_Histo(XKCD_Plot):



    def assign_data(self):
        ran_gen = self.ran_gen

        data_len =  ran_gen.get_int(5, 20)


        self.data['bins'] = self.params['bins']
        self.data['density'] = self.params['density']
        self.data['cumulative'] = self.params['cumulative']
        self.data['histtype'] = self.params['histtype']
        self.data['align'] = self.params['align']
        self.data['orientation'] =self.params['orientation']
        # self.data['log'] = self.params['log']
        self.data['color'] = self.params['color']
        self.data['stacked'] = self.params['stacked']

        self.data['x'] = ran_gen.get_int_list(data_len)
        self.data['x_label'] = self.params['x_label']
        self.data['y_label'] = self.params['y_label']
        self.data['title'] = self.params['title']

    def plot(self, ax, plt):
        self.assign_params()
        self.assign_data()
        data = self.data
        font_name = self.ran_gen.get_random_hd_font()

        if choice([True, False]):
            ax.axis('off')

        ax.set_xticks([])
        ax.set_yticks([])

        ax.hist(x=data['x'],
                bins=data['bins'],
                density=data['density'],
                cumulative=data['cumulative'],
                histtype=data['histtype'],
                align=data['align'],
                orientation=data['orientation'],
                # log=data['log'],
                color=data['color'],
                stacked=data['stacked'],
                )

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())

        del data['x']
        del data['title']
        del data['x_label']
        del data['y_label']

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
                                      xytext=self.joggle_text_postion((0, 0.55)),
                                      textcoords='figure fraction',
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
        ax.set_xticks([])
        ax.set_yticks([])

        ax.hist(x = data['x'],
                bins = data['bins'],
                density = data['density'],
                cumulative = data['cumulative'],
                histtype = data['histtype'],
                align=data['align'],
                orientation=data['orientation'],
                # log=data['log'],
                color=data['color'],
                stacked=data['stacked'],
                )

        img_name, img_save_path = self.get_image_path(index)

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())

        self.dsl_list['path'].append(img_name)
        self.dsl_list['dsl'].append(dsl)

        del data['x']
        del data['title']
        del data['x_label']
        del data['y_label']

        self.meta[img_name] = data
        plt.savefig(img_save_path, quality=30)
        plt.close()
