import os
import tkinter as tk
import tkinter.filedialog
import pygame

class Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        # Initialisation de Pygame
        pygame.init()

        # Variables
        self.playlist = []
        self.current_track = 0
        self.paused = False
        self.loop = False

        # Boutons
        tk.Label(self.root, text="Playlist").grid(row=0, column=0)
        self.listbox = tk.Listbox(self.root, height=10)
        self.listbox.grid(row=1, column=0, rowspan=6)
        tk.Button(self.root, text="Ajouter", command=self.ajouter_pistes).grid(row=1, column=1)
        tk.Button(self.root, text="Supprimer", command=self.supprimer_pistes).grid(row=2, column=1)
        tk.Button(self.root, text="Lire", command=self.lire_pistes).grid(row=3, column=1)
        tk.Button(self.root, text="Pause", command=self.pause_pistes).grid(row=4, column=1)
        tk.Button(self.root, text="Arrêter", command=self.arreter_pistes).grid(row=5, column=1)
        tk.Checkbutton(self.root, text="Boucle", command=self.en_boucle).grid(row=6, column=1)
        tk.Scale(self.root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.régler_volume).grid(row=7, column=0)

    def ajouter_pistes(self):
        tracks = tk.filedialog.askopenfilenames(filetypes=[("Fichiers audio", "*.mp3;*.wav")])
        for track in tracks:
            self.playlist.append(track)
            self.listbox.insert(tk.END, os.path.basename(track))

    def supprimer_pistes(self):
        selection = self.listbox.curselection()
        if selection:
            self.playlist.pop(selection[0])
            self.listbox.delete(selection[0])

    def lire_pistes(self):
        if not pygame.mixer.music.get_busy():
            track = self.playlist[self.current_track]
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()

    def pause_pistes(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def arreter_pistes(self):
        pygame.mixer.music.stop()

    def en_boucle(self):
        self.loop = not self.loop

    def régler_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

# Lancer l'interface graphique
root = tk.Tk()
player = Player(root)
root.mainloop()
