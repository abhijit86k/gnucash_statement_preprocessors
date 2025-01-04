#!/usr/bin/python3
from http.client import ACCEPTED

import pandas as pd
import numpy as np
import sys
import argparse
import os

num_cmd_line_arguments = len(sys.argv) - 1
if num_cmd_line_arguments != 1:
    print('Incorrect Number of arguments.')
    exit(1)

input_filename = sys.argv[1]
#output_filename = os.path.splitext(filename) + '.processed.csv'
print("\n\n****************************************\n")
print("Opening File:\n" + input_filename)

# Check if the file is from SBI, else exit
try:
    pd.read_csv(input_filename, sep='\t', skiprows=6, nrows=1, header=None, engine='python')
except:
    print("Unable to open File")
    exit(1)

sbi_stmt = pd.read_csv(input_filename, sep='\t', skiprows=6, nrows=1, header=None, engine='python')
print('\nFile Open\n')

Account_Field = sbi_stmt[0]
if Account_Field[0].startswith("Account Number"):
    print("Looks like SBI File... Continuing import")
else:
    print("Not an SBI File")
    exit(1)


# Read Account Number
Account_Number = sbi_stmt[1][0]
print("\nProcessing for Account Number:\n"+Account_Number+"\n")

#create outputfile name
output_filename= os.path.splitext(input_filename)[0] + Account_Number + '.gc.csv'


sbi_stmt = pd.read_csv(input_filename, sep='\t', skiprows=20, skipfooter=2, engine='python')
sbi_stmt['Txn Date'] = pd.to_datetime(sbi_stmt['Txn Date'], format='%d %b %Y')
sbi_stmt['Value Date'] = pd.to_datetime(sbi_stmt['Value Date'], format='%d %b %Y')
sbi_stmt.columns.tolist()
sbi_stmt = sbi_stmt.rename(columns={'        Debit': 'Debit'})
sbi_stmt
sbi_stmt = sbi_stmt.drop(columns="Unnamed: 7", axis=1)
for col in sbi_stmt.columns[4:]:
    sbi_stmt[col] = sbi_stmt[col].str.replace(',', '')
    sbi_stmt[col] = pd.to_numeric(sbi_stmt[col], errors='coerce')

#Add a column to map all transactions to a default Imbalance Account
sbi_stmt['Transfer Account']='Imbalance-INR'

sbi_stmt = sbi_stmt.replace(np.nan, '', regex=True)
sbi_stmt.to_csv(output_filename, index=False)
print('Export Complete\n\nWritten to: ' + output_filename)