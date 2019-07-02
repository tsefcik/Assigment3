from builtins import print
from project import Machine as m
from project import Ecoli as e
from project import Forest as f
from project import Segmentation as s
import sys

"""
This is the main driver class for Assignment#3.  @author: Tyler Sefcik
"""


class Main:

    # Machine setup and run
    def run_machine(self, filename, column_names, columns_to_drop):
        # Setup data
        machine = m.Machine()
        machine_data = machine.setup_data(filename=filename, column_names=column_names,
                                          columns_to_drop=columns_to_drop)

        return machine_data

    # Ecoli setup and run
    def run_ecoli(self, filename, column_names, columns_to_drop):
        # Setup data
        ecoli = e.Ecoli()
        ecoli_data = ecoli.setup_data(filename=filename, column_names=column_names,
                                      columns_to_drop=columns_to_drop)

        return ecoli_data

    # Forest setup and run
    def run_forest(self, filename, column_names):
        # Setup data
        forest = f.Forest()
        forest_data = forest.setup_data(filename=filename, column_names=column_names)

        return forest_data

    # Segmentation setup and run
    def run_seg(self, filename, column_names):
        # Setup data
        seg = s.Segmentation()
        seg_data = seg.setup_data(filename=filename, column_names=column_names)

        return seg_data

    # Main driver to run all algorithms on each dataset
    def main(self):
        # Print all output to file
        # Comment out for printing in console
        # sys.stdout = open("./Assignment3Output.txt", "w")

        ##### Machine #####
        machine_names = ["vendor name", "model name", "cycle time", "min main mem", "max main mem", "cache mem",
                     "min channels", "max channels", "pub rel perf", "erp"]
        columns_to_drop = ["model name", "erp"]
        machine_data = self.run_machine(filename="data/machine.data", column_names=machine_names,
                               columns_to_drop=columns_to_drop)

        print("Machine data: ")
        print(machine_data)
        print()

        ##### Ecoli #####
        ecoli_names = ["seq name", "mcg", "gvh", "lip", "chg", "aac", "alm1", "alm2", "class"]
        ecoli_columns_to_drop = ["seq name"]
        ecoli_data = self.run_ecoli(filename="data/ecoli.data", column_names=ecoli_names,
                                    columns_to_drop=ecoli_columns_to_drop)

        print("Ecoli data: ")
        print(ecoli_data)
        print()

        ##### Forest #####
        forest_names = ["X", "Y", "month", "day", "FFMC", "DMC", "DC", "ISI", "temp", "RH", "wind", "rain", "area"]
        forest_data = self.run_forest(filename="data/forestfires.data", column_names=forest_names)

        print("Forest data: ")
        print(forest_data)
        print()

        ##### Segmentation #####
        seg_names = ["class", "cen col", "cen row", "pix count", "sld -5", "sld -2", "vedge mean", "vedge sd",
                     "hedge mean", "hedge sd", "intensity mean", "rawred mean", "rawblue mean", "rawgreen mean",
                     "exred mean", "exblue mean", "exgreen mean", "value mean", "sat mean", "hue mean"]
        seg_data = self.run_seg(filename="data/segmentation.data", column_names=seg_names)

        print("Segmentation data: ")
        print(seg_data)
        print()


if __name__ == "__main__":
    main = Main()
    main.main()
