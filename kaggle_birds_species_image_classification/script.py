# %%

# %%
import os
#os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow.keras.layers as tfl


# %% [markdown]
# ### Load image data

# %%
# Create directory variables for train and valid datasets
train_dir = 'train/'
valid_dir = 'valid/'

# %%
# define parameters for the loader
batch_size = 64
img_height = 224
img_width = 224

# %%
# Set up the train and valid datasets
train_ds = tf.keras.utils.image_dataset_from_directory(
  train_dir,
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# %%
valid_ds = tf.keras.utils.image_dataset_from_directory(
  valid_dir,
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# %%
class_names = train_ds.class_names
print(class_names)

# %%
# Check the training dataset by loading the first 9 images
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

# %% [markdown]
# ### Preprocess the data

# %%
preprocessed_layer = tf.keras.layers.Rescaling(1./255)

# %%
preprocessed_ds = train_ds.map(lambda x, y: (preprocessed_layer(x), y))
image_batch, labels_batch = next(iter(preprocessed_ds))
first_image = image_batch[0]

print(np.min(first_image), np.max(first_image))

# %% [markdown]
# ### Configure the dataset for performance

# %%
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = valid_ds.cache().prefetch(buffer_size=AUTOTUNE)

# %% [markdown]
# ### Train the model

# %%
# Create a model using function API
def convolutional_model(input_shape):

    img_input = tf.keras.Input(shape=(input_shape))

    Z1 = tfl.Conv2D(32,(4,4),strides=1,padding='same')(img_input)
    A1 = tfl.ReLU()(Z1)
    P1 = tfl.MaxPool2D(pool_size=(8,8),strides=8,padding='same')(A1)
    Z2 = tfl.Conv2D(16,(2,2),strides=1,padding='same')(P1)
    A2 = tfl.ReLU()(Z2)
    P2 = tfl.MaxPool2D(pool_size=(4,4),strides=4,padding='same')(A2)
    F = tfl.Flatten()(P2)
    outputs = tfl.Dense(400,activation='softmax')(F)

    model = tf.keras.Model(inputs=img_input, outputs=outputs)
    return model

# %%
conv_model = convolutional_model((224, 224, 3))
conv_model.compile(optimizer = 'adam',
                   loss = tf.losses.SparseCategoricalCrossentropy(),
                   metrics = ['accuracy'])
callback = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss',
                                            patience = 3,
                                            restore_best_weights = True )                  

conv_model.summary()


# %%
history = conv_model.fit(train_ds, epochs = 50, validation_data=valid_ds)


