import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import shutil
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.utils import np_utils

print()

temp_dir = "../temp/"

def init_dir(dir):
    try:
        if os.path.exists(dir):
            shutil.rmtree(dir)
            os.makedirs(dir)
            print("Clear the directory: {}".format(dir))
        else:
            os.makedirs(dir)
            print("Create the directory: {}".format(dir))
    except OSError:
        init_dir(dir)
init_dir(temp_dir)

def savefig(fig, file_name):
    fig.savefig(temp_dir + file_name + ".png")
    print("Image file saved:", temp_dir + file_name + ".png")

print("Loading data...")
from keras.datasets import mnist
(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()
print("Done")
print("x_train_image.shape = {}".format(x_train_image.shape))
print("y_train_label.shape = {}".format(y_train_label.shape))
print(" x_test_image.shape = {}".format(x_test_image.shape))
print(" y_test_label.shape = {}\n".format(y_test_label.shape))

images_per_row = 8
defualt_row_number = 1
max_row_number = 3

def plot_images_labels_prediction(images, labels,
                                  prediction = [],
                                  start_index = 0,
                                  num = images_per_row * defualt_row_number):
    plt.clf()
    fig = plt.gcf()
    fig.set_size_inches(images_per_row * 2, images_per_row * 1.5)
    if num > images_per_row * max_row_number:
        raise ValueError("The maximum data number to print is " + str(images_per_row * max_row_number) + ".")
    for i in range(0, num):
        ax = plt.subplot(max_row_number, images_per_row, 1 + i)
        ax.imshow(images[start_index], cmap="binary")
        title = "i = " + str(start_index) + ", y = " + str(labels[start_index])
        if len(prediction) > 0:
            title += ", predict = " + str(prediction[start_index])
        ax.set_title(title, fontsize = 8)
        ax.set_xticks([])
        ax.set_yticks([])
        start_index += 1
#   plt.show()
    if len(prediction) <= 0:
        savefig(fig, "mlp_images_train_" + str(start_index - num) + "_" + str(start_index - 1))
    else:
        savefig(fig, "mlp_images_test_" + str(start_index - num) + "_" + str(start_index - 1))

plot_images_labels_prediction(x_train_image, y_train_label)
print()

# normalize input image, 0 < input < 1
def normalize_input(input_image):
    return input_image.reshape(input_image.shape[0], 28 * 28).astype("float64") / 255

# normalize output label as one-hot encoding, for example, 4 will normalize as [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
def normalize_output(output_label):
    return np_utils.to_categorical(output_label)

# data preprocessing
x_train = normalize_input(x_train_image)
x_test  = normalize_input(x_test_image)
y_train = normalize_output(y_train_label)
y_test  = normalize_output(y_test_label)

# create multi-layer preceptron neural network
model = Sequential()
# hidden layer 1
model.add(
    Dense(
        units = 100,
        input_dim = 784,
        activation = "relu",
        kernel_initializer = "normal",
        bias_initializer = "normal"
    )
)
# dropout layer
model.add(
    Dropout(
        rate = 0.5
    )
)
# hidden layer 2
model.add(
    Dense(
        units = 10,
        activation = "softmax",
        kernel_initializer = "normal",
        bias_initializer = "normal"
    )
)
print(model.summary(), "\n")

# definite training method
model.compile(
    optimizer = "adam",
    loss = "categorical_crossentropy",
    metrics = ["accuracy"]
)

# start training
train_history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 200,
    epochs = 20,
    validation_split = 0.2
)

def show_train_history(train_history, train, validation):
    plt.clf()
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc = "upper left")
#   plt.show()
    savefig(plt, "mlp_training_history_" + train)

show_train_history(train_history, "acc", "val_acc")
show_train_history(train_history, "loss", "val_loss")
print()

print("Evaluating: ")
scores = model.evaluate(x_test, y_test)
print("The loss of testing data:", scores[0])
print("The accuracy of testing data = {}%".format(scores[1] * 100.0))

print("Predicting: ")
prediction = model.predict_classes(x_test, verbose = 1)
print(pd.crosstab(y_test_label, prediction, colnames=["predict"], rownames=["y"]), "\n")

print("Data frame for error cases:")
df = pd.DataFrame({"label": y_test_label, "predict": prediction})
error_list = df.loc[df.label != df.predict]
print(error_list, "\n")

print("The error case is at i = {}".format(error_list.index[0] - 3))
plot_images_labels_prediction(x_test_image, y_test_label, prediction, start_index = max(0, error_list.index[0] - 3))
print()

print("Process ended.", "\n")
