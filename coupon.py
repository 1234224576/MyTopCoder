def selectOptimumCoupon(total,fiveCoupon,twoCoupon,oneCoupon):
	if(total <= 1000): return (0,0,0)

	minVal = total
	result = []

	for i in range(fiveCoupon+1):
		for j in range(twoCoupon+1):
			for k in range(oneCoupon+1):
				t = total - (i*500 + j*200 + k*100)
				if(t <= 0): continue
				if(t != minVal and minVal > t):
					result = []
				if(t <= total and minVal >= t):
					minVal = t
					result.append((i,j,k))
	ans = result[0]
	for x in result:
		if sum(ans) > sum(x):
			ans = x
	return ans

def test():
	print("correct" if selectOptimumCoupon(1000,2,1,3) == (0,0,0) else "failed")
	print("correct" if selectOptimumCoupon(1210,0,0,0) == (0,0,0) else "failed")
	print("correct" if selectOptimumCoupon(1210,2,1,3) == (2,1,0) else "failed")
	print("correct" if selectOptimumCoupon(1530,2,1,3) == (2,1,3) else "failed")

	print("correct" if selectOptimumCoupon(2130,10,10,10) == (4,0,1) else "failed")
	print("correct" if selectOptimumCoupon(34520,100,100,100) == (69,0,0) else "failed")
	print("correct" if selectOptimumCoupon(0,2,1,3) == (0,0,0) else "failed")
test()