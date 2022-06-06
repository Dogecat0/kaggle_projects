# **Kaggle dataset: Rice Image Dataset**

Five different Rice Image Dataset. Arborio, Basmati, Ipsala, Jasmine, Karacadag

License: CC0: Public Domain

[Kaggle Dataset](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset?datasetId=2049052&sortBy=voteCount)


---


## **Using custom small Convolutional Neural Network and Transfer Learning MobileNetv2 by Keras to build classification models for rice image classification**

<ol type="1">
    <li>Load the data with 80/10/10 train, test and validation split</li>
    <li>Preprocess the data</li>
    <ul>
        <li>Normalize values from RGB [0,255] range to [0,1] range.</li>
    </ul>
    <li>Configue the data</li>
    <ul>
        <li>Make sure to use buffered prefetching so we can yield data from disk without having I/O become blocking.</li>
    </ul>
    <li>Create the model</li>
    <ul>
        <li>Custom CNN model and compare accuracy to transfer learning MobileNetv2</li>
        <li>For both models, the optimizer is set to <strong>Adam</strong> and <strong>SparseCategoricalCrossentropy</strong> for loss function</li>
    </ul>
    <li>Results</li>
    <ul>
        <li>Both the custom CNN model and MobileNetv2 have achieved 99% test accuracy</li>
    </ul>
    <li>Prediction on test dataset and image downloaded from internet</li>
</ol>