# Caffe prototxt for training direct intrinsics

To run training, you need tnarihi's Caffe branch.

* [tnarihi's Caffe branch](https://github.com/tnarihi/caffe/tree/future): Mostly extended for running PythonLayer on GPU even with Theano. 
* [GPU Layer implementation in PythonLayer](https://github.com/tnarihi/tnarihi-caffe-helper): You need to install some Python packages for running GPU computation in Python (PyCUDA, Scikits-CUDA, Theano etc.).

We recommend you to initialize weights in scale 1 BVLC Caffe reference net (conv1-conv5) by learned weights on ImageNet (provided in model zoo).
Note that you have to modify train_val.prototxt to point right paths to your dataset.
