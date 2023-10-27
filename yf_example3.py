""" yf_example3.py

Solution to Week 4 Code Challenge: Modules
"""

import os
import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    """ Download Qantas stock prices for a given year into a CSV file. The name of this file will be qan_prc_YYYY.csv,
    where the YYYY stands for the year in year.  This file will be saved under the data folder.
    Remember that the location of this folder is already in the toolkit_config module.

    Parameters
    ----------
    year : int
        An integer with a four-digit year
    """
    start = f"{year}-01-01"
    end = f"{year}-12-31"
    tic = "QAN.AX"

    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(
        tic=tic,
        pth=pth,
        start=start,
        end=end)


if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(year)
