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
├─mnist
        │  convolutional.py// 卷积模型
        │  input_data.py  //下载数据集，官网上也有，其他py文件可以调用此文件进行下载数据
        │  model.py       // 两个模型初始化
        │  regression.py  // 线性回归模型
        │
        ├─data
        │      regression.ckpt.data-00000-of-00001
        │      regression.ckpt.index
        │
        ├─MNIST_data  // 下载的数据集
        │      t10k-images-idx3-ubyte.gz
        │      t10k-labels-idx1-ubyte.gz
        │      train-images-idx3-ubyte.gz
        │      train-labels-idx1-ubyte.gz

├─main.py   // flask,制作接口

├─src              // 前端代码
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
                index.html   // 前端界面显示入口
```


1. [基础知识](./base.md)

* [flask入门](http://docs.jinkan.org/docs/flask/quickstart.html#a-minimal-application)

### error

AttributeError: module 'input_data' has no attribute 'read_data_sets'