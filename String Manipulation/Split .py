1.1 Sequence (Sequence)			
	Private = False		
	Variables		
		message(String)	
		output(String[])	
	Activities		
		1.2 Assign (Assign)	
			To = message
			Value = UIpath, RPA, Robotic process automation
			Private = False
		1.6 Assign (Assign)	
			To = output
			Value = message.Split(","c)
			Private = False
		1.6 Message Box (MessageBox)	
			Content = String.Join(Environment.NewLine,output)
			AutomaticallyCloseAfter = 00:00:00
			Private = False
