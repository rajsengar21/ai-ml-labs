import numpy as np
x=np.array(([2,9],[1,5],[3,6]),dtype=float)
print(x)
y=np.array([92],[86],[89]),dtype=float)
print(y)
x=x/np.amax(x,axis=0)
y=y/100
print(x)
print(y)
def sigmoid(x):
    return 1/(1+np.exp(-x))
def derivatives_sigmoid(x):
    return x*(1-x)
              
epoch=50000
lr=0.001
inputlayer_neurons=2
hiddenlayer_neurons=4
outputlayer_neurons=1
wh=np.random,uniform(size=(inputlayer_neurons,hiddenlayerr_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,outputlayer_neurons))
bout=np.random.uniform(size=(1,outputlayer_neurons))
for i in range(epoch):
    hinp1=np.dot(x,wh)
    hinp=hinp1+bh
    hlayer_act=sigmoid(hinp)

    outinp1=np.dot(x,wout)
    outinp=outinp1+bout
    output=sigmoid(outinp)

    EO=y-output
    outgrad=deritives_sigmoid(output)
    d_output=EO*outgrad

    EH=d_output.dot(wout.T)
    hiddengrad=derivatives_sigmoid(hlayer_act)
    d_hiddenlayer=
    

    
    
    


            
        
