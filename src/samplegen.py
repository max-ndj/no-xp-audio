from __future__ import unicode_literals, print_function, division
from io import open
from glob import glob
import os
import unicodedata
import string
import random
import time
import math
import torchaudio
import torch
import torch.nn as nn

# Retrieve categories
categories = [os.path.basename(path) for path in glob('data/samples/*')]
n_categories = len(categories)
dataset = {category: glob("data/samples/" + category + "/*.wav") for category in categories}

chunk_size = 128

print("Categories: ", categories)

# Retrieves a random element from the given list
def randItem(l):
    return l[random.randint(0, len(l) - 1)]

def timeSince(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

# One-hot vector for category
def categoryTensor(category):
    index = categories.index(category)
    tensor = torch.zeros(1, n_categories, dtype=torch.Long)
    tensor[0][index] = 1
    return tensor

# Input and output matrices of first to last samples (not including EOS) for input
def ioTensors(filepath):
    waveform, sample_rate = torchaudio.load(filepath)

    left = waveform[0]
    length = len(left)
    padded_size = ((length - 1) // chunk_size + 1) * chunk_size
    padded = torch.cat((left, torch.zeros(padded_size - length)))

    inputmat = torch.reshape(padded, (-1, chunk_size))
    outputmat = torch.cat((*inputmat[1:], torch.zeros(chunk_size)), 0)
    return inputmat, outputmat

def randomTrainingPair():
    category = randItem(categories)
    filename = os.path.basename(randItem(dataset[category]))
    return category, filename

# Make category, input, and target tensors from a random category, file pair
def randomTrainingExample():
    category, filename = randomTrainingPair()
    category_tensor = categoryTensor(category)
    input_tensor, output_tensor = ioTensors("data/samples/" + category + "/" + filename)
    return category_tensor, input_tensor, output_tensor

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size

        self.i2h = nn.Linear(n_categories + input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(n_categories + input_size + hidden_size, output_size)
        self.o2o = nn.Linear(hidden_size + output_size, output_size)
        self.dropout = nn.Dropout(0.1)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, category, input, hidden):
        input_combined = torch.cat((category, torch.unsqueeze(input, 0), hidden), 1)
        hidden = self.i2h(input_combined)
        output = self.i2o(input_combined)
        output_combined = torch.cat((hidden, output), 1)
        output = self.o2o(output_combined)
        output = self.dropout(output)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)

rnn = RNN(chunk_size, chunk_size * 4, chunk_size)
criterion = nn.NLLLoss()
n_iters = 10000
print_every = 1000
learning_rate = 0.0005
all_losses = []
total_loss = 0 # Reset every plot_every iters

start = time.time()

def train(category_tensor, input_tensor, output_tensor):
    output_tensor.unsqueeze_(-1)
    hidden = rnn.initHidden()

    rnn.zero_grad()

    loss = 0

    for i in range(input_tensor.size(0)):
        output, hidden = rnn(category_tensor, input_tensor[i], hidden)
        print("criterion ", output, output_tensor[i])
        loss += criterion(output, output_tensor[i])

    loss.backward()

    for p in rnn.parameters():
        p.data.add_(p.grad.data, alpha=-learning_rate)

    return output, loss.item() / input_tensor.size(0)

for i in range(1, n_iters + 1):
    output, loss = train(*randomTrainingExample())
    total_loss += loss

    if i % print_every == 0:
        print('%s (%d %d%%) %.4f' % (timeSince(start), i, i / n_iters * 100, loss))

    if i % plot_every == 0:
        all_losses.append(total_loss / plot_every)
        total_loss = 0
