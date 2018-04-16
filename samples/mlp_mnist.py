
# coding: utf-8

# In[58]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense

print()


# In[59]:


temp_dir = './temp/'
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
    print('Create directory:', temp_dir, '\n')

def savefig(fig, file_name):
    fig.savefig(temp_dir + file_name + '.png')
    print('Image file saved:', temp_dir + file_name + '.png')


# In[60]:


print('Loading data...')
from keras.datasets import mnist
(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()
print('Done')
print('Inputs:', str(x_train_image[0].shape), 'images.')
print('    x_train_image:', len(x_train_image))
print('    x_test_image :', len(x_test_image))
print('Outputs: labels.')
print('    y_train_label:', len(y_train_label))
print('    y_test_label :', len(y_test_label), '\n')


# In[61]:


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
        ax.imshow(images[start_index], cmap='binary')
        title = "i = " + str(start_index) + ", y = " + str(labels[start_index])
        if len(prediction) > 0:
            title += ", predict = " + str(prediction[start_index])
        ax.set_title(title, fontsize = 8)
        ax.set_xticks([])
        ax.set_yticks([])
        start_index += 1
#   plt.show()
    if len(prediction) <= 0:
        savefig(fig, 'images_train_' + str(start_index - num) + '_' + str(start_index - 1))
    else:
        savefig(fig, 'images_test_' + str(start_index - num) + '_' + str(start_index - 1))


# In[62]:


plot_images_labels_prediction(x_train_image, y_train_label)
print()


# In[63]:


def to_normalize_input(input_image):
    input_shape = input_image.shape
    if len(input_shape) != 3:
        raise ValueError("The length of the shape should be 3.")
    return input_image.reshape(input_shape[0], input_shape[1] * input_shape[2]).astype('float64') / 255

def to_normalize_output(output_label):
    return np_utils.to_categorical(output_label)


# In[64]:


x_train = to_normalize_input(x_train_image)
x_test  = to_normalize_input(x_test_image)

y_train = to_normalize_output(y_train_label)
y_test  = to_normalize_output(y_test_label)


# In[65]:


model = Sequential()
model.add(
    Dense(
        units = 200,
        input_dim = 784,
        activation = 'relu',
        kernel_initializer = 'normal',
        bias_initializer = 'normal'
    )
)
model.add(
    Dense(
        units = 10,
        activation = 'softmax',
        kernel_initializer = 'normal',
        bias_initializer = 'normal'
    )
)


# In[66]:


print(model.summary(), '\n')


# In[67]:


model.compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)


# In[68]:


train_history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 200,
    epochs = 20,
    validation_split = 0.2
)


# In[17]:


def show_train_history(train_history, train, validation, title = None):
    plt.clf()
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc = 'upper left')
#   plt.show()
    savefig(plt, 'training_history_' + train)


# In[29]:


show_train_history(train_history, 'acc', 'val_acc')


# In[44]:


show_train_history(train_history, 'loss', 'val_loss')
print()


# In[36]:


print('Evaluating: ')
scores = model.evaluate(x_test, y_test)
print("The loss for test data:", scores[0])
print("The accuracy for test data:", scores[1] * 100, '%\n')


# In[52]:


print('Predicting: ')
prediction = model.predict_classes(x_test, verbose = 1)
print(pd.crosstab(y_test_label, prediction, colnames=['predict'], rownames=['y']), '\n')


# In[55]:


print('Data frame for error cases:')
df = pd.DataFrame({'label': y_test_label, 'predict': prediction})
print(df[df.label != df.predict], '\n')


# In[54]:


plot_images_labels_prediction(x_test_image, y_test_label, prediction, start_index = 110)
print()


# In[57]:


print('Process ended.', '\n')

