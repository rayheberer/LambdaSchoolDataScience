import numpy as np

from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions

from skimage.transform import resize
from skimage.io import imread, imshow

model = ResNet50()

def contains_banana(img):
    rescaled = resize(img, (224, 224), mode='constant')
    
    processed = preprocess_input(rescaled, mode='tf')
    batch = np.expand_dims(processed, 0)
    
    predictions = decode_predictions(model.predict(batch))

    top_pred, top_score = predictions[0][0][1], predictions[0][0][2]
    
    if top_pred == 'banana':
        return top_score
    else:
        return 0

def crop_image(img, quadrant):
    assert quadrant in ["TL", "TR", "BL", "BR"], "quadrant must be one of ['TL', 'TR', 'BL', 'BR']"
    crop_a = (img.shape[0] // 3) * 2
    crop_b = (img.shape[1] // 3) * 2

    if quadrant == "TL":
        img = img[:crop_a, :crop_b]
    elif quadrant == "TR":
        img = img[:crop_a, -crop_b:]
    elif quadrant == "BL":
        img = img[-crop_a:, :crop_b]
    else:
        img = img[-crop_a:, -crop_b:]

    return img

def find_banana(img):
    top_score = 0
    top_quadrant = "None"
    for quadrant in ['TL', 'TR', 'BL', 'BR']:
        cropped = crop_image(img, quadrant)
        pred = contains_banana(cropped)
        if pred > top_score:
            top_score = pred
            top_quadrant = quadrant
    
    # check the center
    pred = contains_banana(img)
    if pred > top_score:
        top_quadrant = "C"

    return top_quadrant