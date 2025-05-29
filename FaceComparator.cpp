#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;

double computeSSIM(const Mat& i1, const Mat& i2) {
    Mat ssim_map;
    cv::Scalar mssim = quality::QualitySSIM::compute(i1, i2, noArray());
    return (mssim[0] + mssim[1] + mssim[2]) / 3;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cout << "Usage: ./FaceComparator <image1> <image2>" << std::endl;
        return -1;
    }
    Mat img1 = imread(argv[1]);
    Mat img2 = imread(argv[2]);

    if (img1.empty() || img2.empty()) {
        std::cerr << "Cannot load images!" << std::endl;
        return -1;
    }

    resize(img1, img1, Size(128, 128));
    resize(img2, img2, Size(128, 128));

    double ssim = computeSSIM(img1, img2);
    std::cout << ssim << std::endl;

    return 0;
}
