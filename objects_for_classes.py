reginald = Giraffes()

def this_is_a_normal_function(): print('regular function')

class ThisIsMySillyClass:
              def this_is_a_class_function():
print('function of the class') def this_is_also_a_class_function():
                    print('it\'s also function of the class?')

class Animals(Animate):
              def breathe(self):
                    pass
              def move(self):
                    pass
              def eat_food(self):
                    pass

class Mammals(Animals):
              def feed_young_with_milk(self):
					pass	 

class Giraffes(Mammals):
              def eat_leaves_from_trees(self):
					pass
reginald = Giraffes()