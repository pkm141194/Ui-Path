1.1 Sequence (Sequence)							
	Private = False						
	Variables						
		ExcelData(DataTable)					
	Activities						
		1.2 Read Range (ReadRange)					
			DataTable = ExcelData				
			AddHeaders = True				
			PreserveFormat = False				
			Workbook path = C:\Users\pkm14\OneDrive\Desktop\result1.xlsx				
			SheetName = Sheet2				
			Private = False				
		1.2 For Each Row in Data Table (ForEachRow)					
			DataTable = ExcelData				
			Private = False				
			Body				
				1.3 Body (Sequence)			
					Private = False		
					Variables		
						pwd(String)	
					Activities		
						1.13 Get Password (GetPassword)	
							Password = AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAjqxsXEzKKEefSdZKU+bFzgAAAAACAAAAAAAQZgAAAAEAACAAAAAwQ/Fv9dxEL0VqEElr3vhZLhSyBLXYCn40mvA0pKy2QAAAAAAOgAAAAAIAACAAAAC33nhXrPZoiZqESH6cJztYjPfzRA75KYaxvgz8GF4vUyAAAACFx+PBr1E9qBvz0B20LGeNiH+Uw6r0nAo8yLqBFZiuUEAAAADQMcxDuyBCEowieZx0g2utVqF3PGmavgc/zwKD6kwRkKjB4SX6t4KKf9sFzLEPqAOmJI/irmAiDfihI6EqcPLA
							Result = pwd
							ResultType = System.String
							Private = False
						1.4 Send SMTP Mail Message (SendMail)	
							Email = rpa@xtremeonline.com.au
							Password = pwd
							Server = smtp.gmail.com
							Port = 587
							SecureConnection = Auto
							To = CurrentRow("Email").ToString
							Subject = CurrentRow("Subject").ToString
							Body = CurrentRow("Body").ToString
							IsBodyHtml = False
							Private = False
