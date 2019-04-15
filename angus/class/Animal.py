class Animal:
  headNum = 1
  age = 0
  catagory = "crawel"
  gender = None

  def __init__(self, g):
    self.gender = g

  def drink(self, sth):
    print "i can drink %s " % sth

  def eat(self, sth):
    print "i want to eat %s " % sth

  def walk(self):
    print "i like walking"


if __name__ == "__main__":
  an = Animal("female")
  print an.gender
  an.drink("water")
  an.eat("grass")
  an.walk()
