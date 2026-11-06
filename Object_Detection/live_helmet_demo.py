from ultralytics import YOLO
import cv2

WEIGHTS = "/Users/junedshaikh/Downloads/SH17_Pretrained_Project_Starter/runs/detect/runs/sh17_pretrained_demo/weights/best.pt"

print("Loading helmet detection model...")
model = YOLO(WEIGHTS)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Camera open nahi hua.")
    print("Mac Settings > Privacy & Security > Camera mein Terminal permission check karo.")
    raise SystemExit(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Live helmet detection started. Press Q to quit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera se frame nahi mila.")
            break

        results = model.predict(
            source=frame,
            imgsz=640,
            conf=0.15,
            device="mps",
            classes=[10],
            verbose=False
        )

        display_frame = results[0].plot()
        cv2.imshow("Workplace Safety - Helmet Detection", display_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
