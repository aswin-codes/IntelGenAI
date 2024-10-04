import cvzone
import cv2
from cvzone.ClassificationModule import Classifier
img = cv2.imread("Resources/LateBlight.png")
#Resources/RiceBlast.png
#Resources/WheatRusts.png
#cap = cv2.VideoCapture(0)
myClassifier = Classifier('MyModel/keras_model.h5','MyModel/labels.txt')
while True:
    #_,img = cap.read()
    predictions = myClassifier.getPrediction(img)

    cv2.imshow("Image",img)
    cv2.waitKey(1)

