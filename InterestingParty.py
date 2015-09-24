def party(first,second):
	maxCount = 0
	topics = first + second
	memo = {}
	for topic in topics:
		if topic not in memo:
			count = 0
			for i in range(len(first)):
				if first[i] == topic or second[i] == topic:
					count+=1
			memo[topic] = count
			if maxCount < count:
				maxCount = count
	return maxCount

def test():
	first = ["f","g","s","f"]
	second = ["h","f","f","b"]
	print("correct" if party(first,second) == 4 else "failed")
	first = ["va","di","lo","co"]
	second = ["ta","sp","dis","me"]
	print("correct" if party(first,second) == 1 else "failed")
	first = ["sn","pr","co","mo"]
	second = ["py","py","an","py"]
	print("correct" if party(first,second) == 3 else "failed")
	first = ["t","o","p","c","o","d","e","r","s","i","n","g","l","e","r","o","u","n","d","m","a","t","c","h","f","o","u","r","n","i"]
	second = ["n","e","f","o","u","r","j","a","n","u","a","r","y","t","w","e","n","t","y","t","w","o","s","a","t","u","r","d","a","y"]
	print("correct" if party(first,second) == 6 else "failed")
test()