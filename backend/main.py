import Millennium # type: ignore

from win32.colors import get_accent_color
from api.themes_store import find_all_themes
from api.user_data import get_conditionals

class Plugin:
    # if steam reloads, i.e. from a new theme being selected, or for other reasons, this is called. 
    # with the above said, that means this may be called more than once within your backends lifespan 
    def _front_end_loaded(self):
        print("loaded millennium frontend")

    def _load(self):     
        # This code is executed when your plugin loads. 
        # notes: thread safe, running for entire lifespan of millennium
        print(f"loaded pluginidk with millennium v{Millennium.version()}")

    def _unload(self):
        print("unloading")
