# This file produces a randomly generated story, similar to the
# output from an old-fashioned text adventure. In it, your character
# goes hunting for monsters and peiodically rests. It runs until the
# character gets bored and goes home, or dies.

# This library of terms can be modified to suit you
animals = ["wolf", "bear", "fox", "eagle", "badger"]
kind = ["dire", "mutant", "raging", "flying", "radioactive"]
feeling = ["pleasant", "shady", "peaceful"]
place = ["river", "glade", "copse", "thicket", "path"]
hit = ["strike", "stab", "slash", "pierce", "gouge", "smack"]
mhit = ["bites", "shocks", "claws", "gouges", "pummels"]
dead = ["killed", "defeated", "vanquished"]

restprob = 30 # percent
huntprob = 65 # percent

import random as r

name = input("What is your name?")
print("Let the hunt begin, {}!".format(name))

boredom = 0
maxhp = 10
hp = maxhp

while hp > 0:
	print("You have "+str(hp)+" health out of a maximum of "+str(maxhp),".\n")

	roll = r.randint(1, 100)
	if roll <= huntprob:
		comm = 'h'
	elif roll <= huntprob+restprob:
		comm = 'r'
	else:
		comm = 'q'
		
	if comm == 'q':
		break
	if comm == 'r':
		findex = r.randint(0, len(feeling)-1)
		pindex = r.randint(0, len(feeling)-1)
		print("You rest in a "+feeling[findex]+" "+place[pindex]+".")
		hp = min(maxhp, hp+r.randint(1, int(maxhp/2)))
		boredom = boredom + r.randint(0, maxhp)
		if boredom > maxhp:
			print("Resting is getting boring. Time to hunt!")
			comm = 'h'
	if comm == 'h':
		mhp = r.randint(int(maxhp/4), maxhp-1)
		monstertype = animals[r.randint(0, len(animals)-1)]
		monsterkind = kind[r.randint(0, len(kind)-1)]
		killed = dead[r.randint(0, len(dead)-1)]
		
		monstername = monsterkind+" "+monstertype

		print("You meet a "+monstername+"!")

		initiative = ((maxhp-mhp)/hp > 0.8) # You catch the monster out if it's smaller by enough
		# Upper and lower damage limits for the current enounter: monster and player
		mupper = int(mhp/3)
		mlower = int(mhp/10)
		pupper = maxhp
		plower = int(maxhp/5)

		while mhp > 0 and hp > 0:
			monsterhit = hit[r.randint(0, len(hit)-1)]
			response = mhit[r.randint(0, len(mhit)-1)]
			# if you have initiative you hit first.
			if initiative:
				damage = r.randint(plower, pupper)
				print("You "+monsterhit+" the "+monstername+" for "+str(damage)+" damage!")
				mhp = mhp - damage
			damage = r.randint(mlower, mupper)
			print("The "+monstername+" "+response+" you for "+str(damage)+" damage!")
			hp = hp - damage
			damage = r.randint(plower, pupper)
			print("You "+monsterhit+" the "+monstername+" for "+str(damage)+" damage!")
			mhp = mhp - damage
		if mhp <= 0:
			print("You "+killed+" the "+monstername+"!")
			maxhp = maxhp + r.randint(mlower, mupper)
			boredom = max(0, boredom - r.randint(0, int(maxhp/3)))
if comm == 'q':
	print("You go home.")
else:
	print("Sadly, "+name+", you were killed by the "+monstername+".")
