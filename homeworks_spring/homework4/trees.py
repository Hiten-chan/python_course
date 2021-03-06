from scipy.ndimage import imread
import matplotlib.pyplot as plt
import numpy as np
import os

from sklearn.ensemble import RandomForestClassifier,\
    ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics.classification import accuracy_score


# function to get images from directory as matrix
# with shape of (n, 14400)
def get_images(dir_name):
    images = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (14400, )
        images.append(x)
    images = np.array(images)
    return images

# lets get images from lemons and strawberries directories
# and then shuffle them so our train/validation split is fair
lemons = get_images("lemons")
strawberries = get_images("strawberries")
np.random.shuffle(lemons)
np.random.shuffle(strawberries)

# lets get 400 (200 lemons and 200 strawberries) of images as training data
train_lemons = lemons[:200, ]
train_strawberries = strawberries[:200, ]

# other images are validation data
validate_lemons = lemons[200:, ]
validate_strawberries = strawberries[200:, ]

train = np.concatenate((train_lemons, train_strawberries))
validate = np.concatenate((validate_lemons, validate_strawberries))

# true classes 1 for face image and 0 for non-face image
train_y = np.concatenate((np.ones(200), np.zeros(200)))

# lets learn our Classifier
random_forest = RandomForestClassifier(n_estimators=10)
random_forest = random_forest.fit(train, train_y)
validate_y = np.concatenate((np.ones(50), np.zeros(50)))
predicted_y = random_forest.predict(validate)
# lets print accuracy_score of our prediction
print(accuracy_score(validate_y, predicted_y))


# lets learn our Classifier
x = ExtraTreesClassifier(n_estimators=10)
x = x.fit(train, train_y)
validate_y = np.concatenate((np.ones(50), np.zeros(50)))
predicted_x = x.predict(validate)
# lets print accuracy_score of our prediction
print(accuracy_score(validate_y, predicted_x))


# lets learn our Classifier
x = AdaBoostClassifier(n_estimators=10)
x = x.fit(train, train_y)
validate_y = np.concatenate((np.ones(50), np.zeros(50)))
predicted_x = x.predict(validate)
# lets print accuracy_score of our prediction
print(accuracy_score(validate_y, predicted_x))


# lets learn our Classifier
x = GradientBoostingClassifier(n_estimators=10)
x = x.fit(train, train_y)
validate_y = np.concatenate((np.ones(50), np.zeros(50)))
predicted_x = x.predict(validate)
# lets print accuracy_score of our prediction
print(accuracy_score(validate_y, predicted_x))
