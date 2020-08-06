sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "copybara" # your noun here
verb_replacement = "eats" # your verb here

new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3

print new_sentence