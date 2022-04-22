bar_opts = {
    'text_params':{
            'title': None,
            'x_label': None,
            'y_label': None,
    },
    'cat_params': {
            'align': ['center', 'edge'],
            'color': ['b','g','r','c','m','y','k'],
            'edgecolor': ['b','g','r','c','m','y','k','w']

    },
    'dsl_template':  """
                        <structure> 
                        <type> bar </type>
                           <align> {align} </align>
                           <color> {color} </color>
                           <edgecolor> {edgecolor} </edgecolor>
                        </structure>
                     """,
    'save_dir':'xkcd',
    'meta_dir': 'meta',
    'img_dir': 'imgs',
    'meta_file': 'xkcd_bar_meta.json',
    'dsl_file': 'xkcd_bar_dsl.csv',
'img_prefix': 'xkcd_bar',
}

line_opts = {
    'text_params': {
        'x_label': None,
        'y_label': None,
        'title': None,
        'line_legends':None
    },
    'cat_params': {
        'line_style': ['-', '--', '-.', ':', ''],
        'line_color': ['b', 'g', 'r', 'c', 'm', 'y', 'k'],
        'line_marker': [".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s",
                        "p", "P", "*", "h", "H", "+", "x", "X", "D", "d", "|", "_", None],
        'is_line_legends': [True, False]
    },
    'dsl_template': """
    
    <structure> 
                        <type> line </type>
                        <marker> 
                            {line_marker} 
                        </marker>
                        <linestyle>
                            {line_style}
                        </linestyle>
                        <is_line_legends>
                            {is_line_legends}
                        </is_line_legends>
                    </structure> 
                """,
    'save_dir': 'xkcd',
    'meta_dir': 'meta',
    'img_dir': 'imgs',
    'meta_file': 'xkcd_line_meta.json',
    'dsl_file': 'xkcd_line_dsl.csv',
    'img_prefix': 'xkcd_line',
}

pie_opts = {
    'text_params':{
            'column_name': None,
    },
    'cat_params': {
              'explode': [True, False],
            'ring': [True, False],
            'sketch':  [True, False],
            'shadow': [True, False],
    },
    'dsl_template': """
            <structure> 
                <type> pie </type>
                <explode> {explode} </explode>
                <ring> {ring} </ring>
                <sketch> {sketch} </sketch>
                <shadow> {shadow} </shadow>
            </structure>
            """,
    'save_dir':'xkcd',
    'meta_dir': 'meta',
    'img_dir': 'imgs',
    'meta_file': 'xkcd_pie_meta.json',
    'dsl_file': 'xkcd_pie_dsl.csv',
    'img_prefix': 'xkcd_pie',
}

box_opts = {
    'text_params':{
             'title': None,
            'column_name': None
    },
    'cat_params': {
            'vert': [True, False]
    },
    'dsl_template':  """
        <structure>
            <type> box </type>
            <vert> {vert} </vert>
        </structure>
        """,
    'save_dir':'xkcd',
    'meta_dir': 'meta',
    'img_dir': 'imgs',
    'meta_file': 'xkcd_box_meta.json',
    'dsl_file': 'xkcd_box_dsl.csv',
    'img_prefix': 'xkcd_box',
}

histo_opts = {
    'text_params':{
             'title': None,
            'x_label': None,
            'y_label': None
    },
    'cat_params': {
        'bins': ['auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', 'sqrt', None],
        'density': [True, False],
         'cumulative': [True, False],
         'histtype': ['bar', 'barstacked', 'step', 'stepfilled'],
         'align': ['left', 'mid', 'right'],
         'orientation': ['vertical', 'horizontal'],
         'color': ['b','g', 'r', 'c', 'm', 'y', 'k'],
         'stacked': [True, False],
    },
    'dsl_template':  """
        <structure> 
            <type> histo </type>
            <bins> {bins} </bins>
            <density> {density} </density>
            <cumulative> {cumulative} </cumulative>
            <histtype> {histtype} </histtype>
            <align> {align} </align>
            <orientation> {orientation} </orientation>
            <color> {color} </color>
            <stacked> {stacked} </stacked>
        </structure>
        """,
    'save_dir':'xkcd',
    'meta_dir': 'meta',
    'img_dir': 'imgs',
    'meta_file': 'xkcd_histo_meta.json',
    'dsl_file': 'xkcd_histo_dsl.csv',
    'img_prefix': 'xkcd_histo',
}

scatt_opts = {
    'text_params':{
            'title': None,
    },
    'cat_params': {
            'marker':[".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s",
                        "p", "P", "*", "h", "H", "+", "x", "X", "D", "d", "|", "_", None],
            'color': ['b','g', 'r', 'c', 'm', 'y', 'k'],
            'edgecolors': ['face', 'none', None]
    },
    'dsl_template':  """  
                        <structure> 
                            <type> scatt </type>
                           <marker> {marker} </marker>
                           <color> {color} </color>
                           <edgecolors> {edgecolors} </edgecolors>
                        </structure>
                     """,
    'save_dir':'xkcd',
    'meta_dir': 'meta',
    'img_dir': 'imgs',
    'meta_file': 'xkcd_scatt_meta.json',
    'dsl_file': 'xkcd_scatt_dsl.csv',
    'img_prefix': 'xkcd_scatt',
}
