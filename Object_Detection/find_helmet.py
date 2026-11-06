from ultralytics import YOLO
import glob, os, cv2

model_path = "/Users/junedshaikh/Downloads/SH17_Pretrained_Project_Starter/runs/detect/runs/sh17_pretrained_demo/weights/best.pt"
image_dir = "/Users/junedshaikh/Downloads/archive-3/images"
output = "/Users/junedshaikh/Downloads/SH17_Pretrained_Project_Starter/helmet_test_found.jpg"

model = YOLO(model_path)
images = sorted(glob.glob(image_dir + "/*"))

print("Checking images for helmets...")

results = model.predict(
    source=images[:100],
    imgsz=640,
    conf=0.05,
    classes=[10],
    device="mps",
    stream=True,
    verbose=False
)

for result in results:
    if result.boxes is not None and len(result.boxes) > 0:
        cv2.imwrite(output, result.plot())
        print("Helmet detected in:", os.path.basename(result.path))
        print("Saved result to:", output)
        break
else:
    print("No helmet detected in the first 100 images.")
