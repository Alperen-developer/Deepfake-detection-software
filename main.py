import subprocess
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Java betikleri çalıştıran fonksiyonlar
def run_face_segmenter(video_path):
    subprocess.run(["javac", "FaceSegmenter.java"])
    subprocess.run(["java", "FaceSegmenter", video_path])

def run_motion_analyzer(video_path):
    subprocess.run(["javac", "MotionAnalyzer.java"])
    subprocess.run(["java", "MotionAnalyzer", video_path])

# C++ betiği çalıştıran fonksiyon
def run_face_comparator(image1, image2):
    os.system(f"g++ FaceComparator.cpp -o FaceComparator")
    result = subprocess.run(["./FaceComparator", image1, image2], capture_output=True, text=True)
    return float(result.stdout.strip())

# Basit bir deepfake model yükleyelim (dummy bir model için placeholder)
def load_deepfake_model():
    # Buraya örnek bir model yükleyebilirsin
    # Şimdilik sahte bir model kullanıyoruz
    class DummyModel:
        def predict(self, x):
            return np.array([[0.7]])  # %70 deepfake gibi sabit dönüyor
        
    return DummyModel()

# Ana işlem
def detect_deepfake(video_path):
    print("[+] Java Face Segmenter çalışıyor...")
    run_face_segmenter(video_path)

    print("[+] Java Motion Analyzer çalışıyor...")
    run_motion_analyzer(video_path)

    print("[+] Deepfake Modeli yükleniyor...")
    model = load_deepfake_model()

    print("[+] Video işleniyor...")
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (128, 128))
        frames.append(frame)
    cap.release()
    
    frames = np.array(frames) / 255.0
    frames = frames.reshape((-1, 128, 128, 3))

    # Basit bir tahmin (gerçek modelde daha karmaşık olur)
    preds = model.predict(frames)
    avg_pred = np.mean(preds)

    print(f"[+] Ortalama tahmin: {avg_pred:.2f}")
    
    if avg_pred > 0.5:
        print(">>> Bu video DEEPFAKE olabilir!")
    else:
        print(">>> Bu video GERÇEK gibi görünüyor.")
    
    # Ekstra C++ yüz karşılaştırması (örnek)
    similarity = run_face_comparator("face1.jpg", "face2.jpg")
    print(f"[+] Yüz benzerliği (C++): {similarity:.2f}")

# Çalıştır
if __name__ == "__main__":
    video_path = input("Video dosya yolunu girin: ")
    detect_deepfake(video_path)
