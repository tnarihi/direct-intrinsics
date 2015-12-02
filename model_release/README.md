# Direct Intrinsics

Model release of our ICCV 2015 paper for BVLC CAFFE framework:

    Takuya Narihira, Michael Maire, and Stella X. Yu. Direct Intrinsics: Learning Albedo-Shading Decomposition by Convolutional Regression. International Conference on Computer Vision, 2015
	
See *.ipynb in IPython notebook for example usage.
There are some hard-coded paths to Caffe and images.
You have to modify them to fit your environment.
The models run on [master of CAFFE](https://github.com/BVLC/caffe/commit/6232dfcd1422077304fbf50b00afe24c5a0427ee).

### Model files

* sintel_final_train.caffemodel: `MSCR+dropout+deconv+DA+GenMIT` for Sintel prediction.
Trained on our training split.
* sintel_final_test.caffemodel: `MSCR+dropout+deconv+DA+GenMIT` for Sintel prediction.
Trained on our testing split.
* mit_final_barron_train.caffemodel: `Ours + ResynthSintel` for MIT prediction.
Trained on training set of Barron's split.
