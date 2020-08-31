import pygame
import random
import time

class bunyi:
	def a(self):
		return pygame.mixer.music.load("wav/a1.wav")
		#pygame.mixer.music.play()
		
	def a1(self):
		return pygame.mixer.music.load("wav/a1s.wav")
		#pygame.mixer.music.play()

	def b(self):
		return pygame.mixer.music.load("wav/b1.wav")
		#pygame.mixer.music.play()
		
	def c(self):
		return pygame.mixer.music.load("wav/c2.wav")
		#pygame.mixer.music.play()
		
	def c1(self):
		return pygame.mixer.music.load("wav/c1s.wav")
		#pygame.mixer.music.play()

	def d(self):
		return pygame.mixer.music.load("wav/d1.wav")
		#pygame.mixer.music.play()

	def d1(self):
		return pygame.mixer.music.load("wav/d1s.wav")
		#pygame.mixer.music.play()

	def e(self):
		return pygame.mixer.music.load("wav/e1.wav")
		#pygame.mixer.music.play()

	def f(self):
		return pygame.mixer.music.load("wav/f1.wav")
		#pygame.mixer.music.play()

	def f1(self):
		return pygame.mixer.music.load("wav/f1s.wav")
		#pygame.mixer.music.play()

	def g(self):
		return pygame.mixer.music.load("wav/g1.wav")
		#pygame.mixer.music.play()

	def g1(self):
		return pygame.mixer.music.load("wav/g1s.wav")
		#pygame.mixer.music.play()

	def play(self):
		return pygame.mixer.music.play()

	def stop(self):
		return pygame.mixer.music.stop()

def play():						#FUNCTION that play and stop the sound
	key.play()						#play sound that load
	gap=random.uniform(0.3, 1.3)	#gap between sound 0.3 to 1.3
	print (gap)
	time.sleep(gap)					#play sound with this time
	key.stop()						#stop play the sound


pygame.init()

key=bunyi()							#assign object to class

while True:

	gen=random.randint(0, 11)		#get random number
	print (gen)

	if gen==0:
		key.a()

	elif gen==1:
		key.a1()

	elif gen==2:
		key.b()

	elif gen==3:
		key.c()

	elif gen==4:
		key.c1()

	elif gen==5:
		key.d()

	elif gen==6:
		key.d1()

	elif gen==7:
		key.e()

	elif gen==8:
		key.f()

	elif gen==9:
		key.f1()

	elif gen==10:
		key.g()

	elif gen==11:
		key.g1()

	play()			#play the sound and stop the sound