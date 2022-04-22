import os
import pandas as pd

def combine_dsl():
    new_df = None
    for file in os.listdir("data/raw"):
        if file.endswith(".csv"):
            data = pd.read_csv(os.path.join('data/raw', file))
            if file == 'xkcd_mul_dsl.csv':
                data['dsl'] = data['dsl'].apply(update)

            if new_df is None:
                new_df = data
            else:
                new_df = new_df.append(data, ignore_index=True)
    new_df.to_csv(os.path.join('data', 'transfer_dsl_records.csv'), index=False)



combine_dsl()


