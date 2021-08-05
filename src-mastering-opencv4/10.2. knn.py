import cv2
import numpy as np

SIZE_IMAGE = 20
NUMBER_CLASSES = 10

def load_digits_and_labels(big_image):
    """Returns all the digits from the 'big' image and creates the
    corresponding labels for each image"""
    # Load the 'big' image containing all the digits:
    digits_img = cv2.imread(big_image, 0)
    # Get all the digit images from the 'big' image:
    number_rows = digits_img.shape[1] / SIZE_IMAGE
    rows = np.vsplit(digits_img, digits_img.shape[0] / SIZE_IMAGE)
    digits = []
    for row in rows:
        row_cells = np.hsplit(row, number_rows)
        for digit in row_cells:
            digits.append(digit)
    digits = np.array(digits)
    # Create the labels for each image:
    labels = np.repeat(np.arange(NUMBER_CLASSES), len(digits) /
                       NUMBER_CLASSES)
    return digits, labels


# Load all the digits and the corresponding labels:
digits, labels = load_digits_and_labels('../resources/digits.png')
print(digits.shape)

# Shuffle data
# Constructs a random number generator:
rand = np.random.RandomState(1234)
# Randomly permute the sequence:
shuffle = rand.permutation(len(digits))
digits, labels = digits[shuffle], labels[shuffle]

# Compute the descriptors for all the images.
# In this case, the raw pixels are the feature descriptors
raw_descriptors = []
for img in digits:
    raw_descriptors.append(np.float32(img.flatten()))
raw_descriptors = np.squeeze(raw_descriptors)

# At this point we split the data into training and testing (50% for each one):
partition = int(0.5 * len(raw_descriptors))
raw_descriptors_train, raw_descriptors_test = np.split(raw_descriptors, [partition])
labels_train, labels_test = np.split(labels, [partition])

print(raw_descriptors_train.shape)
print(labels_train)

knn = cv2.ml.KNearest_create()
knn.train(raw_descriptors_train, cv2.ml.ROW_SAMPLE, labels_train)

# Test the created model:
k = 5
ret, result, neighbours, dist = knn.findNearest(raw_descriptors_test, k)

# Compute the accuracy:
print(result)
print(labels_test)
print((result.flatten() == labels_test).mean())
# (result == labels_test).mean()
# print("Accuracy: {}".format(acc))

