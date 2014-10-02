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

def dict_bi():
  bi = {}
  for a in alphlist():
    bi[a] = "{0:b}".format(ord(a))  
  return bi

def dict_oct():
  octa = {}
  for a in alphlist():
    octa[a] = "{0:o}".format(ord(a))  
  return octa
  
def dict_hex():
  hexa = {}
  for a in alphlist():
    hexa[a] = "{0:x}".format(ord(a))  
  return hexa  

if __name__ == '__main__':
  print loweralph()
  print upperalph()
  print alphlist()
  print dicalpha()
  print dict_bi()
  print dict_oct()
  print dict_hex()
        
