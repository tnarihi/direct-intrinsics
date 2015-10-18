import numpy as np
import cv2

# Sintel scene names
sintel_scenes = dict(
    train=['alley_1', 'bamboo_1', 'bandage_1', 'cave_2', 'market_2', 'market_6', 'shaman_2', 'sleeping_1', 'temple_2'],
    test=['alley_2', 'bamboo_2', 'bandage_2', 'cave_4', 'market_5', 'mountain_1', 'shaman_3', 'sleeping_2', 'temple_3'])

# MIT object names
mit_objects = dict(
    train=['apple', 'box', 'cup1', 'dinosaur', 'frog1', 'panther', 'paper1', 'phone', 'squirrel', 'teabag2'],
    test=['cup2', 'deer', 'frog2', 'paper2', 'pear', 'potato', 'raccoon', 'sun', 'teabag1', 'turtle'])

# Mean BGR values of input
mean_bgr = np.array([104, 117, 123], dtype=np.float)

def get_pad_multiple_32(shape):
    # Get pad values for y and x axeses such that an image
    # has a shape of multiple of 32 for each side
    def _f(s):
        n = s // 32
        r = s % 32
        if r == 0:
            return 0
        return 32 - r
    return _f(shape[0]), _f(shape[1])

def bgr2rgb(img):
    # Convert an BGR image to RGB
    return img[..., ::-1]

def minmax_01(img):
    # Put values in a range of [0, 1]
    ma, mi = img.max(), img.min()
    return (img - mi) / (ma - mi)

def unpad_img(img, pad):
    # Crop an image according to pad, used in post_process
    y = img.shape[0] - pad[0]
    x = img.shape[1] - pad[1]
    return img[:y, :x, :]

def post_process(img, pad, i=0):
    # Post processes of Direct intrinsics net.
    # The output of direct intrinsics net is in log domain with bias +0.5, and in BGR order.
    return unpad_img(minmax_01(bgr2rgb((np.exp(img[i]) - 0.5).transpose(1, 2, 0))), pad)

def predict(net, img):
    # Predicting function

    # Pad an image so that it has a shape of a multiple of 32
    pad = get_pad_multiple_32(img.shape)
    pad_img = cv2.copyMakeBorder(img, 0, pad[0], 0, pad[1], cv2.BORDER_CONSTANT)
    # Reshape and fill input with the image
    net.blobs['data'].reshape(1, 3, *pad_img.shape[:2])
    net.blobs['data'].data[0, ...] = np.rollaxis(pad_img - mean_bgr, 2)
    # Predict and get the outputs albedo and shading
    out = net.forward()
    a = out['out-albedo'].copy()
    s = out['out-shading'].copy()
    # Appy post processes before returning
    return post_process(a, pad), post_process(s, pad)
