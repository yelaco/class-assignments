package ReaderWriter;

import java.io.*;
import java.util.concurrent.Semaphore;

public class DataFile {
    private int size = 0;
    private Semaphore mutex, wrt;
    public int readCount = 0;

    public DataFile() throws IOException {
        mutex = new Semaphore(1);
        wrt = new Semaphore(1);
        resetSampleFile();
    }

    private void resetSampleFile() {
        try {
            new PrintWriter("sample.txt").close();
        } catch (FileNotFoundException ignored) {}
    }

    public void waitWrt() throws InterruptedException {
        wrt.acquire();
    }

    public void signalWrt() {
        wrt.release();
    }

    public void waitMutex() throws InterruptedException {
        mutex.acquire();
    }

    public void signalMutex() {
        mutex.release();
    }

    public void writeData(String message) {
        try (FileWriter writer = new FileWriter("sample.txt", true)){
            BufferedWriter bufferedWriter = new BufferedWriter(writer);
            bufferedWriter.write(message);
            bufferedWriter.newLine();
            bufferedWriter.close();
            size += message.length();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String readData() {
        StringBuilder content = new StringBuilder("");
        try (FileReader reader = new FileReader("sample.txt")){
            BufferedReader bufferedReader = new BufferedReader(reader);
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                content.append(line);
            }
            bufferedReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return content.toString();
    }

    public int getSize() {
        return this.size;
    }
}
