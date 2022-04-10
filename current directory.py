1.1 Sequence (Sequence)			
	Private = False		
	Variables		
		DirectoryPath(String)	
		splitfolder(String[])	
	Activities		
		1.2 Assign (Assign)	
			To = DirectoryPath
			Value = Environment.CurrentDirectory
			Private = False
		1.2 Message Box (MessageBox)	
			Content = DirectoryPath
			AutomaticallyCloseAfter = 00:00:00
			Private = False
		1.2 Assign (Assign)	
			To = splitfolder
			Value = DirectoryPath.Split("\"c)
			Private = False
		1.2 Message Box (MessageBox)	
			Content = String.Join(Environment.NewLine,splitfolder)
			AutomaticallyCloseAfter = 00:00:00
			Private = False
