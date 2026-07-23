
The basic thing we can do in computer vision. For eg when we process a cat picture and we want the algorithm to return cat as output. We can run a linear classifier where it says whether its a cat or dog. We just compare two things 

Next would be neural networks, which has non linearity that will help us predict many things in computer vision

Classification - No spatial awareness, semantic segmentation - No objects just pixels, object detection - Detect different objects along with pixels and spatial awareness, Instance segmentation - Combines detection and segmentation

Video classification, multimodal video understanding which requires vision and sound etc, Visualisation and understanding

Images are designed to be represented in terms of tensors of 256 units. [0, 255]

Data driven approach: Collect a dataset of the images and labels, Then we train a ML algorithms to return a classifier which we can use to classify, Then we evaluate the classifier on test data rather than trained images

Nearest neighbour classifier: The train function memorises all the images and labels. The predict function predicts the most similar images and outputs the labels. The images are calculated with some distances. Whichever image is the closest to the test image, the corresponding label is returned. Train: O(1) and predicting is O(N). This is why 1NN does not work. It takes more time to test than to train.

L1 distance: The sum of all the absolute values of each image pixels.
L2 distance: The sum of squares of the difference of the distances. Then we square root the entire sum.

Linear classifier = xW. They only get the colors but not the textures, or features or something that makes an image different color than it is trained on. 

Regularalisation: Prevent the model from doing too well on train dataset which makes it less accurate on test dataset
L2 regularisation: Square the weight matrix and sum them all. Likes to spread out the weights.
L1 regularisation: Sum of all the absolute weight values

Stochastic gradient descent: Subset or minibatch of data. Calculating the gradients of the minibatch and then do step descent. It is faster and better.

Saddle point: Where in high dimension vectors, we get a point where the gradient is 0 on all sides for that particular point. The descent stops where its not a true minimum. This is very common and the biggest problem in SGD

SGD with momentum: We update by velocity which is determined with previous velocity and the current gradient. So this gives a push required to get out of the saddle point

RMSProp: Its normally the better approach than SGD because it changes the learning rate based on the parameters getting the gradients which are large and small. So if a parameter are getting larger gradients it reduces the learning rate, otherwise it increases. It has a moving gradient squared variable which is dependent on decay rate and previous gradients and present gradients.

Adam Optimizer: Combination of momentum and RMSprop. Very famous in modern day deep learning. It has two moments, The first moment is the average gradient which says which direction the previous gradient are pointed to. Next is the average squared gradient, which says how large the gradients have been recently. But at the start, there is an initialisation bias where the gradient is small but the change will be very big. To account to this, we have biases for the moments.![[Screenshot 2026-07-22 at 7.39.17 PM.png]]

ResNets: Step learning rate decay

Second order optimizations are bad for deep learning because it is expensive and slow because of the inverse which we need to calculate while backtracking through second order derivatives. Also computing the hessian is somewhat a time taking process 

