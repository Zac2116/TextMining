def jCDistance(A,B):
	#A intersect B / (A union B) 
	#A: list
	#B: list

	deno = set(A) & set(B)
	nom = set(A) | set(B)

	jC = len(deno) / float(len(nom))
	return jC