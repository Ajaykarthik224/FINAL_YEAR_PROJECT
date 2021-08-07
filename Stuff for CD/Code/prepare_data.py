import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time


class prepare_data:

    def __init__(self, path):
        super().__init__()
        self.path_of_file = path

    def prepare(self):
        # Read the csv file with the rainfall data
        data = pd.read_csv(self.path_of_file)

        # Remove rows with missing data
        data = data.dropna(how="any", axis=0)
        data.cov()
        data.corr()

        # Classify annual rainfall of more than 3000mm as flood = True else False
        data['FLOOD'] = data.apply(
            lambda row: True if row['annual'] > 3000 else False, axis=1)

        # Convert the [True False] values to [1,0] for easy processing
        data['FLOOD'].replace([True, False], [1, 0], inplace=True)

        # Separate the concept values and the target values and return it
        x = data.iloc[:, 1:19]
        y = data.iloc[:, -1]
        # figManager = plt.get_current_fig_manager()
        # figManager.window.showMaximized()

        # Plotting the data in the graph

        # c = data[['jan', 'feb', 'mar', 'apr', 'may', 'jun',
        #           'jul', 'aug', 'sep', 'oct', 'nov', 'dec']].mean().plot.line()
        # # c.hist()
        # plt.xlabel('Month', fontsize=20)
        # plt.ylabel('Mean Rainfall in mm', fontsize=20)
        # plt.show()

        # time.sleep(5)
        # figManager = plt.get_current_fig_manager()
        # figManager.window.showMaximized()
        # ax = data[['jan', 'feb', 'mar', 'apr', 'may', 'jun',
        #            'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'jf', 'mam', 'jjas', 'ond']].mean().plot.bar(width=0.5, edgecolor='k', align='center', linewidth=2)
        # plt.xlabel('Month', fontsize=30)
        # plt.ylabel('Monthly Rainfall', fontsize=20)
        # plt.title('Rainfall in India for all Months', fontsize=25)
        # ax.tick_params(labelsize=20)
        # plt.grid()
        # plt.ioff()
        # plt.show()

        return [x, y]


prepare_data('data/data_in_csv.csv').prepare()
