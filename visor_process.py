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
        self.filename, read_input = self.open_image(filename_queue)
        resized = tf.image.resize_images(read_input, height, width, 1)
        resized.set_shape([height, width, 3])
        flipped = tf.image.flip_up_down(resized)
        self.flipped = flipped
        return flipped

    def open_image(self, filename_queue):
        reader = tf.WholeFileReader()
        key, value = reader.read(filename_queue)
        image = tf.image.decode_jpeg(value)
        return key, image

    def inputs(self):
        return self.filename, self.flipped


def main():
    cwd = os.getcwd()
    with tf.Graph().as_default():
        #  Example data set
        imageList = ['face/face1.jpg', 'face/face2.jpg']
        #  Change Dimenstions 28x28... Do tranformation...
        imageOps = VisorFix(imageList)
        imageOps.edit_image(28, 28)
        image = imageOps.inputs()
        init = tf.initialize_all_variables()
        sess = tf.Session()
        sess.run(init)
        tf.train.start_queue_runners(sess=sess)
        for i in imageOps.filenames:
            filename, img = sess.run(image)
            print(filename)
            img = Image.fromarray(img, "RGB")
            img.save(os.path.join(cwd+"/training/"+str(i)))


if __name__ == "__main__":
    main()
