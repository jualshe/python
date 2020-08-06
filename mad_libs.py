# easy way
# def mad_libs():
# 	string = "I am a noun"
# 	string = string.replace ("noun", "llama")
# 	return string

# print mad_libs()
#____________________
#hard way
def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "noun":
        return random_noun()
    if word == "verb":
        return random_verb()
    else: 
    	return word[0]

def mad_libs(sentence):
	processed = ""
	index = 0
	box_length = 4
	while index < len(sentence):
		frame = sentence[index:index+box_length]
		to_add = word_transformer(frame)
		processed = processed+to_add
		if len(to_add) == 1:
			index = index+1
		else:
			index = index +4 
	return processed

# print mad_libs('I am a noun')
# print mad_libs('I am a verb')