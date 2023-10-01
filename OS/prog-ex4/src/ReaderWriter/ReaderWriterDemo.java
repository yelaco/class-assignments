package ReaderWriter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ReaderWriterDemo {
    public static void demoSingleWriterAndSingleReader() throws IOException {
        DataFile dataFile = new DataFile();

        Reader reader = new Reader(dataFile);
        Thread readerThread = new Thread(reader);

        Writer writer = new Writer(dataFile);
        Thread writerThread = new Thread(writer);

        writerThread.start();
        readerThread.start();

        List<Thread> threads = new ArrayList<>();
        threads.add(writerThread);
        threads.add(readerThread);

        ThreadUtil.sleep(2000);

        writer.stop();
        reader.stop();

        ThreadUtil.waitForAllThreadsToComplete(threads);
    }

    public static void demoMultipleWritersAndMultipleReaders() throws IOException {
        DataFile dataFile = new DataFile();
        int writerCount = 5;
        int readerCount = 5;
        List<Thread> threads = new ArrayList<>();
        List<Writer> writers = new ArrayList<>();
        List<Reader> readers = new ArrayList<>();

        for (int i = 0; i < writerCount; i++) {
            Writer writer = new Writer(dataFile);
            Thread writerThread = new Thread(writer);
            writerThread.start();
            threads.add(writerThread);
            writers.add(writer);
        }

        for (int i = 0; i < readerCount; i++) {
            Reader reader = new Reader(dataFile);
            Thread readerThread = new Thread(reader);
            readerThread.start();
            threads.add(readerThread);
            readers.add(reader);
        }

        ThreadUtil.sleep(10000);

        readers.forEach(Reader::stop);
        writers.forEach(Writer::stop);

        ThreadUtil.waitForAllThreadsToComplete(threads);
    }

    public static void main(String[] args) throws IOException {
//        demoSingleWriterAndSingleReader();
        demoMultipleWritersAndMultipleReaders();
    }
}