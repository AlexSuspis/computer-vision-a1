# not sure about the per class thing and what are the actual and predicted classes

#classification accuracy is a metric to evaluate the performance of classification predictive model

#First we need to use a classification model to make prediction for each example in a test data

# Accuracy = Correct Predictions /  Total Predictions
# Error = 1 - Accuracy
def error_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	accuracy =  correct / float(len(actual)) * 100
    error = 100 - accuracy
    return error




# A confusion matrix is a summary of the predictions made by a classification model organized into a table by class
#Each row indicates the actual class
#Each column represents the predicted class
# The cells on the diagonal represent correct Predictions
#from the confusion matrix we can find accuracy

def confusion_matrix(actual,predicted):

    # extract the different classes
    classes = np.unique(actual)

    # initialize the confusion matrix
    confusionMatrix = np.zeros((len(classes), len(classes)))

    # loop across the different combinations of actual / predicted classes
    for i in range(len(classes)):
        for j in range(len(classes)):

           # count the number of instances in each combination of actual / predicted classes
           confusionMatrix[i, j] = np.sum((actual == classes[i]) & (predicted == classes[j]))

    return confusionMatrix
