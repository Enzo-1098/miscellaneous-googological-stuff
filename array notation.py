def a(b):
 if len(b)==1:return b[0]
 if b[-1]==1:return a(b[:-1])
 if b[1]>1:return a([b[0]**b[0],b[1]-1]+b[2:])
 for c in enumerate(b[2:]):
  if c[1]>1:return a([b[0]]*(c[0]+2)+[c[1]-1]+b[c[0]+3:])