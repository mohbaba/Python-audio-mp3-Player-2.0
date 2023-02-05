import flet as ft
from flet import *


def main(page: Page):
    page.title = "Audio Player"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    
    # Side Bar which will contain Tracks, Playlists and "Now playing" options
    def side_bar():
        side_bar= Container(
            padding= padding.all(20),
            content = Column(
                width = 330,
                height= 500,
                controls= [
                    Column(
                        controls = [
                            FilledTonalButton(
                                text = 'Tracks',
                                height = 50,
                                width= 320,
                                style = ButtonStyle(
                                    color = {ft.MaterialState.DEFAULT:ft.colors.WHITE},
                                    shape=RoundedRectangleBorder(radius=10),
                                )
                            )
                        ]
                    )
                ]
            )
        )
        
        
        
        return side_bar
    
    
    
    c = Container(
        width = 1000,
        height= 700,
        gradient= LinearGradient(
            begin= alignment.bottom_center,
            end= alignment.top_center,
            colors= ["lightgreen100", "lightgreen200"],
        ),
        content = side_bar()
    )
    
    
    
    
    
    
    
    
    
    
    page.add (c)
    

flet.app(target=main, assets_dir="assets")