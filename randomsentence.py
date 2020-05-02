# Random Sentence Engine
# Creates randomized sentences with different varied structures by using a decision tree structure
# to choose each new part of speech based on what it follows.

import random

# These lists hold the words that the sentences can use.

# The selector will choose from various lists, and then choose a random word from that list,
# but this is based on what the previous word was.
# The numbers refer to which selection state the engine uses to pick that type of word.

#1: Possessive-type words
poss = ["your", "my", "his"]

#2: Objects - words that refer to a noun
obj = ["the", "a", "some", "that"]                         

#3: Nouns - people, places, things, and abstract ideas
noun = ["car", "tree", "boat", "plane", "dog", "cat", "house"]

#4: Verbs - action words. In this list, they don't act on anything.
verb = ["ran", "swam", "flew", "barked", "exploded", "shone"]

#5: Transitive verbs act on a noun.
transitive = ["drove", "hit", "yanked", "poked", "mended", "moved"]

#6: Adjectives describe a noun
adjective = ["wet", "shiny", "blue", "slick", "old", "aromatic", "rough", "weak", "glittery"]

#7: Adverbs describe a verb
adverb = ["dully", "quickly", "nicely", "slowly", "smoothly"]

#8: Conjunctions tie sentences together into larger sentences.
conjunc = ["and", "while", "but", "then", "so", "because", "although"] # 8

# 9 is the ending state which is only available after a
# part of speech capable of finishing a sentence.

# Variables to store the lengths of all the lists.                                                
lenposs = int(len(poss))
lenobj = int(len(obj))
lennoun = int(len(noun))
lenverb = int(len(verb))
lentransitive = int(len(transitive))
lenadj = int(len(adjective))
lenadverb = int(len(adverb))
lenconjunc = int(len(conjunc))

# This flag is set when the sentence reaches an ending state, halting the engine.
sentence_finished = 0
# This is a flag that specifies the current part of speech. Its value controls what parts of speech
# can come after it.
chosen = 0  # 0 is specifically for the beginning of the sentence.
# This is the string that the program outputs as a sentence.
outputsentence = ""

while not sentence_finished:
        
    if chosen == 0:
        # This flag is set if the transitive verb is chosen so that verbs are not chosen inside an object phrase
        istransitive = 0
        choices = [1, 2]  # the parts of speech that may begin a sentence.
        chosen = random.sample(choices, 1)
        
    if chosen == [1]: # possessive word
        element = random.randint(0, lenposs-1) # print a random word from the possesive list.
        outputsentence = outputsentence + " " + poss[element]
        # after a posessive type word we could have a noun or an adjective.
        choices = [3, 6]
        chosen = random.sample(choices, 1) # choose which one to use.
    
    if chosen == [2]: # object word
        element = random.randint(0, lenobj-1) #print a random word from the object list.
        outputsentence = outputsentence + " " + obj[element]
        # after an object type word we could have a noun or an adjective.
        choices = [3, 6]
        chosen = random.sample(choices, 1) # choose which one to use.
    
    if chosen == [3]: # noun
        element = random.randint(0, lennoun-1)
        outputsentence = outputsentence + " " + noun[element]
        if istransitive: # this is an object noun that should be followed by an adverb or the end of the clause.
            choices = [7, 8, 9]
        else:
            choices = [4, 5] # This is a subject noun which has to be followed by a verb
        chosen = random.sample(choices, 1)
        
    if chosen == [4]: # verb
        element = random.randint(0, lenverb-1)
        outputsentence = outputsentence + " " + verb[element]
        choices = [7, 8, 9] # modify with adverb, use a conjection to another clause or end the sentence
        chosen = random.sample(choices, 1)
        
    if chosen == [5]: # a transitive verb (one that does a thing to a thing.)
        element = random.randint(0, lentransitive-1)
        outputsentence = outputsentence + " " + transitive[element]
        istransitive = 1
        choices = [1, 2] # we now need to refer to some object (a noun)
        chosen = random.sample(choices, 1)
        
    if chosen == [6]: # adjective
        element = random.randint(0, lenadj-1)
        outputsentence = outputsentence + " " + adjective[element]
        choices = [3, 6] # a noun or another adjective
        chosen = random.sample(choices, 1)
    
    if chosen == [7]: #adverb
        element = random.randint(0, lenadverb-1)
        outputsentence = outputsentence + " " + adverb[element]
        choices = [8, 9] # use a conjection to another clause or end the sentence
        chosen = random.sample(choices, 1)
        
    if chosen == [8]: #conjunction
        element = random.randint(0, lenconjunc-1)
        outputsentence = outputsentence + " " + conjunc[element]
        chosen = 0 # starting a new clause is like starting a new sentence
    
    if chosen == [9]:
        outputsentence = outputsentence.replace(" ", "", 1)
        outputsentence = outputsentence.capitalize()
        outputsentence = outputsentence + ". \n"
        print(outputsentence)
        sentence_finished = 1
