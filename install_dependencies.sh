#!/bin/bash

echo "[+] Kütüphaneler kuruluyor..."

# Python kütüphaneleri
echo "[+] Python kütüphaneleri yükleniyor..."
pip3 install numpy opencv-python tensorflow

# Java için OpenCV kurulumu
echo "[+] Java OpenCV kurulumu..."
if ! [ -d "opencv-java" ]; then
    mkdir opencv-java
    cd opencv-java
    wget -O opencv.zip https://github.com/opencv/opencv/releases/download/4.5.5/opencv-4.5.5.zip
    unzip opencv.zip
    echo "[!] Java için OpenCV manuel bağlama gerekebilir."
    cd ..
fi

# C++ için OpenCV kurulumu (brew üzerinden)
echo "[+] C++ OpenCV kurulumu..."
brew install opencv

echo "[+] Tüm kütüphaneler başarıyla kuruldu!"
