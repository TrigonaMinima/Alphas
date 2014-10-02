import string

def loweralph():
  return string.ascii_lowercase        

def upperalph():
  return string.ascii_uppercase 

def alphlist():
  l = []
  for a in loweralph():
    l.append(a)
  for a in upperalph():
    l.append(a)  
  return l        

def dicalpha():
  d = {}
  for a in alphlist():
    d[a] = ''
  return d 

if __name__ == '__main__':
  print loweralph()
  print upperalph()
  print alphlist()
  print dicalpha()
        
