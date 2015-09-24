def cryptography(inputs):
	minNum = min(inputs)
	for i in range(len(inputs)):
		if inputs[i] == minNum:
			inputs[i] += 1
			break

	ans = 1
	for i in inputs:
		ans *= i
	return ans

def test():
	print("correct" if cryptography([1,2,3]) == 12 else "failed")
	print("correct" if cryptography([1,3,2,1,1,3]) == 36 else "failed")
	print("correct" if cryptography([1000,999,998,997,996,995]) == 986074810223904000 else "failed")
	print("correct" if cryptography([1,1,1,1]) == 2 else "failed")
test()