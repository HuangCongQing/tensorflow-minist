# tensorflow-minist
TensorFlow与Flask结合打造手写体数字识别

视频学习网站：https://www.imooc.com/learn/994

environments：python3.5 win764位

课程目录
* TensorFlow框架介绍
* MNIST数据集及模型建立
* Flask框架建立
* MNIST模型与FLask框架整合

```
// 主要目录
mnist
        │  convolutional.py
        │  input_data.py
        │  model.py
        │  regression.py
        │
        ├─data
        │      regression.ckpt.data-00000-of-00001
        │      regression.ckpt.index
        │
        ├─MNIST_data
        │      t10k-images-idx3-ubyte.gz
        │      t10k-labels-idx1-ubyte.gz
        │      train-images-idx3-ubyte.gz
        │      train-labels-idx1-ubyte.gz



├─src
        │  └─js
        │          main.js
        │
        ├─static
        │  ├─css
        │  │      bootstrap.min.css
        │  │
        │  └─js
        │          echarts.all.js
        │          echarts.common.min.js
        │          echarts.min.js
        │          jquery.min.js
        │          main.js
        │
        └─templates
                index.html
```


1. [基础知识](./base.md)

* [flask入门](http://docs.jinkan.org/docs/flask/quickstart.html#a-minimal-application)

### error

AttributeError: module 'input_data' has no attribute 'read_data_sets'