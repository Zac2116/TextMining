

def ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])


def featureGenerate(title,description,searchItem):
	t = ngrams(title,1)
	s = ngrams(searchItem,1)
	d = ngrams(description,1)

	jc1_1 = jCDistance(t,s)
	jc1_2 = jCDistance(t,d)
	jc1_3 = jCDistance(s,d)

	t2 = ngrams(title,2)
	s2 = ngrams(searchItem,2)
	d2 = ngrams(description,2)

	jc2_1 = jCDistance(t2,s2)
	jc2_2 = jCDistance(t2,d2)
	jc2_3 = jCDistance(s2,d2)


	result = [jc1_1,jc1_2,jc1_3,jc2_1,jc2_2,jc2_3]
	return result


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


import pandas as pd
data = pd.read_csv("~/Desktop/train_clean.csv")
df = pd.DataFrame(columns = ['product_uid','ts1_1','td1_2','sd1_3','ts2_1','td2_2','sd2_3'])

for i in range(1,2): #len(data)
	#descriptions
	id = data.iloc[i][1]
	d_l = data.iloc[i]['desList'][1:][:-1].split(", ")
	t_l = data.iloc[i]['productList'][1:][:-1].split(", ")
	s_l = data.iloc[i]['searchList'][1:][:-1].split(", ")
	print(d_l)
	print(t_l)
	print(s_l)
	cur_row = featureGenerate(t_l,d_l,s_l)
	df2 = pd.Series([id]+cur_row, index=['product_uid','ts1_1','td1_2','sd1_3','ts2_1','td2_2','sd2_3'])
	df = df.append(df2, ignore_index=True)
	df.to_csv("~/Desktop/distanceFeature.csv")



