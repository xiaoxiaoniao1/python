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

#old style
class People(Animal):
    name = None

    def __init__(self, gender, name="angus"):
        Animal.__init__(self, gender)
        self.name = name

    def speak(self, sth):
        print "i can speak, %s" % sth

#new style
class Monkey(Animal, object):
    name = None

    def __init__(self, gender, name="angus"):
        super(Monkey, self).__init__(gender)
        self.name = name

    def speak(self, sth):
        print "i can speak, %s" % sth


if __name__ == "__main__":
  #an = Animal("female")
  #print an.gender
  #an.drink("water")
  #an.eat("grass")
  #an.walk()

  #p = People(gender="male", name = "leif")
  #p.speak(" i am leif")
  #p.walk()
  #print p.gender

  #p1 = People(name="leif", gender="female")
  #p1.speak(" i am leif")
  #p1.walk()
  #print p1.gender

  m = Monkey("male")
  print m.gender

  #单例模式 - 整个应用中只有一个实例(对象)
