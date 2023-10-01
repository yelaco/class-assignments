package BoundedBuffer;

import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.Semaphore;

public class DataQueue {
    Queue<Message> queue = new LinkedList<Message>();
    private final int maxSize;
    Semaphore full, empty, mutex;

    public DataQueue(int maxSize) {
        this.maxSize = maxSize;
        full = new Semaphore(0);
        empty = new Semaphore(maxSize);
        mutex = new Semaphore(1);
    }

    public boolean isFull() {
        return this.queue.size() == maxSize;
    }

    public void waitEmpty() throws InterruptedException {
        empty.acquire();
    }

    public void signalEmpty() {
        empty.release();
    }

    public void waitFull() throws InterruptedException {
        full.acquire();
    }

    public void signalFull() {
        full.release();
    }

    // mutex is always acquired and released in the same thread -
    // -> never getting more than 1 available permits
    public void waitMutex() throws InterruptedException {
        if (mutex.availablePermits() == 1) {
            mutex.acquire();
        }
    }

    public void signalMutex() {
        mutex.release();
    }

    public void add(Message msg) {
        queue.add(msg);
    }

    public Message poll() {
        return queue.poll();
    }

    public int getSize() {
        return queue.size();
    }
}
