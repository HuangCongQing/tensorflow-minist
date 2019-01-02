from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip # 解压
import os  # 系统文件
import tempfile  # 模板文件

import numpy
from six.moves import urllib
from six.moves import xrange
import tensorflow as tf
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets