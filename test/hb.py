import pygame
import random
import time

class bunyi:
	def a(self):
		return pygame.mixer.music.load("../wav/a1.wav")
		#pygame.mixer.music.play()
		
	def a1(self):
		return pygame.mixer.music.load("../wav/a1s.wav")
		#pygame.mixer.music.play()

	def b(self):
		return pygame.mixer.music.load("../wav/b1.wav")
		#pygame.mixer.music.play()
		
	def c(self):
		return pygame.mixer.music.load("../wav/c2.wav")
		#pygame.mixer.music.play()
		
	def c1(self):
		return pygame.mixer.music.load("../wav/c1s.wav")
		#pygame.mixer.music.play()

	def d(self):
		return pygame.mixer.music.load("../wav/d1.wav")
		#pygame.mixer.music.play()

	def d1(self):
		return pygame.mixer.music.load("../wav/d1s.wav")
		#pygame.mixer.music.play()

	def e(self):
		return pygame.mixer.music.load("../wav/e1.wav")
		#pygame.mixer.music.play()

	def f(self):
		return pygame.mixer.music.load("../wav/f1.wav")
		#pygame.mixer.music.play()

	def f1(self):
		return pygame.mixer.music.load("../wav/f1s.wav")
		#pygame.mixer.music.play()

	def g(self):
		return pygame.mixer.music.load("../wav/g1.wav")
		#pygame.mixer.music.play()

	def g1(self):
		return pygame.mixer.music.load("../wav/g1s.wav")
		#pygame.mixer.music.play()

	def play(self):
		return pygame.mixer.music.play()

	def stop(self):
		return pygame.mixer.music.stop()

def play():
	key.play()
	gap=random.uniform(0.3, 1.3)
	print (gap)
	time.sleep(gap)
	key.stop()


pygame.init()

key=bunyi()

while True:

	#rangkap 1

	key.g()
	key.play()
	print ('g')
	time.sleep(0.3)
	key.stop()

	key.g()
	key.play()
	print ('g')
	time.sleep(0.5)
	key.stop()

	key.a()
	key.play()
	print ('a')
	time.sleep(0.8)
	key.stop()

	key.g()
	key.play()
	print ('g')
	time.sleep(0.7)
	key.stop()

	key.c()
	key.play()
	print ('c')
	time.sleep(0.8)
	key.stop()

	key.b()
	key.play()
	print ('b')
	time.sleep(0.8)
	key.stop()


	#rangkap 2
	
	key.g()
	key.play()
	print ('g')
	time.sleep(0.3)
	key.stop()

	key.g()
	key.play()
	print ('g')
	time.sleep(0.5)
	key.stop()

	key.a()
	key.play()
	print ('a')
	time.sleep(0.8)
	key.stop()

	key.g()
	key.play()
	print ('g')
	time.sleep(0.7)
	key.stop()

	key.d()
	key.play()
	print ('d')
	time.sleep(0.8)
	key.stop()

	key.c()
	key.play()
	print ('c')
	time.sleep(0.8)
	key.stop()

	#rangkap 3
	for x in range(0, 2):
		key.g()
		key.play()
		print ('g')
		time.sleep(0.3)
		key.stop()

	key.g()
	key.play()
	print ('g')
	time.sleep(0.8)
	key.stop()

	key.e()
	key.play()
	print ('e')
	time.sleep(0.8)
	key.stop()

	key.c()
	key.play()
	print ('c')
	time.sleep(0.8)
	key.stop()

	key.b()
	key.play()
	print ('b')
	time.sleep(0.8)
	key.stop()

	key.a()
	key.play()
	print ('a')
	time.sleep(0.8)
	key.stop()

	time.sleep(3)

#lagu=[key.a(), key.a1(), key.b(), key.c(), key.c1(), key.d(), key.d1(), key.e(), key.f(), key.f1(), key.g(), key.g1()]


#for x in range(10):
#gen=random.randint(0, 11)
#print gen
#lagu[0]
#pygame.mixer.music.play()
#time.sleep(0.5)



#lagu=[key.a(), key.f(), key.c()]
#
#for x in lagu:
#
#	lagu[x]
#	time.sleep(0.5)

#lagu=[key.a(),key.f(),key.c()]
#for attr, value in lagu.__dict__.iteritems():
#	print attr, value
#	time.sleep(0.5)

#lagu=[key.a(),key.f(),key.c()]
#ter=list(lagu)
#print ter 
