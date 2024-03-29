from textual.widgets import Static 

class Logo(Static):
	DEFAULT_CSS = """
	Logo {
		color: auto;		
	}
"""
	logo = """
	 ___
 ___/   \___    ____   ___  ____    _    
/   \   /   \  |  _ \ / _ \/ ___|  / \   
\___ ### ___/  | |_) | | | \___ \ / _ \  
/    ###    \  |  _ <| |_| |___) / ___ \ 
\___/   \___/  |_| \_\\___/|____/_/   \_\
    \___/      RETHINKING OS ABSTRACTIONS
"""

	def compose(self):
		print("logo", self.logo)
		yield Static(self.logo)

