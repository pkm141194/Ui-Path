1.1 Sequence1 (Sequence)															
	Private = False														
	Variables														
		token(String[])													
		currencyTable(DataTable)													
		StatusCode(Int32)													
		ResponceCode(String)													
	Activities														
		1.6 Assign (Assign)													
			To = token												
			Value = {"inr","krw","kwd","mmk","myr"}												
			Private = False												
		1.2 Build Data Table (BuildDataTable)													
			DataTable = currencyTable												
			Private = False												
		1.2 HTTP Request (HttpClient)													
			EndPoint = https://api.coingecko.com/api/v3/exchange_rates												
			Method = GET												
			AcceptFormat = ANY												
			BodyFormat = application/xml												
			Timeout (milliseconds) = 6000												
			Enable SSL certificate verification = True												
			Result = ResponceCode												
			StatusCode = StatusCode												
			Private = False												
		1.2 If (If)													
			Condition = StatusCode = 200												
			Private = False												
			Then												
				1.4 Sequence (Sequence)											
					Private = False										
					Variables										
						JsonObject(JObject)									
					Activities										
						1.10 Deserialize JSON (DeserializeJson<JObject>)									
							JsonString = ResponceCode								
							JsonObject = JsonObject								
							Private = False								
							TypeArgument = Newtonsoft.Json.Linq.JObject								
						1.10 For Each (ForEach<JObject>)									
							Values = JsonObject.SelectTokens("rates")								
							Private = False								
							TypeArgument = Newtonsoft.Json.Linq.JObject								
							Body								
								1.11 Body (Sequence)							
									Private = False						
									Activities						
										1.12 For Each (ForEach<String>)					
											Values = token				
											Private = False				
											TypeArgument = System.String				
											Body				
												1.13 Body (Sequence)			
													Private = False		
													Activities		
														1.14 Add Data Row (AddDataRow)	
															DataTable = currencyTable
															ArrayRow = {item,JObject(item)("name").ToString,JObject(item)("unit").ToString,JObject(item)("value").ToString,JObject(item)("type").ToString}
															Private = False
						1.10 Write Range (WriteRange)									
							StartingCell = A1								
							DataTable = currencyTable								
							AddHeaders = False								
							SheetName = Sheet1								
							Workbook path = C:\Users\pkm14\OneDrive\Desktop\result1.xlsx								
							Private = False								
			Else												
				1.3 Sequence (Sequence)											
					Private = False										
					Activities										
						1.6 Write Line (WriteLine)									
							Text = "something wrong" + StatusCode.ToString								
							Private = False								

