# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 18:43:05 2018

@author: barday

The purpose of this script is to go through the log files that are generated during the Automated Karnak Testing and provide a quick summary of Pass/Fail results.
The script must be called in this format: Test_Results.py C:\\Users\\Demo_Path\\ """

import os
import sys
import time
import mmap

karnak_success = "setupcomplete: time to complete"
inOS_success = "SUCCESSFUL AWC INSTALL!!!"
karnak_total = "connect: time to complete"
inOS_total = ": opening modern"

path_provided = r'C:\Users\barday\Documents\WATT\2018_04_25\WindowsAddPrn'

folder = path_provided.split('\\')[-2]
test = path_provided.split('\\')[-1]

if test == "WindowsAddPrn":
    test = "Setup_inOS"
    keyword_success = inOS_success
    keyword_total = inOS_total
elif test == "Karnak-Auto":
    test = "Setup_Karnak"
    keyword_success = karnak_success
    keyword_total = karnak_total


'''Setting variable success equal to 0'''
success = 0
'''Setting variable total equal to 0'''
total = 0


for file in os.listdir(path_provided):
    
    with open( folder + "_" + test + "_Results.txt", "a") as result_file:
        if file.endswith(".log"):
            with open(path_provided + '\\'+ file, "r") as openfile:
                fileNowOpen = mmap.mmap(openfile.fileno(), 0, access=mmap.ACCESS_READ)
                if fileNowOpen.find(keyword_total) != -1:
                    total += 1
                if fileNowOpen.find(keyword_success) != -1:
                    success += 1
                    result_file.writelines(file + '     1 \n')
                elif fileNowOpen.find(keyword_success) == -1:
                    result_file.writelines(file + '     0 \n')

