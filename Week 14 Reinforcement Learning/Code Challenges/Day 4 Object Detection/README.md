# Object Detection

In this challenge you'll build a very simple implementation of object detection
and localization. You'll build on the material you covered in the unit on
convolutional neural networks, using pretrained CNNs from the Keras library and
basic image manipulation. The project proceeds in three steps:

## Step 1

Build a function `contains_banana(img)` that takes in an image `img`, resizes
it to 224x224, and returns a float describing the confidence with which Keras
believes the image contains a banana. Do this using the Keras pretrained
ResNet50 architecture. If "banana" is in ResNet50's top-3 results for the image,
report the corresponding reported probability. Otherwise, return 0.0. To test
that this function works, you should apply it to the examples in the
`sample_data` folder.


## Step 2

Build a function `crop_image(img, quadrant)` that takes in an image `img` and a
parameter `quadrant` in `["TL", "TR", "BL", "BR"]` and returns the top left 2/3
x 2/3, the top left, the top right, the bottom left, or the bottom right,
depending on the parameter value. To visualize this partitioning, imagine that
we lay a tic tac toe board over the image. Then the TL partition corresponds to
the roughly 67% of the image lying in the top-left-most four squares.

## Step 3

Now combine the results of steps 1 and 2 to build the function
`find_banana(img)`. If the image argument doesn't contain a banana, the function
should return the string `None`. If it does contain a banana, the function
should return either `"TL"`, `"TR"`, `"BL"`, `"BR"`, or `"C"` (for "center")
depending on whether one of the four partitions or the original image has the
highest banana probability (according to ResNet50).

## Stretch goals

The function `crop_image` should complain if the parameter `quadrant` isn't one
of `["TL", "TR", "BL", "BR"]`. Modify the function slightly so that it throws an
appropriate error if an invalid quadrant is passed.

Write unit tests to make sure that `contains_banana` correctly finds that each
image in `sample_data/positive_examples` contains a banana and each image in
`sample_data/negative_examples` does not.

## Other notes

For resources discussing object detection see:

- [Original YOLO paper](https://pjreddie.com/media/files/papers/yolo.pdf)
- [YOLO for Object Detection explained](https://medium.com/diaryofawannapreneur/yolo-you-only-look-once-for-object-detection-explained-6f80ea7aaa1e)
- [How computers learn to recognize objects instantly (Joshua Redmon, TED)](https://youtu.be/Cgxsv1riJhI)


For reference on ResNet50, see:
https://www.pyimagesearch.com/2017/03/20/imagenet-vggnet-resnet-inception-xception-keras/

For example usage, see: https://keras.io/applications/
