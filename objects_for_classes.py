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

reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

harold = Giraffes()
harold.move()

class Animals(Animate):
              def breathe(self):
                    print('breathe')
              def move(self):
                    print('move')
              def eat_food(self):
                    print('eat_food')

class Mammals(Animals):
              def feed_young_with_milk(self):
                    print('feed_young_with_milk')

class Giraffes(Mammals):
              def eat_leaves_from_trees(self):
                    print('eat_leaves_from_trees')

reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()
