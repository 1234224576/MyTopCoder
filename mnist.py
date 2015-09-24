import data
import matplotlib.pyplot as plt
import numpy as np
from chainer import cuda, Function, FunctionSet, gradient_check, Variable, optimizers, utils
import chainer.functions as F
mnist =  data.load_mnist_data()

x_all = mnist['data'].astype(np.float32) / 255
y_all = mnist['target'].astype(np.int32)
x_train, x_test = np.split(x_all, [60000])
y_train, y_test = np.split(y_all, [60000])

model = FunctionSet(
	l1 = F.Linear(784, 100),
    l2 = F.Linear(100, 100),
    l3 = F.Linear(100,  10),
)

optimizer = optimizers.SGD()
optimizer.setup(model)

def forward(x_data, y_data):
	x = Variable(x_data)
	t = Variable(y_data)
	h1 = F.relu(model.l1(x))
	h2 = F.relu(model.l2(h1))
	y = model.l3(h2)
	return F.softmax_cross_entropy(y, t), F.accuracy(y, t)


batchsize = 100
datasize = 60000  
for epoch in range(20):
	print('epoch %d' % epoch)
	indexes = np.random.permutation(datasize)
	for i in range(0, datasize, batchsize):
		x_batch = x_train[indexes[i : i + batchsize]]
		y_batch = y_train[indexes[i : i + batchsize]]

		optimizer.zero_grads()
		loss, accuracy = forward(x_batch, y_batch)
		loss.backward()
		optimizer.update()

sum_loss, sum_accuracy = 0, 0
for i in range(0, 10000, batchsize):
	x_batch = x_test[i : i + batchsize]
	y_batch = y_test[i : i + batchsize]
	loss, accuracy = forward(x_batch, y_batch)
	sum_loss      += loss.data * batchsize
	sum_accuracy  += accuracy.data * batchsize

mean_loss     = sum_loss / 10000
mean_accuracy = sum_accuracy / 10000

print("loss:",mean_loss)
print("actualy:",mean_accuracy)

plt.style.use('fivethirtyeight')
def draw_digit3(data, n, ans, recog):
    size = 28
    plt.subplot(10, 10, n)
    Z = data.reshape(size,size)   # convert from vector to 28x28 matrix
    Z = Z[::-1,:]             # flip vertical
    plt.xlim(0,27)
    plt.ylim(0,27)
    plt.pcolor(Z)
    plt.title("ans=%d, recog=%d"%(ans,recog), size=8)
    plt.gray()
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")


plt.figure(figsize=(15,15))

cnt = 0
for idx in np.random.permutation(60000)[:100]:

    xxx = x_train[idx].astype(np.float32)
    h1 = F.dropout(F.relu(model.l1(Variable(xxx.reshape(1,784)))),  train=False)
    h2 = F.dropout(F.relu(model.l2(h1)), train=False)
    y  = model.l3(h2)
    cnt+=1
    draw_digit3(x_train[idx], cnt, y_train[idx], np.argmax(y.data))
plt.show()



