package DiningPhilosophers;

import java.util.concurrent.Semaphore;

public class RiceBowl {
    private final Semaphore[] chopsticks = new Semaphore[5];

    public RiceBowl() {
        for (int i = 0; i < 5; i++) {
            chopsticks[i] = new Semaphore(1);
        }
    }

    public void waitChopstick(int idx) throws InterruptedException {
        chopsticks[idx].acquire();
    }

    public void signalChopstick(int idx) {
        chopsticks[idx].release();
    }
}
