## **Kaggle dataset: Rice Image Dataset**
#### Five different Rice Image Dataset. Arborio, Basmati, Ipsala, Jasmine, Karacadag
https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset?datasetId=2049052&sortBy=voteCount

---

License: CC0: Public Domain

---

Using custom small Convolutional Neural Network and Transfer Learning MobileNetv2 by Keras to build classification models for rice image classification:
<br><br>
1. Load the data
-  Load the image data by using **keras.utils.image_dataset_from_directory** and setting the train/split ratio to 0.8/0.2.
2. Preprocess the data
-  Standardize values from RGB [0,255] range to [0,1] range by using **keras.layers.Rescaling**
3. Configue the data
-  Make sure to use buffered prefetching so we can yield data from disk without having I/O become blocking by using **Dataset.cache** and **Dataset.prefetch**
4. Create the model
-  Create custom CNN model and Transfer Learning MobileNetv2 model.
-  For both models, the optimizer is set to **keras.optimizers.Adam** and **keras.losses.SparseCategoricalCrossentropy** for loss function.
5. Result
-  The custom CNN model has achived validation accuracy of 99.2% and MobileNetv2 model with validation accuracy of 97.1%.
<br><br>
After thoughts: 
- The custom CNN may have overfitting problem, future task could include to have a dropout layer and data augmentation layer to solve overfitting.
- The MobileNetv2 model has achived 97.1% accuracy so no further fine tuning work has been carried out.


