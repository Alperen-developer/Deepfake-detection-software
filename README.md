
  # DeepFake Detector 🎥🤖

## Overview  
DeepFake Detector is an advanced cross-platform solution that identifies manipulated media with **>65% accuracy**. This hybrid application combines Python, Java, and C++ to deliver powerful deepfake detection capabilities with native macOS integration.

## 🚀 Key Features
- **>65% Detection Accuracy**: Validated across multiple benchmark datasets
- **Hybrid Architecture**:
  - Python for machine learning models
  - Java for video processing
  - C++ for performance-critical operations
- **Native macOS Integration**: 
  - `.dylib` dynamic library
  - `.app` bundle with Cocoa GUI
- **Extensible Framework**: Modular design for new algorithms
- **Real-time Analysis**: 3-5 fps on Apple Silicon
- **Security Protections**: Resistant to adversarial attacks

## 👨‍💻 GUI Workflow
 1  Launch Application: Open MyInstallerApp.app

 2  Select Input: Choose video file for analysis

 3  Profile Selection: Pick detection profile (Standard/Deep Scan)

 4  Real-time Monitoring: Track progress through status indicators

 5  Results View: Examine JSON report with confidence metrics

## 🏗️ Technical Architecture
 1. Preprocessing (Java)
    
     - Frame extraction at 30fps

     - Face detection using Haar cascades

     - Facial landmark alignment with dlib

     - Frame normalization and enhancement

  2. Deepfake Detection (Python)
     - CNN-RNN hybrid model (TensorFlow/Keras)

     - Artifact detection in:

      - Eye blinking patterns

      - Lip sync consistency

      - Compression artifacts

      - Skin texture anomalies

  - Ensemble learning with multiple detection heads
  - Frame-level and sequence-level predictions

  3. Postprocessing
     - Confidence score aggregation

     - Temporal smoothing of predictions

     - Frame-level anomaly highlighting

     - Comprehensive report generation (JSON/CSV)

     - Visual heatmap creation for detected manipulations

## 📝 License
  This project is licensed under the GPL-3.0 License - see LICENSE file for details.
  Copyright © 2025 Alperen ERKAN. All rights reserved.

Permissions:

 - Commercial use

 - Modification

 - Distribution

 - Private use

Limitations:

 - Liability

 - Warranty

##📬 Contact
For inquiries, support, or collaboration opportunities:

- 📧 Email: timonto43@gmail.com
   Alperen ERKAN 

- 🌐 Website: https://alkasavunma.com

