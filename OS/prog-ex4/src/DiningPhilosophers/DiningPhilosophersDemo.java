package DiningPhilosophers;

import java.util.ArrayList;
import java.util.List;

public class DiningPhilosophersDemo {
    public static void main(String[] args) {
        RiceBowl rb = new RiceBowl();
        List<Philosopher> philosophers = new ArrayList<>();
        List<Thread> threads = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            Philosopher philosopher = new Philosopher(i, rb);
            Thread threadPhilosopher = new Thread(philosopher);
            threadPhilosopher.start();
            threads.add(threadPhilosopher);
            philosophers.add(philosopher);
        }

        ThreadUtil.sleep(5000);

        philosophers.forEach(Philosopher::stop);

        ThreadUtil.waitForAllThreadsToComplete(threads);
    }
}