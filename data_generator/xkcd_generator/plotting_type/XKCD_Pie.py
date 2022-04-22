from data_generator.xkcd_generator.XKCD_Plot import XKCD_Plot
from random import randint, choice
from matplotlib import pyplot as plt
import numpy as np
import os

class XKCD_Pie(XKCD_Plot):



    def assign_data(self):
        ran_gen = self.ran_gen

        self.data['pie_number'] = ran_gen.get_int(2, 5)
        self.data['sizes'] = ran_gen.get_int_list(self.data['pie_number'])
        self.data['startangle'] = ran_gen.get_int(0, 90)

        self.data['shadow'] = self.params['shadow']
        self.data['sketch'] = self.params['sketch']


        self.data['explode'] = [0 for _ in range(self.data['pie_number'])]
        self.data['radius'] = 1
        if self.params['explode']:
            self.data['explode'][randint(0, self.data['pie_number'] - 1)] = 0.2
        if self.params['ring']:
            self.data['radius'] = choice([0.3, 0.4, 0.5, 0.6, 0.7, 0.8])

    def plot(self, ax, plt):
        self.assign_params()
        self.assign_data()
        font_name = self.ran_gen.get_random_hd_font()
        data = self.data

        anotation_instances = []
        # ax.axis('equal')
        """
        From https://matplotlib.org/3.1.0/gallery/pie_and_polar_charts/pie_and_donut_labels.html
        """
        if data['sketch']:
            wedges, texts = ax.pie(data['sizes'], wedgeprops=dict(width=data['radius']), startangle=0, colors='w')
            edgecolor = choice(['b', 'k'])
            for w in wedges:
                w.set_linewidth(2)
                w.set_edgecolor(edgecolor)
        else:
            wedges, texts = ax.pie(data['sizes'], wedgeprops=dict(width=data['radius']), startangle=0)

        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="->"),
                  bbox=bbox_props, zorder=0, va="center")
        for i, p in enumerate(wedges):
            i += choice(range(0, len(wedges)))
            p = wedges[i]
            ang = (p.theta2 - p.theta1) / 2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})

            box_style = [
                'circle',
                'round',
                'round4',
                'roundtooth',
                'sawtooth',
                'square'
            ]
            anotation_instances.append(
                ax.annotate(self.params['column_name'], xy=(x, y), xytext=(1.35 * np.sign(x), 0.8 * y),
                            # horizontalalignment=horizontalalignment,
                            fontsize=choice([12, 15, 20, 25]),
                            fontname=font_name,
                            bbox=dict(boxstyle=choice(box_style), fc="w"),
                            )
            )
            break

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())
        del data['sizes']
        return data, dsl


    def plot_and_save(self, index):
        self.assign_params()
        self.assign_data()
        font_name = self.ran_gen.get_random_hd_font()
        data = self.data

        plt.xkcd()
        fig = plt.figure()
        ax = plt.axes()
        plt.tight_layout(pad=5)

        anotation_instances = []
        ax.axis('equal')
        """
        From https://matplotlib.org/3.1.0/gallery/pie_and_polar_charts/pie_and_donut_labels.html
        """
        if data['sketch']:
            wedges, texts = ax.pie(data['sizes'], wedgeprops=dict(width=data['radius']), startangle=0, colors='w')
            edgecolor = choice(['b', 'k'])
            for w in wedges:
                w.set_linewidth(2)
                w.set_edgecolor(edgecolor)
        else:
            wedges, texts = ax.pie(data['sizes'], wedgeprops=dict(width=data['radius']), startangle=0)

        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="->"),
                  bbox=bbox_props, zorder=0, va="center")
        for i, p in enumerate(wedges):
            i += choice(range(0, len(wedges)))
            p = wedges[i]
            ang = (p.theta2 - p.theta1) / 2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})

            box_style = [
                'circle',
                'round',
                'round4',
                'roundtooth',
                'sawtooth',
                'square'
            ]
            anotation_instances.append(
                ax.annotate(self.params['column_name'], xy=(x, y), xytext=(1.35 * np.sign(x), 0.8 * y),
                            # horizontalalignment=horizontalalignment,
                            fontsize=choice([12, 15, 20, 25]),
                            fontname=font_name,
                            bbox=dict(boxstyle=choice(box_style), fc="w"),
                            )
            )
            break
        img_name, img_save_path = self.get_image_path(index)

        plt.savefig(img_save_path, quality=30)

        dsl = self.generate_dsl().replace('\n', ' ').replace('\t', ' ')
        dsl = ' '.join(dsl.split())

        self.dsl_list['path'].append(img_name)
        self.dsl_list['dsl'].append(dsl)


        del data['sizes']

        self.meta[img_name] = data

        plt.close()
