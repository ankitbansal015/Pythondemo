s=set()
#print(type(s))
#s_from_list={2,4,6,5,7,}
#print(s_from_list)
#print(type(s_from_list))
s.add(2)
s.add(6)
s1=s.union({3,9})
s2=s.intersection({1,6,5,9})
print(s,s1,s2)
print(len(s2))
print(type(s1))
print(min(s))
print(max(s2))
print(s.isdisjoint(s1))
s.remove(2)
print(s)