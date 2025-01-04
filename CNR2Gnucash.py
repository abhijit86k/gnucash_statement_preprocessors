#!/usr/bin/python3

import pandas as pd
import numpy as np
import sys
import argparse
import os
import xlrd
import io

num_cmd_line_arguments = len(sys.argv) - 1
if num_cmd_line_arguments != 1:
    print('Incorrect Number of arguments.')
    exit(1)

filename = sys.argv[1]
#type(filename)
#output_filename = os.path.splitext(filename) + '.processed.csv'
#print(input_filename)
#create outputfile name
output_filename= os.path.splitext(filename)[0] + '.gc.csv'


# Check if the file is from Canara, else exit
with open(filename, 'r') as file:
    content = file.read()
content = content.replace('=', '')
#content = content.replace('"','')


#Customer ID Check
Canara_stmt = pd.read_csv(io.StringIO(content), sep = ',', skiprows = 13, nrows = 1, header=None , engine = 'python')
customer_ID = Canara_stmt[1][0]

Canara_stmt = pd.read_csv(io.StringIO(content), sep = ',', skiprows = 18, nrows = 1, header=None , engine = 'python')

#account_number = Canara_stmt[1][0][2:-1].rstrip()
account_number = Canara_stmt[1][0]
type(account_number)

print('CustomerID='+ str(customer_ID)+' and A/C No='+str(account_number))
if input('Proceed? (y/n): ')=='y':
    pass
else:
    print('Exiting')
    exit(1)




#with open('ProcessedCanara.csv','w')  as file:
#    file.write(content)


Canara_stmt = pd.read_csv(io.StringIO(content),        sep = ',',  skiprows = 25, engine = 'python')


#
Canara_stmt['Txn Date'] = pd.to_datetime(Canara_stmt['Value Date'], format = '%d %b %Y')

Canara_stmt['Value Date'] = Canara_stmt['Txn Date']

last_column = Canara_stmt.columns.tolist()[-1]
if last_column == 'Unnamed: 8':
    Canara_stmt=Canara_stmt.drop(columns = last_column, axis = 1)

for col in Canara_stmt.columns[-4:]:
    Canara_stmt[col] = Canara_stmt[col].astype(str)
    Canara_stmt[col] = Canara_stmt[col].str.replace(',', '')
    Canara_stmt[col] = pd.to_numeric(Canara_stmt[col], errors = 'coerce')


# In[17]:


Canara_stmt = Canara_stmt.replace(np.nan, '', regex=True)


#Add a column to map all transactions to a default Imbalance Account
Canara_stmt['Transfer Account']='Imbalance-INR'

Canara_stmt.to_csv(output_filename, index=False)
print('Export Complete to' + output_filename)
