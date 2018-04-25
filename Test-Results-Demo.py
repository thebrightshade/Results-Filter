# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 18:43:05 2018

@author: barday

The purpose of this script is to go through the log files that are generated during the Automated Karnak Testing and provide a quick summary of Pass/Fail results.
The script must be called in this format: Test_Results.py C:\\Users\\Demo_Path\\ """

import os
import sys
import time

path = r'C:\Users\barday\Documents\WATT\2018_04_25\WindowsAddPrn'

folder = path.split('\\')[-2]
test = path.split('\\')[-1]

if test == "WindowsAddPrn":
    test = "inOS_Setup"
elif test == "Karnak-Auto":
    test = "Karnak_Setup"

for file in os.listdir(path):
    with open( folder + "_" + test + "_Results.txt", "a") as result_file:
        result_file.writelines(file + '\n')