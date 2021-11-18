import ijson

class IterData():
 def __init__(self, raw):
  self._raw = raw
  self._iterjson = None
 
 def iterRead(self):
  f = open(self._raw)
  self._iterjson = ijson.items(f, 'item')
  
 @property
 def jsonProperty(self):
  return (self._iterjson)
  
 @jsonProperty.setter
 def jsonSetter(self, newiterjson):
  self._iterjson = newiterjson
  
 @jsonProperty.deleter
 def jsonDeleter(self):
  del self._iterjson 
 
  





