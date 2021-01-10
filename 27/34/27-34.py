Fin = open("27-34b.txt")

D = 6

N = int( Fin.readline() )

s, dMin  = 0, [10001]*D
for i in range(N):
  abc = list( map( int, Fin.readline().split() ) )
  abc = sorted( [abc[0]+abc[1], abc[0]+abc[2], abc[1]+abc[2]] )
  s += abc[0]
  for x in abc[1:]:
    d = x - abc[0]
    r = d % D
    if r > 0:
      for k in range(1, D):
        r0 = (r + k) % D
        dMin[r0] = min( d+dMin[k], dMin[r0] )
      dMin[r] = min( d, dMin[r] )

if s % D == 0:
  print( s, s % D )
else:
  print( s, s % D )
  print( dMin )
  s += dMin[D - s % D]
  print( s, s % D  )

Fin.close()
