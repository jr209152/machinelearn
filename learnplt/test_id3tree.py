import matplotlib.pyplot as plt
from ID3DTree import *
dtree = ID3DTree()
dtree.loadDataSet("dataset.dat",["age","revenue","student","credit"])
dtree.train()
print dtree.tree
