import os
import tensorflow as tf
import numpy as np
from PIL import Image


class VisorFix(object):
    """
    Format data in TensorFlow before training
    """

    def __init__(self, filenames):
        self.filenames = filenames

    def edit_image(self, height, width):
        filename_queue = tf.train.string_input_producer(self.filenames)
        self.filename, value = tf.WholeFileReader().read(filename_queue)
        read_input = tf.image.decode_jpeg(value)
        resized = tf.image.resize_images(read_input, height, width, 1)
        print resized
        resized.set_shape([height, width, 3])
        #  resized = tf.image.rgb_to_grayscale(resized)
        print resized
        preprocess = tf.image.flip_up_down(resized)
        #  preprocess = tf.image.random_brightness(resized,.2)
        self.preprocess = preprocess
        return preprocess


def main():
    cwd = os.getcwd()
    with tf.Graph().as_default():
        #  Example data set
        imageList = ['face1.jpg', 'face2.jpg']
        imageListFull = ['data/raw/' + i for i in imageList]
        #  Change Dimenstions 28x28... Do tranformation...
        imageOps = VisorFix(imageListFull)
        imageOps.edit_image(500, 500)
        image = imageOps.filename, imageOps.preprocess
        init = tf.initialize_all_variables()
        sess = tf.Session()
        sess.run(init)
        tf.train.start_queue_runners(sess=sess)
        for i in imageList:
            filename, img = sess.run(image)
            print(filename)
            img = Image.fromarray(img, "RGB")
            img.save(os.path.join(cwd + "/data/training/" + str(i)))


if __name__ == "__main__":
    main()
