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
                            width= 1,
                            color = 'black12',
                            thickness= 2
                            ),
                            Column(
                                spacing = 0,
                                controls =[
                                    
                                    Container(
                                        bgcolor = 'black',
                                        width= 700,
                                        height = 500,
                                        alignment= alignment.bottom_center
                                        
                                    ),
                                    ft.Divider(height=9, thickness = 3, color = 'red'),
                                    Container(
                                        bgcolor = 'black',
                                        width= 700,
                                        height = 100,
                                        alignment= alignment.bottom_center,
                                        
                                        
                                    ),
                                    
                                ]
                            )
                        ]
                    ),
                )
                
    )

ft.app(target=main, assets_dir="assets")