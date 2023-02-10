import flet as ft
from flet import *


def main(page: Page):
    page.title = "Audio Player"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    
    # Side Bar which will contain Tracks, Playlists and "Now playing" options
    def side_bar():
        side_bar= Container(
            bgcolor = "lightgreen200",
            padding = padding.only(top=50),
            content = Column(
                width = 330,
                height= 500,
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
                                color = "white",
                                elevation = 0,
                                # opacity= 7,
                                autofocus = False,
                                bgcolor = "lightgreen200",
                                style = ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=8),
                                ),
                                
                            )
                        ]
                    ),
                    
                    
                    
                    
                    
                ]
            )
        )
        VerticalDivider(
                                width= 10,
                                color = 'white',
                                thickness= 10
                            ),
        
        return side_bar
    
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
        content = side_bar()
    )
    
    
    
    
    
    
    
    
    
    
    page.add (
                Container(
                    
                    width = 1000,
                    height= 700,
                    gradient= LinearGradient(
                        
                        begin= alignment.bottom_center,
                        end= alignment.top_center,
                        colors= ["lightgreen100", "lightgreen200"],
                    ),
                    
                    content = Row(
                        controls=[
                            Container(
                        
                        bgcolor = "lightgreen200",
                        padding = padding.only(top=50),
                        content = Column(
                            
                            width = 330,
                            height= 500,
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
                                            color = "white",
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
                    width= 10,
                    color = 'white',
                    thickness= 10
                )
                    
                        ]
                    ),
                )
                
    )

ft.app(target=main, assets_dir="assets")