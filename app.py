import cv2
import numpy as np
from tensorflow.keras.models import load_model

try:
    model = load_model("D:\sign_gesture_language\model\sign_language_classifier.h5")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

mapping = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
    8: 'I', 9: 'J (Tidak Ada)', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
    14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
    21: 'V', 22: 'W', 23: 'X', 24: 'Y'
}

BOX_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 0, 0)
BOX_THICKNESS = 3
TEXT_THICKNESS = 2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Gagal mengakses kamera")
        break

    frame = cv2.flip(frame, 1)
    img_proc = frame.copy()
    
    h, w, c = frame.shape

    box_size = 200   

    x_center = w // 2
    y_center = h // 2

    x1 = x_center - box_size // 2
    y1 = y_center - box_size // 2
    x2 = x_center + box_size // 2
    y2 = y_center + box_size // 2

    try:
        roi = img_proc[y1:y2, x1:x2]

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        img_model = cv2.resize(thresh, (28, 28))

        img_input = img_model.reshape(1, 28, 28, 1) / 255.0

        prediction = model.predict(img_input, verbose=0)
        class_id = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        letter = mapping.get(class_id, "???")

        text = f"{letter} ({confidence:.1f}%)"

        cv2.putText(frame, text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, TEXT_COLOR, TEXT_THICKNESS)

        cv2.imshow("Model Input (Debug)", img_model)

    except Exception:
        pass

    cv2.rectangle(frame, (x1, y1), (x2, y2), BOX_COLOR, BOX_THICKNESS)
    cv2.imshow("Deteksi Bahasa Isyarat (Tekan 'q' untuk keluar)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
