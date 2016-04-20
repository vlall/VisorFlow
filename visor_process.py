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
        #  Second parameter is color channels
        read_input = tf.image.decode_jpeg(value, 1)
        resized = tf.image.resize_images(read_input, height, width)
        #  resized.set_shape([height, width, 1])
        #  Remove size 1 dimensions...
        resized = tf.squeeze(resized)
        # This flattens out a tensor to 1 Dimension... resized = tf.reshape(resized, [-1])
        print resized
        #preprocess = tf.image.random_brightness(resized,.2)
        return resized


def main():
    cwd = os.getcwd()
    with tf.Graph().as_default():
        #  Example data set
        imageList = ['face1.jpg']
        imageListFull = ['data/raw/' + i for i in imageList]
        #  Change Dimenstions 28x28...
        imageOps = VisorFix(imageListFull)
        editImage = imageOps.edit_image(500, 500)
        image = imageOps.filename, imageOps.edit_image(500, 500)
        init = tf.initialize_all_variables()
        sess = tf.Session()
        sess.run(init)
        tf.train.start_queue_runners(sess=sess)
        for i in imageList:
            filename, img = sess.run(image)
            print img
            print filename
            img = Image.fromarray(img, "L")
            img.save(os.path.join(cwd + "/data/training/" + str(i)))
            print ("Images saved")


if __name__ == "__main__":
    main()
