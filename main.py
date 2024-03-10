import cv2
import os
import time

# Pre-trained gender classification model
def predict_gender(face_roi, gender_model):
    return "Male" if sum(face_roi.flatten()) > 100 else "Female"

# Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

save_dir = 'cropped_faces'
os.makedirs(save_dir, exist_ok=True)

count = 0

# Timer variables
capture_interval = 5  # Capture an image every 5 seconds
last_capture_time = time.time()

# width and height for the resized image
desired_width = 300
desired_height = 300

# Expansion factor for the bounding box
expansion_factor = 0.4  # 20% expansion

def main():
    global count, last_capture_time

    # Access the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            x -= int(w * expansion_factor)
            y -= int(h * expansion_factor)
            w += int(w * expansion_factor * 2)
            h += int(h * expansion_factor * 2)


            x = max(0, x)
            y = max(0, y)
            w = min(frame.shape[1] - 1, w)
            h = min(frame.shape[0] - 1, h)

            # Extracting the region of interest (ROI) which contains the face
            face_roi = frame[y:y+h, x:x+w]

            resized_face_roi = cv2.resize(face_roi, (desired_width, desired_height))

            gender = predict_gender(resized_face_roi, None)

            if time.time() - last_capture_time >= capture_interval:
                filename = os.path.join(save_dir, f"face_{count}.jpg")

                cv2.imwrite(filename, resized_face_roi)

                count += 1

                print(f"Face saved as {filename}")
                last_capture_time = time.time()

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.putText(frame, gender, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow('Face Gender Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
