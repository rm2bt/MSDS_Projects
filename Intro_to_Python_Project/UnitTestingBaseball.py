# Examining Baseball Trends Through the Recent Decades
# Michael Kastanowski, Rehan Merchant, Matthew Nicklas, Drake Wagner
# Unit Testing for Baseball data

import requests
import csv
from numpy import *
import pandas as pd

bat_df = pd.read_csv("Salary_Batting.txt") #import batting
pitch_df = pd.read_csv("Salary_Pitching.txt") #import pitching

#Unit test to see if the column names changed correctly when organizing the data 
import unittest

class DataCleaningTestCase(unittest.TestCase): # inherit from unittest.TestCase
    
    def test_is_column_lengths_working_properly_batting_data(self):
      
        #old_names = ['playerID', 'yearID',  'teamID', 'lgID', 'R', 'H', '2B', '3B', 'HR', 'salary']
        old_names = ['playerID','yearID','stint','teamID','lgID','G','AB','R','H','2B','3B','HR','RBI',
                     'SB','CS','BB','SO','IBB','HBP','SH','SF','GIDP']
        
        # Test to see that the columns with the unused data were removed from the data set 
        self.assertNotEqual(len(bat_df.columns), len(old_names))
        
    def test_is_column_lengths_working_properly_pitching_data(self):
      
        #List with the original data headers to compare to shorter headers
        old_names2 = ['playerID','yearID','stint','teamID','lgID','W','L','G','GS','CG','SHO','SV','IPouts', 'H','ER', 'HR',
                      'BB','SO','BAOpp','ERA','IBB','WP', 'HBP','BK','BFP','GF','R','SH','SF','GIDP']
        
        # Test to see that the columns with the unused data were removed from the data set 
        self.assertNotEqual(len(pitch_df.columns), len(old_names2))
        
    def test_is_column_names_working_properly_pitching_data(self): #To make sure the name changes worked for pitching data
      
        #List with the original data headers to compare to shorter headers
        old_names3 = ['playerID', 'yearID',  'teamID', 'lgID', 'W', 'L' ,'R', 'H', 'ERA', 'salary']
    
        # Test to see if the rename of the headers worked properly 
        self.assertNotEqual(pitch_df.columns.values.tolist(), old_names3)
        
    def test_is_column_names_working_properly_batting_data(self): #To make sure the name changes worked for batting data
      
        #List with the original data headers to compare to shorter headers
        old_names4 = ['playerID', 'yearID',  'teamID', 'lgID', 'R', 'H', '2B', '3B', 'HR', 'salary']
    
        # Test to see if the rename of the headers worked properly 
        self.assertNotEqual(bat_df.columns.values.tolist(), old_names4)
                     
if __name__ == '__main__':
    unittest.main()  