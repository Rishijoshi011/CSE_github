#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

#define N 5  // Number of philosophers

sem_t forks[N];  // One semaphore per fork

void *philosopher(void *num) {
    int id = *(int *)num;
    while (1) {
        // Thinking
        printf("Philosopher %d is thinking.\n", id);

        // Hungry
        printf("Philosopher %d is hungry.\n", id);
        sem_wait(&forks[id]);  // Pick up left fork
        sem_wait(&forks[(id + 1) % N]);  // Pick up right fork

        // Eating
        printf("Philosopher %d is eating.\n", id);
        sleep(1);

        // Put down forks
        sem_post(&forks[id]);
        sem_post(&forks[(id + 1) % N]);

        // Thinking again
        printf("Philosopher %d is thinking again.\n", id);
    }
}

int main() {
    pthread_t thread_id[N];
    int philosophers[N];

    // Initialize the semaphores
    for (int i = 0; i < N; i++) {
        sem_init(&forks[i], 0, 1);
    }

    // Create philosopher threads
    for (int i = 0; i < N; i++) {
        philosophers[i] = i;
        pthread_create(&thread_id[i], NULL, philosopher, &philosophers[i]);
    }

    // Join philosopher threads
    for (int i = 0; i < N; i++) {
        pthread_join(thread_id[i], NULL);
    }

    return 0;
}
