def ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])