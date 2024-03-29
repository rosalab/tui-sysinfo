from textual.widgets import Static
from textual.containers import Container

class Logo(Static):
	DEFAULT_CSS = """
	Logo {
		color: auto;
		max-width: 1fr;	
		align: right bottom;
		text-align: right;
		height: 100%;
	}
"""
	logo = r"""
           ___
       ___/   \___  
      /   \   /   \ 
      \___ ### ___/ 
      /    ###    \ 
      \___/   \___/ 
          \___/     
  ____   ___  ____    _    
 |  _ \ / _ \/ ___|  / \   
 | |_) | | | \___ \ / _ \  
 |  _ <| |_| |___) / ___ \ 
 |_| \_\\___/|____/_/   \_\
 RETHINKING OS ABSTRACTIONS
"""

	def compose(self):
		yield Static(self.logo)

