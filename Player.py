import os
import flet as ft
from pydub import AudioSegment
import pygame
from pygame import mixer
from flet import *


home_dir = os.path.expanduser("~\Music")

files = os.listdir(home_dir)

# for files in rocks:
#     print(rocks)


def main(page: Page):
    page.title = "Audio Player"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    
    def play(file):
        os.chdir(home_dir)
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        page.update()
        
    
    def playall():
        
        pass
    
    def pause():
        
        pass
    
    def _divider():
        div=VerticalDivider(
                                width= 10,
                                color = 'white',
                                thickness= 10
                            ),
        
        return div
        
    
    
    cont = []
    # This function lists the tracks as buttons in the container
    def tracks_button(e):
        files = os.listdir(home_dir)
        for file in files:
            button = ElevatedButton(
                text = file,
                height = 45,
                width= 300,
                color = "white",
                elevation = 0,
                # opacity= 7,
                autofocus = False,
                bgcolor = "lightgreen200",
                on_click= lambda f = file: play(f),
                style = ButtonStyle(
                    shape=RoundedRectangleBorder(radius=4),
                ),
            )
            cont.append(button)
            page.update()
        
        
        
    
    
    
    
    
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
                                                    on_click = tracks_button,
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
                            width= 3,
                            color = 'black12',
                            thickness= 2
                            ),
                            Column(
                                spacing = 0,
                                controls =[
                                    
                                    Container(
                                        # bgcolor = 'black',
                                        width= 700,
                                        height = 470,
                                        margin = margin.only(left=-10),
                                        content = ListView(cont,spacing =0, padding = 10)
                                        
                                        
                                    ),
                                    Container(
                                        # bgcolor = 'red',
                                        height = 10,
                                        width = 695,
                                        margin = margin.only(left=-10),
                                        content = Divider(
                                            thickness = 3.0,
                                            color = 'black45',
                                            )
                                    ),
                                    
                                    
                                    
                                    Container(
                                        # bgcolor = 'black',
                                        width= 700,
                                        height = 120,
                                        margin = margin.only(left=-10),
                                        content = Column(
                                            controls = [
                                                Column(
                                                    
                                                    controls = [
                                                        Container(
                                                            padding = padding.only(top =10),
                                                            alignment = alignment.center,
                                                            content = ProgressBar(
                                                                width = 400,
                                                                value = 0.5,
                                                                )
                                                            ),
                                                        ]
                                                    ),
                                                Column(
                                                    controls = [
                                                        
                                                        Container(
                                                            
                                                            content = Row(
                                                                alignment = 'center',
                                                                controls = [
                                                                    IconButton(
                                                                        icon= icons.SKIP_PREVIOUS_ROUNDED,
                                                                        icon_color = 'white',
                                                                        icon_size = 50  
                                                                        ),
                                                                    IconButton(
                                                                        icon= icons.PLAY_CIRCLE_ROUNDED,
                                                                        icon_color = 'white',
                                                                        icon_size = 50  
                                                                        ),
                                                                    IconButton(
                                                                        icon= icons.SKIP_NEXT_ROUNDED,
                                                                        icon_color = 'white',
                                                                        icon_size = 50  
                                                                        ),
                                                                    
                                                                ]
                                                            )
                                                        )
                                                    ],
                                                )
                                            ]
                                        )
                                    ),
                                    
                                ]
                            )
                        ]
                    ),
                )
                
    )

ft.app(target=main, assets_dir="assets")