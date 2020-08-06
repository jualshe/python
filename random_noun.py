from random import randint

def random_noun():
    random_num = randint(0, 1)
    if random_num == 0:
        return "llama"
    else:
        return "apple"