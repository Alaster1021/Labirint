def create(ccskrf):
  import random
  def generate0():
      b=12*24
      a=[[] for _ in range(b)]
      notused=[]
      for g in range(b):
          notused+=[g]
      k=random.randint(0,len(notused)-1)
      s=notused[k]
      notused.remove(s)
      while 60 in notused or 167 in notused:
          #k=random.randint(0,len(notused)-1)
          #s=notused[k]
          #notused.remove(s)
          c=[]
          if s>=12:
              c+=[s-12]
          if s<=275:
              c+=[s+12]
          if not s%12==11:
              c+=[s+1]
          if not s%12==0:
              c+=[s-1]
          k1=random.randint(0,len(c)-1)
          s1=c[k1]
          a[s]+=[s1]
          a[s1]+=[s]
          if s1 in notused:
              notused.remove(s1)
          s=s1
      for y in range(len(a)):
        a[y]=set(a[y])
        a[y]=list(a[y])
      return a
  def generate1(a):
      m=[1]*25+[1,0]*12+[1]
      labirint=m*24+[1]*50
      c1=-1
      for u in range(len(labirint)):
          if labirint[u]==0:
              c1+=1
              if c1-12 in a[c1]:
                  labirint[u-25]=2
              if c1+12 in a[c1]:
                  labirint[u+25]=2
              if c1+1 in a[c1]:
                  labirint[u+1]=2
              if c1-1 in a[c1]:
                  labirint[u-1]=2
      return labirint
  r=generate0()
  #print(r)
  r=generate1(r)
  o=[]
  stry=[]
  w=[]
  for i in range(50):
    o+=[r[i*25:(i+1)*25]]
  for j in range(len(o)):
    for z in range(25):
      if o[j][z]!=1:
        stry+=['.']
      else:
        stry+=['█']
    w+=[stry]
    stry=[]
  w[11][0]="S"
  w[27][-1]="F"
  #print(w)
  st=''
  Q=[]
  f = open(ccskrf, "w", encoding="utf-8")
  for ip in range(50):
    for ie in range(25):
      st+=str(w[ip][ie])
    Q+=[st]
    st=''
  #print(Q)
  f.writelines(line+'\n' for line in Q)
  f.close()
  return f
print(create("/content/untitled"))
