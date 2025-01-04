# gnucash_statement_preprocessors
Scripts to Translate Bank statements to CSVs suitable for Gnucash

## Setup:
1. Clone this repository using 'git clone' OR download the both python scripts to a directory on your machine, and make sure both are executable.
2. Add this location to PATH
3. Copy the following snippets into the file ```~/.local/share/gnucash/books/<BOOKNAME>.gcm```


		[Import csv,transaction - SBI-Savings-Import]
		Name=SBI-Savings-Import
		SkipStartLines=1
		SkipEndLines=0
		SkipAltLines=false
		CsvFormat=true
		Separators=,
		DateFormat=0
		CurrencyFormat=0
		Encoding=UTF-8
		MultiSplit=false
		BaseAccountGuid=47df840124fb49aab1ef379f6b17433b
		BaseAccount=Assets:CheckingAccountSBI
		ColumnTypes=None;Date;Description;Notes;Withdrawal;Deposit;None;Transfer Account;```



		[Import csv,transaction - Canara-Savings-Import]
		Name=Canara-Savings-Import
		SkipStartLines=1
		SkipEndLines=0
		SkipAltLines=false
		CsvFormat=true
		Separators=,
		DateFormat=0
		CurrencyFormat=0
		Encoding=UTF-8
		MultiSplit=false
		BaseAccountGuid=3d010b81e0544b51a1487bb92ffb3298
		BaseAccount=Assets:CheckingAccountCanara
		ColumnTypes=None;Date;Num;Description;None;Withdrawal;Deposit;None;Transfer Account;


## Usage

1. SBI:
	- Download statements as Spreadsheet (XLS) from Online SBI Website. The downloaded file has the extension of XLS (but is actually a CSV file)
	- Run ```SBI2Gnucash.py <FILENAME>.xls```
	- This will generate a file <FILENAME>.gc.csv which is suitable for gnucash to digest
	- Open Gnucash, select File>Import>Transactions from CSV.
		1. "Select File for Import" Make sure that file name you select should end in .gc.csv
		2. "Import Preview": Underload and save settings there should be template named SBI-Import-Setting. Make sure to set the Source account correctly. This should be the account for which you have downloaded the statement.
		4. "Match Import and Gnucash Accounts": You can set the destination to "Imbalance"
	- Finish the import; then go into the Imbalance Account and assign destination accounts to each transaction
2. Canara Bank:
	- Download the statement in CSV format from the Online Banking Interface
	- Run ```CNR2Gnucash <FILENAME>.CSV``` which will produce <FILENAME>.gc.csv
	- Follow the same procedure as above, but use the save/load Template CanaraImport in step 2.

## Caveats:
If there are no transactions the script fails in a non-elegant way.
99% of issues can be diagnosed by looking at the source XLS or CSV. 


