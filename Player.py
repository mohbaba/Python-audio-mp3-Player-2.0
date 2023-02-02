import flet
from flet import *


def main(page: Page):
    page.title = "Audio Player"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
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