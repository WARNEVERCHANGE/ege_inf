Fin = open("27-22a.txt")

N = int( Fin.readline() )
B = 10
D = 4

dMin = [100001]*B
s = 0
for i in range(N):
  a, b = map( int, Fin.readline().split() )
  s += min( a, b )
  d = abs( a-b )
  r = d % B
  dMinNew = dMin[:]
  for k in range(1, B):
    r0 = (r + k) % B
    dMinNew[r0] = min( d+dMin[k], dMin[r0] )
  dMinNew[r] = min( d, dMin[r] )
  dMin = dMinNew[:]

if s % B == D:
  print( s )
else:
  print( s, s % B, dMin )
  r0 = D - s % B
  if r0 < 0: r0 += B
  print( s + dMin[r0] )

Fin.close()