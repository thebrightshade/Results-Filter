# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 18:43:05 2018

@author: barday

The purpose of this script is to go through the log files that are generated during the Automated Karnak Testing and provide a quick summary of Pass/Fail results.
The script must be called in this format: Test_Results.py C:\Users\Demo_Path\ """

import os
import sys
import time


'''Keywords for inOS AWC testing and Karnak Setup testing, need to define arguments for these.'''
#keyword_success = "setupcomplete: time to complete"
keyword_success = "SUCCESSFUL AWC INSTALL!!!"
#keyword_total = "connect: time to complete"
keyword_total = ": opening modern"

'''We are defining our function result_filter, which is called upon the path that will be provided by the user as an argument,
we are calling that argument "path_provided".'''
def result_filter(path_provided):

    '''Setting variable success equal to 0'''
    success = 0
    '''Setting variable total equal to 0'''
    total = 0
    
    '''We are going through the directory and creating a list of files/folders 
    in the directory for which the path was provided by the user'''
    for file in os.listdir(path_provided):

        '''Filtering for files which end in .log extension and then opening those files and iterating through it line by line 
        and if the keyword which confirms that an install was attempted is found, value of "total" is increased by +1,
        if keyword confirming success is found, value for "success" is increased by +1'''
        if file.endswith(".log"):
            with open(path_provided + file, "r") as openfile:
                for line in openfile:
                    if keyword_total in line:
                        total += 1
                    if keyword_success in line:
                        success += 1
        
        
        else:
            '''If files or folders which do not end in .log extension are found, we skip them and continue'''
            continue
    
    '''We set the variable "Results" in the output format that we want, i.e. Pass: success/total and then we return the "Results" when our function is called.'''
    Results = ("Pass: " + str(success) + "/" + str(total))
    return Results


'''Defining the function write_results, which writes the results to a file named Results.txt'''
def write_results(Results):
    with open("Result.txt", "w") as result_file:
        result_file.write(Results)



'''This is the main function which will call above defined functions
Setting the variable "p" as the second argument that is the path provided by the user, the first being the name of the script
Calling the function result_filter on that argument (p) and assigning it to the variable r
Calling the function write_results on the variable r which will write the results which were returned by the result_filter'''
def main():
    p = sys.argv[1]
    print(p)
    time.sleep(5)
    r = result_filter(p)
    write_results(r)
    print (sys.argv)
    time.sleep(5)
    
if __name__ == "__main__":
    main()
