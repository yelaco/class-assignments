package ReaderWriter;

import java.util.Random;
import java.util.logging.Logger;

public class Writer implements Runnable {
    private static final Logger log = Logger.getLogger(Writer.class.getCanonicalName());
    private boolean running = false;
    private final DataFile dataFile;

    public Writer(DataFile dataFile) {
        this.dataFile = dataFile;
    }

    @Override
    public void run() {
        running = true;
        write();
    }

    public void stop() {
        running = false;
    }

    public void write() {
       while (running) {
           try {
                dataFile.waitWrt();
           } catch (InterruptedException e) {
              break;
           }

           if (!running) {
               break;
           }

           dataFile.writeData(generateString());
           log.info("Size of the file is: " + dataFile.getSize());
           dataFile.signalWrt();

           ThreadUtil.sleep((long) (Math.random() * 100));
       }
       log.info("Writer Stopped");
    }

    private String generateString() {
        int leftLimit = 97; // letter 'a'
        int rightLimit = 122; // letter 'z'
        int targetStringLength = 10;
        Random random = new Random();
        StringBuilder buffer = new StringBuilder(targetStringLength);
        for (int i = 0; i < targetStringLength; i++) {
            int randomLimitedInt = leftLimit + (int)
                    (random.nextFloat() * (rightLimit - leftLimit + 1));
            buffer.append((char) randomLimitedInt);
        }
        String generatedString = buffer.toString();
        log.info(String.format("[%s] Generated String: %s",
                Thread.currentThread().getName(), generatedString));

        return generatedString;
    }
}
