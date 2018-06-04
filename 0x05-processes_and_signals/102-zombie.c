#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - runs a infinite while loop
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: always 0
 */
int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);
		i++;
	}
	infinite_while();
	return (0);
}
