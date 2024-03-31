from textual.widgets import Static, Label
from textual.app import ComposeResult


class Logo(Static):
	DEFAULT_CSS = """
	Logo {
		color: auto;
		align: center top;
		height: 100%;
		width: 100%;
		padding: 0 0 0 0;
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
""".rstrip()

	def compose(self) -> ComposeResult:
		yield Label(self.logo)

