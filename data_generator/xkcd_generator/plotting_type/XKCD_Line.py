from data_generator.xkcd_generator.XKCD_Plot import XKCD_Plot
from random import randint
from matplotlib import pyplot as plt
import os

class XKCD_Line(XKCD_Plot):

    def assign_data(self):
        for p in self.opt['text_params']:
            if p == 'x_label':
                self.data[self.params[p]] = sorted(self.ran_gen.get_int_list(10))
            elif p == 'y_label':
                self.data[self.params[p]] = self.ran_gen.get_int_list(10)

    def joggle_params(self):
        """
        Randomly remove some params
        :return:
        """
        joggling_params = ['title']
        for p in joggling_params:
            self.params[p] = self.params[p] if randint(0, 1) == 1 else None

    def plot(self, ax, plt):
        self.assign_params()
        self.assign_data()
        self.joggle_params()

        font_name = self.ran_gen.get_random_hd_font()
        params = self.params
        plt.xticks([])
        plt.yticks([])
        title_instance = ax.set_title(params['title'], fontsize=20, fontweight='bold', fontname=font_name) if params[
            'title'] else None
        ax.plot(params['x_label'], params['y_label'], '', data=self.data,
                color=params['line_color'], marker=params['line_marker'], linestyle=params['line_style'])
        plt.ylabel('')
        plt.xlabel('')

        legend_instance = ax.legend(params['line_legends'], fontsize=20, ) if self.params['is_line_legends'] else None
        if legend_instance:
            plt.setp(legend_instance.texts, family=font_name)

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())
        data = self.params
        del data['title']
        del data['x_label']
        del data['y_label']
        del data['line_legends']
        return data, dsl

    def plot_and_save(self, index):

        self.assign_params()
        self.assign_data()
        self.joggle_params()

        font_name = self.ran_gen.get_random_hd_font()

        params = self.params
        # Config plot
        plt.xkcd()
        fig = plt.figure()
        ax = plt.axes()
        plt.tight_layout(pad=5)

        # Create Line instance
        title_instance = ax.set_title(params['title'], fontsize=20, fontweight='bold', fontname=font_name) if params[
            'title'] else None
        ax.plot(params['x_label'], params['y_label'], '', data=self.data,
                color=params['line_color'], marker=params['line_marker'], linestyle=params['line_style'])
        plt.ylabel('')
        plt.xlabel('')

        legend_instance = ax.legend(params['line_legends'], fontsize=20, ) if self.params['is_line_legends'] else None
        if legend_instance:
            plt.setp(legend_instance.texts, family=font_name)
        plt.xticks([])
        plt.yticks([])
        y_label_pos = self.joggle_text_postion((0.08, 0.55))
        x_label_pos = self.joggle_text_postion((0.5, 0.14))
        ylabel_instance = ax.annotate(params['y_label'], xy=self.joggle_text_postion((0.13, 0.5)),
                                      xycoords='figure fraction', fontsize=20,
                                      fontweight='bold',
                                      fontname=font_name,
                                      xytext=y_label_pos, textcoords='figure fraction',
                                      arrowprops=dict(arrowstyle="->"),
                                      horizontalalignment='left',
                                      verticalalignment='bottom')

        xlabel_instance = ax.annotate(params['x_label'], xy=self.joggle_text_postion((0.5, 0.2)),
                                      xycoords='figure fraction', fontsize=20,
                                      fontweight='bold',
                                      fontname=font_name,
                                      xytext=x_label_pos, textcoords='figure fraction',
                                      arrowprops=dict(arrowstyle="->"),
                                      horizontalalignment='left',
                                      verticalalignment='bottom')

        img_name, img_save_path = self.get_image_path(index)

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())

        self.dsl_list['path'].append(img_name)
        self.dsl_list['dsl'].append(dsl)

        data = self.params
        del data['title']
        del data['x_label']
        del data['y_label']
        del data['line_legends']

        self.meta[img_name] = data
        plt.savefig(img_save_path, quality=30)
        plt.close()
