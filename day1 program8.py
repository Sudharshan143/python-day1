def isNumeric(s):
   s = s.strip()
   try:
      s = float(s)
      return True
   except:
      return False

str=input("ENTER THE VALUE: ")
ret_val=isNumeric(str)
print(ret_val)
