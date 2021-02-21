from import_datasets_class import *


class CalculateGSD:
    def __init__(self, csv_file):
        """
        This class calculates the grain size distribution for each node .
        The class was written by Max.
        :param csv_file: File name of the csv-file to import
        """
        self.fractions = int()
        self.data_without_gsd = pd.DataFrame
        self.read_csv(csv_file)
        self.calculate_gsd()
        self.data_gsd = pd.DataFrame

    def read_csv(self, csv_file):
        self.data_without_gsd = pd.read_csv(csv_file)

    def calculate_gsd(self):
        data_gsd = self.data_without_gsd
        data_gsd.loc[:, "Sum1"] = data_gsd.loc[:, "Fraction1"]
        i = 2
        while True:
            data_gsd.loc[:, "Sum{0}".format(str(i))] = data_gsd.loc[:, "Sum{0}".format(str(i - 1))] \
                                                  + data_gsd.loc[:, "Fraction{0}".format(str(i))]
            i += 1
            if i > self.fractions:
                break
        self.data_gsd = data_gsd
