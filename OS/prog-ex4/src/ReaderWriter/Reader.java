package ReaderWriter;

import java.util.logging.Logger;

public class Reader implements Runnable {
    private static final Logger log = Logger.getLogger(Reader.class.getCanonicalName());
    private boolean running = false;
    private final DataFile dataFile;

    public Reader(DataFile dataFile) {
        this.dataFile = dataFile;
    }

    @Override
    public void run() {
        running = true;
        read();
    }

    public void stop() {
        running = false;
    }

    public void read() {
        while (running) {
            try {
                dataFile.waitMutex();
                dataFile.readCount++;
                if (dataFile.readCount == 1)
                    dataFile.waitWrt();
                dataFile.signalMutex();
            } catch (InterruptedException e) {
                break;
            }
            if (!running) {
                break;
            }
            String content = dataFile.readData();
            showContent(content);

            try {
                dataFile.waitMutex();
                dataFile.readCount--;
                if (dataFile.readCount == 0)
                    dataFile.signalWrt();
                dataFile.signalMutex();
            } catch (InterruptedException e) {
                break;
            }
            ThreadUtil.sleep((long) (Math.random() *100));
        }
        log.info("Reader Stopped");
    }

    private void showContent(String content) {
        if (content != null) {
            log.info(String.format("[%s] reading file content: %s",
                    Thread.currentThread().getName(), content));
        }
    }
}
