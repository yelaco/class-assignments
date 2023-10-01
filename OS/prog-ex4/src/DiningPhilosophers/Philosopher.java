package DiningPhilosophers;

import java.util.logging.Logger;

public class Philosopher implements Runnable {
    private static final Logger log = Logger.getLogger(Philosopher.class.getCanonicalName());
    private final int ith;
    private boolean running = false;
    private final RiceBowl rb;

    public Philosopher(int ith, RiceBowl rb) {
        this.ith = ith;
        this.rb = rb;
    }

    @Override
    public void run() {
        running = true;
        eat();
    }

    public void stop() {
        running = false;
    }

    public void eat() {
        while (running) {
            try {
//                if (ith % 2 == 0) {
//                    rb.waitChopstick(ith);
//                    rb.waitChopstick((ith + 1) % 5);
//                } else {
//                    rb.waitChopstick((ith + 1) % 5);
//                    rb.waitChopstick(ith);
//                }
                rb.waitChopstick(ith);
                rb.waitChopstick((ith+1) % 5);
            } catch (InterruptedException e) {
                log.severe("Error while waiting to eat");
                break;
            }

            if (!running) {
                break;
            }

            log.info(String.format("%d-th philosopher is eating", ith));

//            if (ith % 2 == 0) {
//                rb.signalChopstick(ith);
//                rb.signalChopstick((ith + 1) % 5);
//            } else {
//                rb.signalChopstick((ith + 1) % 5);
//                rb.signalChopstick(ith);
//            }
            rb.signalChopstick((ith + 1) % 5);
            rb.signalChopstick(ith);


//            ThreadUtil.sleep((long) (100));
        }
        log.info("Philosopher Stopped");
    }
}
