1.1 Sequence (Sequence)			
	Private = False		
	Variables		
			
		input(DataTable)	
		ouput(DataTable)	
	Activities		
		1.2 Read CSV (ReadCsvFile)	
			FilePath = C:\Users\pkm14\OneDrive\Desktop\Excel format.csv
			DataTable = input
			Delimiter = Comma
			Has headers = True
			Private = False
		1.2 Filter Data Table (FilterDataTable)	
			DataTable = input
			SelectColumnsMode = Keep
			FilterRowsMode = Keep
			DataTable = ouput
			Private = False
		1.2 Write Range (WriteRange)	
			StartingCell = A1
			DataTable = ouput
			AddHeaders = False
			SheetName = Sheet1
			Workbook path = C:\Users\pkm14\OneDrive\Desktop\result1.xlsx
			Private = False
