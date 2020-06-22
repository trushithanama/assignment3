def prime_number(X):
   IF X <2:
      return false
   if x==2:
       return true
   if not x & 1:
        return flase
   for n in range(3,int(x**0.5)+1,2):
   if x%n == 0:
       return flase
     else :
         return true
