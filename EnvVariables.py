import os

#setup variable
os.environ['mass_effect'] = "C://Users//GrandProf//Pictures//mass.effect//me1.png"

def convert(val): 
  if type(val) != str:
    return val 
  if val.isnumeric(): 
    return int(val) 
  elif val == 'True': 
    return True
  elif val == 'False': 
    return False
  else:
    return val 

#get variable 
masseff = convert(os.environ.get('mass_effect')) 
masseff = os.getenv('mass_effect')

