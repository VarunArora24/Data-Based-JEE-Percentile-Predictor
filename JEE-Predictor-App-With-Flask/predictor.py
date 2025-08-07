import math
def sigmoid(z):
    return 1/(1+math.exp(-z))
data=[(120,93),(180,98),(200,99)]
w1=0.1
bias=-0.1
lr=0.01
for epoch in range(10001):
    total_loss=0
    for marks,y in data:
        z=(marks*w1)/300+bias
        pred=sigmoid(z)
        error=pred-y
        dz=error*pred*(1-pred)
        w1 -= lr * dz * marks
        bias-=lr*dz
print(f"Trained weights: w1 = {w1:.4f}, bias = {bias:.4f}")
a=int(input('enter marks'))
c=w1*a/300+bias
value=sigmoid(c)
print(value*100)

