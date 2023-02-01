import flet
from flet import *


def main(page: Page):
    page.title = "Audio Player"
    
    c = Container(
        width = 700,
        height= 700,
        gradient= LinearGradient(
            begin= alignment.bottom_center,
            end= alignment.top_center,
            colors= ["lightblue600", "lightblue900"],
        ),
        bgcolor="grey"
    )
    
    
    
    
    
    
    
    
    
    
    page.add (c)
    

flet.app(target=main, assets_dir="assets")