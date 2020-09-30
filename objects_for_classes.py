reginald = Giraffes()

def this_is_a_normal_function(): print('regular function')

class ThisIsMySillyClass:
              def this_is_a_class_function():
print('function of the class') 

def this_is_also_a_class_function():
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


import turtle
avery = turtle.Pen() 
kate = turtle.Pen()


avery.forward(50)
avery.right(90)
avery.forward(20)

kate.left(90)
kate.forward(100)


jacob = turtle.Pen()
jacob.left(100)
jacob.forward(50)


reginald = Giraffes()
reginald.move()


eginald = Giraffes() 
reginald.breathe() 
reginald.eat_food()
reginald.feed_young_with_milk()

reginald.move()

class Giraffes(Mammals):
	def find_food(self):
		self.move()
		print("I found food") 
		self.eat_food()
	def eat_leaves_from_trees(self): 
		self.eat_food()
	def dance_a_jig(self): 
		self.move()
		self.move()
		self.move() 
		self.move()


reginald = Giraffes()
reginald.dance_a_jig()
