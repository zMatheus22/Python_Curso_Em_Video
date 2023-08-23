# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame

print('===== Desafio 021 =====')
print('Musica: Xannax')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('audio/Xannax.mp3')
pygame.mixer_music.play()
pygame.mixer_music.set_volume(0.06)
pygame.event.wait()
