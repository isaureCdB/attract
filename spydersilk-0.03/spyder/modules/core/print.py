# Copyright 2007-2011, Sjoerd de Vries
# This file is part of the Spyder module: "core" 
# For licensing information, see LICENSE.txt 

def generate_str(typename, parentnames, source, members, deleted_members, block):
  if block != None: raise Exception
  s = """  def __str__(self):
    \\\"\\\"\\\"Auto-generated by Spyder:
     module core
     file print.py
     function generate_str
    Converts the current object to a string
    This function is triggered by the print statement
    Redirects to self.__print__\\\"\\\"\\\"
    return self.__print__(0, \"str\")
"""
  s += """  def str(self):
    \\\"\\\"\\\"Auto-generated by Spyder:
     module core
     file print.py
     function generate_str
    Converts the current object to a string
    Redirects to self.__print__\\\"\\\"\\\"
    return self.__print__(0, \"str\")
"""      
  s += """  def data(self):
    \\\"\\\"\\\"Auto-generated by Spyder:
     module core
     file print.py
     function generate_str
    Converts the current object to a string
    Redirects to self.__print__\\\"\\\"\\\"
    return self.__print__(0, \"str\")
"""      
  if len(members) == 0: return None,s   
  return s.replace("\\\"\\\"\\\"", '"""'),s

def generate_repr(typename, parentnames, source, members, deleted_members, block):
  if block != None: raise Exception
  s = """  def repr(self):
    \\\"\\\"\\\"Auto-generated by Spyder:
     module core
     file print.py
     function generate_repr
    Converts the current object to a representation string
    As a side effect, saves all files within the object
    Redirects to self.__print__\\\"\\\"\\\"
    return self.__print__(0, \"repr\")
"""
  s += """  def __repr__(self):
    \\\"\\\"\\\"Auto-generated by Spyder:
     module core
     file print.py
     function generate_repr
    Converts the current object to a representation string
    As a side effect, saves all files within the object
    Redirects to self.__print__\\\"\\\"\\\"
    return self.__print__(0, \"repr\")
"""        
  if len(members) == 0: return None,s    
  return s.replace("\\\"\\\"\\\"", '"""'),s

def generate_print(typename, parentnames, source, members, deleted_members, block):
  requiredmembers, defaultmembers, optionalmembers, args, allargs = spyder.core.parse_members(typename,members,None, spyder.safe_eval)  
  if block != None: raise Exception
  s = """  def __print__(self,spaces,mode):
    \"\"\"Auto-generated by Spyder:
     module core
     file print.py
     function generate_print
    Pretty-prints the current object, for internal use only\"\"\"
"""
  s += "    ret = \"%s (\\n\" % self.typename() \n"
  for m in members:
    mm = m[1]
    for n in range(0,len(mm)):
      c = mm[n]
      if c == "=":
        mm = mm[:n].rstrip()
        break
      elif c == "'" or c == "\"": break
    s += "    v = self.%s\n" % mm
    spaces = 0
    if mm in optionalmembers:
      s += "    if v != None:\n"
      spaces = 2
    s += "    %sif type(v) != %s: v = %s(v)\n" % (spaces * " ", m[0], m[0]) 
    s += "    %sret += \"%%s%s = \" %% ((spaces+2) * \" \") + v.__print__(spaces+2, mode) + \",\\n\"\n" % (spaces * " ", mm)
  s += "    ret += \"%s)\" % (spaces * \" \")\n"
  s += "    return ret\n"
  arraycode  = r"""  def __print__(self,spaces,mode):
    ret = "%%s (\n" %% self.typename()
    for v in self:
      ret += (spaces+2) * " " + v.__print__(spaces+2, mode) + ",\n"
    ret += spaces * " " +  ")"
    return ret"""
  if len(members) == 0: return None,arraycode    
  return s,arraycode


spyder.defineunimethod("__str__", generate_str)
spyder.defineunimethod("__repr__", generate_repr)
spyder.defineunimethod("__print__", generate_print)