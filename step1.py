from keypoints import Keypoint

#Extract the SIFT features from the training and the test images

#Implement the SIFT descriptor from scratch, we are not allowed to call inbuilt SIFT functions from other libraries such as OpenCV

#-------I/O--------

#Input -> directory path (where the images we want are)
#Output -> list/array of images
def load_images(path):
    return 0

#--------GAUSSIAN BLUR AND DIFFERENCE OF GAUSSIANS---------
def gaussian_function(x, mu, sd):
    #implement formula from lecture slides
    return 0

def convolution(img, kernel, avg=False):
    #implement code from lab
    return convoluted_img

def gaussian_kernel(size, sigma=1):
    #code from lab?
    return kernel

def gaussian_blur(img, kernel_size, sigma):
    #kernel = gaussian_kernel(kernel_size, sigma)
    #blurred_img = convolution(img, kernel, avg=True)
    return blurred_img

def diff_gaussians(gaussian1, gaussian2):
    #subtract both gaussians and return DoG matrix
    return diff_gaussians

#---------Keypoint Functions---------

# original img -> list of keypoint objects
def find_keypoints(img):

    keypoints = []

    #compute first gaussian blur with standard deviation s1
    #compute second gaussian blur with standard deviation s2
    #compute the DoG (Difference of Gaussians)

        #LOOP DESCRIPTION: Find the keypoints in DoG by iterating every pixel and comparing it to its neighbours (local maxima and minima method)
        #FOR EVERY PIXEL IN DoG MATRIX
            #find local minima and maxima in DoG
            #refer to "Local Maxima and Local Minima" chapter in https://www.analyticsvidhya.com/blog/2019/10/detailed-guide-powerful-sift-technique-image-matching-python/

            #create a Keypoint object and pass in the (x,y) coordinate of the keypoint 
            #append Keypoint object to keypoints list

        #END LOOP

    return keypoints

# list of keypoint objects -> list of refined keypoints
def refine_keypoints(keypoints):
    return refined_keypoints

#[Keypoint], img (DoG? Original?) -> [Keypoint] (now with updated orientation attributes)
def find_orientation(keypoints, img):
    #for each keypoint in keypoints:
        #find keypoint's gradient in x and y direction, by referring to its neighbours in img:
            #refer to chapter on "Calculate Magnitude and Orientation" 
            #on https://www.analyticsvidhya.com/blog/2019/10/detailed-guide-powerful-sift-technique-image-matching-python/
            
        #calculate Keypoint magnitude and orientation based on x and y gradients
        #update Keypoint magnitude and orientation attributes 
    return keypoints

def find_descriptors(keypoints):
    return descriptors

#image -> list of SIFT descriptors

def sift(img):

    #list of Keypoint objects
    keypoints = []

#Step 1) initial detection of keypoints
    keypoints = find_keypoints(img)

#Step 2) refine the keypoints
    keypoints = refine_keypoints(keypoints)

#Step 3) determine orientation of each keypoint
    keypoints = find_orientation(keypoints)

#Step 4) determine each keypoint's descriptor
    keypoints = find_descriptors(keypoints)

    #filter descriptors out of keypoints list
    descriptors = []

    return descriptors


def main():
    print("Hello from main function")

if __name__ == "__main__":
    main()
