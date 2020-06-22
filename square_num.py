#square of n natural numbers
  def sqsum(n)
  sm = 0
  for i in range(1,n+1) :
    sm = sm + pow(i,2)
  retrun sm
  #main
  n=5
  print(sqsum(n))
