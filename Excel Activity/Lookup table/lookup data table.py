1.1 Sequence (Sequence)							
	Private = False						
	Variables						
		DT1(DataTable)					
		Output(GenericValue)					
		DT2(DataTable)					
	Activities						
		1.2 Read Range (ReadRange)					
			DataTable = DT1				
			AddHeaders = True				
			PreserveFormat = False				
			Workbook path = cust1.xlsx				
			SheetName = Sheet1				
			Private = False				
		1.14 Read Range (ReadRange)					
			DataTable = DT2				
			AddHeaders = True				
			PreserveFormat = False				
			Workbook path = cust2.xlsx				
			SheetName = Sheet1				
			Private = False				
		1.14 For Each Row in Data Table (ForEachRow)					
			DataTable = DT1				
			Private = False				
			Body				
				1.15 Body (Sequence)			
					Private = False		
					Activities		
						1.2 Lookup Data Table (LookupDataTable)	
							DataTable = DT2
							LookupValue = row("Customer ID").ToString
							ColumnName = Customer ID
							ColumnName = Order No
							CellValue = Output
							Private = False
						1.8 Write Cell (WriteCell)	
							Cell = "D" +(DT1.Rows.IndexOf(row)+2).ToString
							Text = Output
							SheetName = Sheet1
							Workbook path = cust1.xlsx
							Private = False
