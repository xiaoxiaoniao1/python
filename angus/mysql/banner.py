import json
  
class Banner:
  id = None
  path = None
  weight = None
  menuId = None
  type = None

  def __init__(self, id, path, weight, menuId, type):
    self.id = id
    self.path = path
    self.weight = weight
    self.menuId = menuId
    self.type = type

  def __str__(self):
    #return "[id=%s, path=%s, weight=%s, menuId=%s, type=%s]" % (self.id, self.path, self.weight, self.menuId, self.type)
    return json.dumps(self.__dict__)

  def __repr__(self):
    return self.__str__()

  def toJson(self):
    return json.dumps(self.__dict__)
