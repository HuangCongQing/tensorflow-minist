import os
import input_data  # 进行下载数据
from tensorflow.examples.tutorials.mnist import input_data
# import tensorflow as tf
# import model
# 下载数据
data = input_data.read_data_sets('MNIST_data/', one_hot = True)   # 进行下载数据，下载到目录MNIST_data/

