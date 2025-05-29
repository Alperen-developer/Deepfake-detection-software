import org.opencv.core.*;
import org.opencv.videoio.VideoCapture;
import org.opencv.imgproc.Imgproc;

public class MotionAnalyzer {
    public static void main(String[] args) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);

        String videoPath = args[0];
        VideoCapture capture = new VideoCapture(videoPath);

        Mat prev = new Mat();
        Mat current = new Mat();
        int motionCount = 0;

        if (capture.read(prev)) {
            Imgproc.cvtColor(prev, prev, Imgproc.COLOR_BGR2GRAY);
        }

        while (capture.read(current)) {
            Imgproc.cvtColor(current, current, Imgproc.COLOR_BGR2GRAY);
            Mat diff = new Mat();
            Core.absdiff(prev, current, diff);
            double motion = Core.sumElems(diff).val[0];
            if (motion > 1000000) {
                motionCount++;
            }
            prev = current.clone();
        }
        capture.release();
        System.out.println("Motion detected frames: " + motionCount);
    }
}
