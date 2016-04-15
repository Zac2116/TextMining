import pandas as pd
data = pd.read_csv("~/Desktop/train.csv")
des = pd.read_csv("~/Desktop/product_descriptions.csv")
df = pd.DataFrame(columns = ['product_uid','jc1','jc2','jc3','dd1','dd2','dd3'])

for i in range(1,len(data)):
	#descriptions
	id = data.iloc[i][1]
	if id in des['product_uid']:
		d = des[des['product_uid']==id]
		d_l = d['product_description'].iloc[0].split(" ")
	else:
		d_l = []

	t_l = data.iloc[i][2].split(" ")
	s_l = data.iloc[i][3].split(" ")

	cur_row = featureGenerate(t_l,d_l,s_l)
	df2 = pd.Series([id]+cur_row, index=['product_uid','jc1','jc2','jc3','dd1','dd2','dd3'])
	df = df.append(df2, ignore_index=True)

	df.to_csv("distanceFeature.csv")


def featureGenerate(title,description,searchItem,i=2):
	t = ngrams(title,i)
	s = ngrams(searchItem,i)
	d = ngrams(description,i)

	jc1 = jCDistance(t,s)
	jc2 = jCDistance(t,d)
	jc3 = jCDistance(s,d)

	dd1 = DicDist(t,s)
	dd2 = DicDist(t,d)
	dd3 = DicDist(s,d)

	result = [jc1,jc2,jc3,dd1,dd2,dd3]
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

