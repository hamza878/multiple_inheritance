class A:
  def letsPrint2(self):
    print('im from class A')
    
class B:
  def letsPrint(self):
    print('im from class B')
    
class C(A, B):
  pass


obj = C()
obj.letsPrint()
