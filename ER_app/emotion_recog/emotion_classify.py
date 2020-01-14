import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np
from os.path import join
from keras import backend as K

def recognition(input_path, output_path):
    
    K.clear_session()
    emotion_model_path = 'ER_app/emotion_recog/model/bkvgg12.059-0.663695.hdf5'
    detection_model_path = 'ER_app/emotion_recog/haarcascade_files/haarcascade_frontalface_default.xml'

    emotion_classifier = load_model(emotion_model_path, compile=False)
    face_detection = cv2.CascadeClassifier(detection_model_path)

    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised", "neutral"]

    
    img = cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

    
    for face in faces:
        (fX, fY, fW, fH) = face
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
            
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]

        cv2.putText(img, label, (fX, fY + fH + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        cv2.rectangle(img, (fX, fY), (fX + fW, fY + fH),
                                (0, 0, 255), 2)
    
    cv2.imwrite(output_path, img)
    return len(faces)
