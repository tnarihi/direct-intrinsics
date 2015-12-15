# Caffe prototxt for training direct intrinsics

To run training, you need tnarihi's Caffe branch.

* [tnarihi's Caffe branch](https://github.com/tnarihi/caffe/tree/future): Mostly extended for running PythonLayer on GPU even with Theano. 
* [GPU Layer implementation in PythonLayer](https://github.com/tnarihi/tnarihi-caffe-helper): You need to install some Python packages for running GPU computation in Python (PyCUDA, Scikits-CUDA, Theano etc.).

The above dependencies are contained in [modified_caffe](../modified_caffe) as submodules. You can initiazile them by `git submodule update --init modified_caffe/{caffe,caffe_helper}` from toplevel of the workingtree.


We recommend you to initialize weights in scale 1 BVLC Caffe reference net (conv1-conv5) by learned weights on ImageNet (provided in model zoo).
Note that you have to modify train_val.prototxt to point right paths to your dataset. You can create datset from [../data](../data).
