def test(name="masa", age=30):
  print "name=%s, age=%d" % (name, age)

if __name__=="__main__":
  test(name="angus")
  test("leif")
  test("lance",20)
  test(age=20)
