import os
import pygame
from tkinter import Tk, Button, Label, filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Lecteur de musique")
        self.root.geometry("300x100")
        self.music_dir = ""
        self.current_song = ""
        self.paused = False
        
        self.label_status = Label(self.root, text="Aucune musique en cours", bd=1, relief="sunken", anchor="w")
        self.label_status.pack(fill="x")
        
        self.btn_browse = Button(self.root, text="Choisir un fichier audio", command=self.choose_music)
        self.btn_browse.pack(pady=5)
        
        self.btn_play = Button(self.root, text="Jouer", command=self.play_music, state="disabled")
        self.btn_play.pack(side="left", padx=5)
        
        self.btn_pause = Button(self.root, text="Pause", command=self.pause_music, state="disabled")
        self.btn_pause.pack(side="left", padx=5)
        
        self.btn_stop = Button(self.root, text="Stop", command=self.stop_music, state="disabled")
        self.btn_stop.pack(side="left", padx=5)
        
    def choose_music(self):
        self.music_dir = filedialog.askopenfilename(initialdir="/", title="Choisir un fichier audio", filetypes=(("Fichiers audio", "*.mp3 *.wav"),))
        if self.music_dir:
            self.btn_play.config(state="normal")
        
    def play_music(self):
        if not self.current_song:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_dir)
            self.current_song = os.path.basename(self.music_dir)
            self.label_status.config(text="En train de jouer : " + self.current_song)
        pygame.mixer.music.play()
        self.btn_pause.config(state="normal")
        self.btn_stop.config(state="normal")
        self.btn_play.config(state="disabled")
        
    def pause_music(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.label_status.config(text="En train de jouer : " + self.current_song)
            self.btn_pause.config(text="Pause")
        else:
            pygame.mixer.music.pause()
            self.paused = True
            self.label_status.config(text="Musique en pause : " + self.current_song)
            self.btn_pause.config(text="Reprendre")

        
    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_song = ""
        self.label_status.config(text="Aucune musique en cours")
        self.btn_play.config(state="normal")
        self.btn_pause.config(state="disabled")
        self.btn_stop.config(state="disabled")
        
root = Tk()
music_player = MusicPlayer(root)
root.mainloop()
