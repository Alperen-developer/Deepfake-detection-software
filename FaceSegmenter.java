import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.videoio.VideoCapture;
import org.opencv.objdetect.CascadeClassifier;
import org.opencv.imgproc.Imgproc;

public class FaceSegmenter {
    public static void main(String[] args) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);

        String videoPath = args[0];
        VideoCapture capture = new VideoCapture(videoPath);
        CascadeClassifier faceDetector = new CascadeClassifier("haarcascade_frontalface_default.xml");

        Mat frame = new Mat();
        int count = 0;

        while (capture.read(frame)) {
            MatOfRect faceDetections = new MatOfRect();
            faceDetector.detectMultiScale(frame, faceDetections);

            for (Rect rect : faceDetections.toArray()) {
                Mat face = new Mat(frame, rect);
                Imgcodecs.imwrite("face_" + (count++) + ".jpg", face);
            }
        }
        capture.release();
        System.out.println("Faces extracted: " + count);
    }
}

