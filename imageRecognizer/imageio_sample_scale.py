# coding:utf-8
import sys
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import matplotlib.cm as cm

template_path = "1.png"
target_path = "mandrill.png"

def compute_score_map(template,target):
	th,tw = template.shape
	score_map = np.zeros(shape=(target.shape[0] - th,target.shape[1] - tw))

	for y in range(score_map.shape[0]):
		for x in range(score_map.shape[1]):
			diff = target[y:y + th,x:x + tw] - template
			score_map[y,x] = np.square(diff).sum()
	return score_map

def main():

	template = io.imread(template_path,as_grey = True)
	target = io.imread(target_path,as_grey = True)

	score_maps = []
	scale_factor =  2.0 ** (-1.0/8.0)
	target_scaled = target + 0
	for s in range(8):
		score_maps.append(compute_score_map(template,target_scaled))
		target_scaled = transform.rescale(target_scaled,scale_factor)
	score,s,(x,y) = min([(np.min(score_map),s,np.np.unravel_index(np.argmin(score_map),score_map.shape))
					for s,score_map in enumerate(score_maps)])



# x,y = np.unravel_index(np.argmin(score_map),score_map.shape)

	fig,(ax1,ax2,ax3) = plt.subplots(ncols=3,figsize=(8,3))
	ax1.imshow(template,cmap=cm.Greys_r)
	ax1.set_axis_off()
	ax1.set_title('template')

	ax2.imshow(target,cmap=cm.Greys_r)
	ax2.set_axis_off()
	ax2.set_title('target')
	ax2.add_patch(plt.Rectangle((y,x),tw,th,edgecolor='w',facecolor='none',linewidth=2.5))

	ax3.imshow(score_map,cmap=cm.Greys_r)
	ax3.set_axis_off()
	ax3.set_title('score_map')
	ax3.add_patch(plt.Rectangle((y-th/2,x-tw/2),tw,th,edgecolor='w',facecolor='none',linewidth=2.5))
	plt.show()

if __name__ == '__main__':
	main()