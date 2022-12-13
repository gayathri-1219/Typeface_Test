d={"bfpv":"1","cgjkqsxz":"2","dt":"3","l":"4","mn":"5","r":"6","aeiouhwy":"."}
def codegeneration(s):
	global d
	s=s.lower()
	c=s[0]
	s=s[1:]
	for i in s:
		for k in d.keys():
			if i in k:
				code=d[k]
				if code!=".":
					if code!=c[-1]:
						c+=code
	
	return c

s=str(input())                           #input string
k = codegeneration(s)
print(k)
l = list(map(str,input().split()))       #input list of combinations of phonetic words
for i in l:
	if codegeneration(i)==k:
		print(i)
		
#input:
#Murthy
#Moorthi Murthi Moorthi Mothy Muoothi
#Output:
#Moorthi
#Murthi
#Moorthi
