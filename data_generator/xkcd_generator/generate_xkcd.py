from data_generator.xkcd_generator.plotting_type.XKCD_Bar import XKCD_Bar
from data_generator.xkcd_generator.plotting_type.XKCD_Line import XKCD_Line
from data_generator.xkcd_generator.plotting_type.XKCD_Pie import XKCD_Pie
from data_generator.xkcd_generator.plotting_type.XKCD_Box import XKCD_Box
from data_generator.xkcd_generator.plotting_type.XKCD_Scatter import XKCD_Scatter
from data_generator.xkcd_generator.plotting_type.XKCD_Multi import XKCD_Multi_Plot
from data_generator.xkcd_generator.opts import bar_opts, line_opts, pie_opts,box_opts, scatt_opts

from random import choices,randint

import warnings
warnings.filterwarnings("ignore")



def xkcd_generator(output_dir, img_dir, meta_dir, plot_number):



    bar_gen = XKCD_Bar(bar_opts, output_dir,img_dir, meta_dir)
    line_gen = XKCD_Line(line_opts,output_dir,img_dir, meta_dir)
    pie_gen = XKCD_Pie(pie_opts,output_dir, img_dir, meta_dir)
    box_gen = XKCD_Box(box_opts,output_dir, img_dir, meta_dir)
    scatt_gen = XKCD_Scatter(scatt_opts,output_dir, img_dir, meta_dir)
    multi_plot = XKCD_Multi_Plot(
        output_dir,
        img_dir,
        meta_dir
    )

    multi_types = ['bar', 'line', 'pie', 'box', 'scatt']

    for i in range(plot_number):
        bar_gen.plot_and_save(plot_number)
    bar_gen.save_meta_and_dsl()
    print('Create %d XKCD-style bar plot in ./%s xkcd'%(plot_number, output_dir))

    for i in range(4):
        line_gen.plot_and_save(plot_number)
    line_gen.save_meta_and_dsl()
    print('Create %d XKCD-style line plot in ./%s xkcd'%(plot_number, output_dir))

    for i in range(plot_number):
        pie_gen.plot_and_save(plot_number)
    pie_gen.save_meta_and_dsl()
    print('Create %d XKCD-style pie plot in ./%s xkcd'%(plot_number, output_dir))

    for i in range(plot_number):
        box_gen.plot_and_save(plot_number)
    box_gen.save_meta_and_dsl()
    print('Create %d XKCD-style box plot in ./%s xkcd'%(plot_number, output_dir))

    for i in range(plot_number):
        scatt_gen.plot_and_save(plot_number)
    scatt_gen.save_meta_and_dsl()
    print('Create %d XKCD-style scat plot in ./%s xkcd'%(plot_number, output_dir))


    for i in range(plot_number*5):
        multi_plot.plot_and_save(i, plotting_choice=choices(multi_types, k=randint(2,4)))
    multi_plot.save_meta_and_dsl()

    print('Create %d XKCD-style multi-plot in ./%s xkcd' % (plot_number, output_dir))

    print('Finished Data Generation. You can check raw data in %s'%(output_dir))