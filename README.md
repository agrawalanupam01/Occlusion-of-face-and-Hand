# Occlusion-of-face-and-Hand
This is a basic project using Xml files to detect the hands and face of a person and to check whether there is a occlusion or not.


-->INTRODUCTION

Segmentation is a computer vision technique that differ the two or
more classes of the objects we are working on. In this case we are doing
for “Hand and face occlusion detection”, presence of a face and hand in an
image and calibrates it. In a natural scene, it is difficult for a face to be
protected from occlusion. So a general face detection method is difficult to
find a face because of the lack of facial features. [1]This project have face
detection with large area occlusion or hand detection over the face and
their segmentation. The face and hand detection of the occlusion is
realized, according to the relationship between the human eye and the
human face and the relationship between the mouth and the face, which is
the physiological characteristics of the face and for hand the gaps between
the fingers and general length of the fingers are classified and seen and
thus we detect the hand and further segment it. Finally, the accuracy of
large-area occlusion of various occluders is compared, which proves that
the method is reasonable and robust.
We have built the project namely “Face and hand detection and
segmentation and occlusion. ” In this model we have segmented the image
of hand and face using the HSV values. The concept of hand and face
occlusion detection is helpful and needful in the cases of sign language and
can be proven great help for the people working in the fields of
improvement of it.

-->REQUIREMENTS

● Numpy
● Scipy
● Opencv-python
● Ipython
● Colab Environment
● Xml files of face and hand

-->METHODOLOGY

We import the packages that we’ll need. We’ll use NumPy for some
numerical processing and cv2 for our OpenCV bindings.we import the xml
files for face,hand and fist detection which uses viola john’s haar cascade
classifier. we define the lower and upper boundaries for pixel intensities to
be considered skin.
We grab reference to the webcam by passing a value of 0 to the
cv2.VideoCapture function. [2]We start looping over the frames in the
video. grab the next frame using the camera.read() method.
The camera.read() function returns a tuple, consisting of grabbed and
frame.
The grabbed variable is simply a boolean flag, indicating if the frame was
successfully read or not. The frame is the frame itself. In order to speed up
the skin detection process, we use our imutils.resize convenience function
to resize our frame to have a width of 400 pixels.
First, we convert the image from the RGB color space to the HSV color

space. Then, we apply the cv2.inRange function, supplying our HSV
frame, and our lower and upper boundaries as arguments, respectively.
The output of the cv2.inRange function is our mask This mask is a single
channel image, has the same width and height as the frame, and is of the
8-bit unsigned integer data type.
Pixels that are white (255) in the mask represent areas of the frame that
are skin. Pixels that are black (0) in the mask represent areas that are not
skin.
However, we may detect many small false-positive skin regions in the
image. To remove these small regions. [3] First, we create an elliptical
structuring kernel. Then, we use this kernel to perform two iterations of
erosions and dilations, respectively.
These erosions and dilations will help remove the small false-positive skin
regions in the image. From there, we smooth the mask slightly using a
Gaussian blur. This smoothing step, while not critical to the skin detection
process, produces a much cleaner mask.We then apply the skin mask to
our frame.

-->LIMITATIONS

There are some pretty obvious limitations and drawbacks to this approach.

1]The main drawback is that we are framing segmentation as a “color
detection” problem. This assumes that we can easily specify the HSV
values for ranges of pixel intensities that are considered skin.
2] However, under different lighting conditions, this approach might not
perform as well — and we would likely have to continue to tweak the HSV
value ranges.
3] The HSV value ranges we supplied worked fairly well for this example
post, but what about for other ethnicities?
For example, If a white male. And surely the same HSV values used to
detect skin could not be used to detect someone from Asia or Africa. This
implies that we have some a prior knowledge regarding the skin tone of
who we want to detect.
4] Of course, more robust approaches can be applied. A (highly simplified)
example would be to perform face detection to an image, determine the
color of the skin on their face, and then use that model to detect the rest of
the skin on their body.

-->REFERENCES

[1] Occlusion Aware Facial Expression Recognition Using CNN With
Attention Mechanism by Yong Li, Xliin Chen
[2] M. Pantic, M. Valstar, R. Rademaker, L. Maat, &quot;Web-based database for
facial expression analysis&quot;, Proc. ICME, pp. 5, Jul. 2005.
[3] S. Li, W. Deng, J. Du, &quot;Reliable crowdsourcing and deep locality-
preserving learning for expression recognition in the wild&quot;, Proc. CVPR
