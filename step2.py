#Input: Array of SIFT Descriptors from step
#Output: a dictionary of n words




#cluster the descriptors

def clusterDescriptors(descriptors[], k):

    # cluster feature descriptors into k groups
    #implement kmeans algorithm - kmeans is an algorithm used for usnupervised learning


    #Step1: Select the value of K  -> number of clusters
    #Step2: Select random K points which act as centroids - Centroids are data points representing the centrer of a cluster
    #Step3: Expectation step - Assign each data point to the closest centroid
    #Step4: Maximization step - compute the new centroid of each cluster
    #Step5: Repeat step 3 - it will reassign each datapoint to the new closest centroid of each cluster
    #Step6: If any reassignmnent occured   Do Step4
        #else Step7
    #Step7: FINISH

    # Each cluster represents a visual world
    # The whole set of clusters represents  a dictionary


    return kmeans



def generate_dictionary(descriptors[]):

# 500 means that we will have 500 clusters 
int dictionarySize = 500
# extract descriptors using sift function from step 1

descriptors []  = sift(img)

# build the dictionary
dictionary = clusterDescriptors(descritors, dictionarySize)


return dictionary
