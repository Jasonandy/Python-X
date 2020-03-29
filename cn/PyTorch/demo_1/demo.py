# coding=utf-8
import torch
import torch.nn as nn
from torch.autograd import Variable

m = nn.LeakyReLU(0.1)
input = Variable(torch.randn(2))
print(input)
print
'---' * 10
print(m(input))
print
'--' * 10
r = nn.ReLU()
print
r(input)

m = nn.Threshold(0.1, 20)
input = Variable(torch.randn(2))
print(input)
print(m(input))

m = nn.Sigmoid()
input = Variable(torch.randn(2))
print(input)
print(m(input))

m = nn.BatchNorm1d(3, affine=False)
input = Variable(torch.randn([[1, 2, 3], [4, 5, 6]]))
output = m(input)
print
output
print
input

rnn = nn.RNN(10, 20, 2)  # input_size,hidden_size,num_layers
input = Variable(torch.randn(5, 3, 10))  # seq_len,batch,input_size
h0 = Variable(torch.randn(2, 3, 20))  # num_layers * num_direction,batch,hidden_size
output, hn = rnn(input, h0)
print
output  # 5*3*20  seq_len ,batch  , hidden_size * num_directions
print
'--' * 10
print
hn
