import pandas as pd
from project import SetupData as sd

"""
    This class is used to setup the Forest data that will be used for processing.
"""


class Forest:

    def setup_data(self, filename, column_names):
        # Read in data file and turn into data structure

        data = pd.read_csv(filename,
                           sep=",",
                           header=0,
                           names=column_names)

        print(data)

        setup = sd.SetupData()
        for index, row in data.iterrows():
            month_num = setup.change_month(row[2])
            data.at[index, "month"] = month_num

            day_num = setup.change_day(row[3])
            data.at[index, "day"] = day_num

        # Normalize data on columns with appropriate values
        data = data.iloc[:, :]
        normalized = setup.normalize_data(data=data)



        # # Make categorical column a binary for the class we want to use
        # for index, row in iris.iterrows():
        #     if iris[target_class][index] == self.class_we_want:
        #         iris.at[index, target_class] = 1
        #     else:
        #         iris.at[index, target_class] = 0
        # # Get copy of data with columns that will be normalized
        # new_iris = iris[iris.columns[0:4]]
        # # Normalize data with sklearn MinMaxScaler
        # scaler = preprocessing.MinMaxScaler()
        # iris_scaled_data = scaler.fit_transform(new_iris)
        # # Remove "class" column for now since that column will not be normalized
        # self.iris_names.remove(target_class)
        # iris_scaled_data = pd.DataFrame(iris_scaled_data, columns=self.iris_names)
        # # Add "class" column back to our column list
        # self.iris_names.append(target_class)
        #
        # # Add "class" column into normalized data structure, then categorize it into integers
        # iris_scaled_data[target_class] = iris[[target_class]]
        #
        # # Get mean of each column that will help determine what binary value to turn each into
        # iris_means = iris_scaled_data.mean()
        #
        # # Make categorical column a binary for the class we want to use
        # for index, row in iris_scaled_data.iterrows():
        #     for column in self.iris_names:
        #         # If the data value is greater than the mean of the column, make it a 1
        #         if iris_scaled_data[column][index] > iris_means[column]:
        #             iris_scaled_data.at[index, column] = 1
        #         # Otherwise make it a 0 since it is less than the mean
        #         else:
        #             iris_scaled_data.at[index, column] = 0

        # Return one hot encoded data frame
        return normalized