import os
import flet as ft
from flet import *


def main(page: Page):
    page.title = "Audio Player"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    
    
    
    def _divider():
        div=VerticalDivider(
                                width= 10,
                                color = 'white',
                                thickness= 10
                            ),
        
        return div
        
    
    c = Container(
        width = 1000,
        height= 700,
        gradient= LinearGradient(
            begin= alignment.bottom_center,
            end= alignment.top_center,
            colors= ["lightgreen100", "lightgreen200"],
        ),
        
    )
    
    
    
    
    
    
    
    
    
    
    page.add (
                Container(
                    
                    width = 1000,
                    height= 600,
                    gradient= LinearGradient(
                        
                        begin= alignment.bottom_center,
                        end= alignment.top_center,
                        colors= ["lightgreen100", "lightgreen200"],
                    ),
                    
                    content = Row(
                        controls=[
                            Container(
                                margin = margin.only(right=-10),
                                gradient= LinearGradient(
                                    begin= alignment.bottom_center,
                                    end= alignment.top_center,
                                    colors= ["lightgreen200", "lightgreen200"],
                                ),
                                padding = padding.only(top=20),
                                content = Column(
                                
                                width = 300,
                                # height= 500,
                                    controls= [
                                        
                                
                                        Column(
                                            
                                            spacing = 0,
                                            controls = [
                                                
                                                ElevatedButton(
                                                    
                                                    text = 'Tracks',
                                                    height = 50,
                                                    width= 300,
                                                    color = "white",
                                                    elevation = 0,
                                                    # opacity= 7,
                                                    autofocus = False,
                                                    bgcolor = "lightgreen200",
                                                    style = ButtonStyle(
                                                        shape=RoundedRectangleBorder(radius=8),
                                                    ),
                                                ),
                                                ElevatedButton(
                                                    
                                                    text = 'Playlists',
                                                    height = 50,
                                                    width= 300,
                                                    color = "white",
                                                    elevation = 0,
                                                    # opacity= 7,
                                                    autofocus = False,
                                                    bgcolor = "lightgreen200",
                                                    style = ButtonStyle(
                                                        shape=RoundedRectangleBorder(radius=8),
                                                    ),
                                                ),
                                                ElevatedButton(
                                                    text = 'Now Playing',
                                                    height = 50,
                                                    width= 300,
                                                    color = "black45",
                                                    elevation = 0,
                                                    # opacity= 7,
                                                    autofocus = False,
                                                    bgcolor = "lightgreen200",
                                                    style = ButtonStyle(
                                                        shape=RoundedRectangleBorder(radius=8),
                                                    ),
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ),
                            ft.VerticalDivider(
                            width= 5,
                            color = 'black12',
                            thickness= 2
                            ),
                            Column(
                                spacing = 0,
                                controls =[
                                    
                                    Container(
                                        # bgcolor = 'black',
                                        width= 700,
                                        height = 500,
                                        margin = margin.only(left=-10),
                                        
                                        
                                    ),
                                    Container(
                                        bgcolor = 'black',
                                        content = Divider(height=50, thickness = 2, color = colors.BLACK  ) 
                                        ),
                                    
                                    Container(
                                        # bgcolor = 'black',
                                        width= 700,
                                        height = 90,
                                        margin = margin.only(left=-10),
                                        
                                    ),
                                    
                                ]
                            )
                        ]
                    ),
                )
                
    )

ft.app(target=main, assets_dir="assets")