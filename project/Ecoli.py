import pandas as pd
from project import SetupData as sd

"""
    This class is used to setup the Ecoli data that will be used for processing.
"""


class Ecoli:

    def setup_data(self, filename, column_names, columns_to_drop):
        # Read in data file and turn into data structure

        data = pd.read_csv(filename,
                           sep="\\s+",
                           header=0,
                           names=column_names)

        # Drop columns that we don't want to consider
        for name in columns_to_drop:
            data = data.drop(name, 1)

        # Normalize data on columns with appropriate values
        last_col = data.iloc[:, -1]
        data = data.iloc[:, 0:data.shape[1] - 1]
        setup = sd.SetupData()
        normalized = setup.normalize_data(data=data)
        normalized = normalized.join(last_col)

        return normalized
