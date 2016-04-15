def jCDistance(A,B):
	#A intersect B / (A union B) 
	#A: list
	#B: list

	deno = set(A) & set(B)
	nom = set(A) | set(B)

	jC = len(deno) / float(len(nom))
	return jC


def DicDist(A,B):
	#size(2 times intersection of A and B )/ size(((A) + (B)))
	deno = set(A) & set(B)
	nom = len(set(A)) + len(set(B))
	DD = len(deno)/float(nom)
	return DD