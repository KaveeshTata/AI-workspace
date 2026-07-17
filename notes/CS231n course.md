
The basic thing we can do in computer vision. For eg when we process a cat picture and we want the algorithm to return cat as output. We can run a linear classifier where it says whether its a cat or dog. We just compare two things 

Next would be neural networks, which has non linearity that will help us predict many things in computer vision

Classification - No spatial awareness, semantic segmentation - No objects just pixels, object detection - Detect different objects along with pixels and spatial awareness, Instance segmentation - Combines detection and segmentation

Video classification, multimodal video understanding which requires vision and sound etc, Visualisation and understanding

Images are designed to be represented in terms of tensors of 256 units. [0, 255]

Data driven approach: Collect a dataset of the images and labels, Then we train a ML algorithms to return a classifier which we can use to classify, Then we evaluate the classifier on test data rather than trained images

Nearest neighbour classifier: The train function memorises all the images and labels. The predict function predicts the most similar images and outputs the labels. The images are calculated with some distances. Whichever image is the closest to the test image, the corresponding label is returned. Train: O(1) and predicting is O(N). This is why 1NN does not work. It takes more time to test than to train.

L1 distance: The sum of all the absolute values of each image pixels.
L2 distance: The sum of squares of the difference of the distances. Then we square root the entire sum.