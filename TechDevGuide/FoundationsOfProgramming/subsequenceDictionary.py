def function(S,D):
	maxi = ""
	for word in D:
		if(len(word) < len(S)):
			if checkWord(S,word) and len(maxi) < len(word):
				maxi = word
	print(maxi)
	

def checkWord(S,word):
	sIndex = 0
	wordIndex = 0
	while(wordIndex < len(word)):
		while (sIndex < len(S)) and (S[sIndex] != word[wordIndex]):
			# print(word[wordIndex], S[sIndex])
			sIndex+=1
		if(sIndex == len(S)):
			return False
		wordIndex+=1
		sIndex+=1
		
	return True

def preprocess(S):
	indices = dict()
	for x in range(len(S)):
		char = S[x]
		if(char in indices):
			indices[char].append(x)
		else:
			indices[char] = [x]
	return indices

def checkWordPreprocessed(indices,word):
	sIndex = 0
	wordIndex = 0
	while(wordIndex < len(word)):
		if word[wordIndex] not in indices:
			return False
		else:
			l = indices[word[wordIndex]]
			index = 0
			while index < len(l) and l[index] < sIndex:
				index+=1
			if(index == len(l)):
				return False
			sIndex = l[index]
		wordIndex+=1
	return True

def preprocessDictionary(S,D):
	paralellize = dict()
	for w in D:
		if w[0] not in paralellize:
			paralellize[w[0]] = [[w, 0]]
		else:
			paralellize[w[0]].append([w, 0])

	paralellize["special"] = []

	for char in S:
		if char in paralellize:
			for tup in paralellize[char]:
				tup[1]= tup[1]+1
				if tup[1] == len(tup[0]):
					paralellize["special"].append(tup[0])
				elif tup[0][tup[1]] not in paralellize:
					paralellize[tup[0][tup[1]]] = [tup]
				else:
					paralellize[tup[0][tup[1]]].append(tup)
			paralellize[char] = []

	print(max(paralellize["special"]))









S = "abppplee"
D = ["able", "ale", "apple", "bale", "kangaroo"]
# function(S,D)

preprocessDictionary(S,D)
# print(checkWordPreprocessed(preprocess(S), D[4]))
