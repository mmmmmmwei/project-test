"""
Title: Image classification from scratch
Author: [fchollet](https://twitter.com/fchollet)
Date created: 2020/04/27
Last modified: 2020/04/28
Description: Training an image classifier from scratch on the Galaxy Zoo dataset to classify early type galaxy and late type galaxy.
"""
"""
## Introduction

This example shows how to do image classification from scratch, starting from JPEG
image files on disk, without leveraging pre-trained weights or a pre-made Keras
Application model. We demonstrate the workflow on the Galaxy Zoo
 classification dataset.

we use Keras image preprocessing layers for image standardization and data augmentation.
"""

"""
## Setup
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

"""
## Load the data: class 1 = Early type galaxy | class 0 = Late type galaxy
"""
root_path = 'D:\\Master\\Galaxy Zoo dataset\\small dataset folder\\'
input_file_name = 'image folder for small dataset'
#file_path = "".join([root_path,"input_file_name",".zip"])
#!unzip file_path -d root_path

# Create image directory path
#image_dir = os.path.join(root_path)
image_dir = "".join([root_path, input_file_name])

"""
Now we have a `Images` folder which contain two subfolders, `class 1` and `class 0`. Each
 subfolder contains image files for each category.
"""

"""
## Generate a `Dataset`
"""

image_size = (300, 300)
batch_size = 32

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    image_dir,
    validation_split=0.3,
    subset="training",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    image_dir,
    validation_split=0.3,
    subset="validation",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

"""
## Visualize the data

Here are the first 9 images in the training dataset. As you can see, label 1 is "early type galaxy"
 and label 0 is "late type galaxy".
"""

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")
plt.show(block=False)
input('press <ENTER> to continue')

"""
# ## Using image data augmentation

# When you don't have a large image dataset, it's a good practice to artificially
# introduce sample diversity by applying random yet realistic transformations to the
# training images, such as random horizontal flipping or small random rotations. This
# helps expose the model to different aspects of the training data while slowing down
#  overfitting.
# """

data_augmentation = keras.Sequential(
    [
        layers.experimental.preprocessing.RandomFlip("horizontal"),
        layers.experimental.preprocessing.RandomRotation(0.1),
    ]
)

"""
Let's visualize what the augmented samples look like, by applying `data_augmentation`
 repeatedly to the first image in the dataset:
"""

plt.figure(figsize=(10, 10))
for images, _ in train_ds.take(1):
    for i in range(9):
        augmented_images = data_augmentation(images)
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(augmented_images[0].numpy().astype("uint8"))
        plt.axis("off")
plt.show(block=False)
input('press <ENTER> to continue')        
