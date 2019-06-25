#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - infinite loop
 * Return: 0
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
 *main - the zombie's factory
 *Return: 0 or 0 after all
 */
int main(void)
{
	pid_t pid;
	int a;

	for (a = 0; a < 5; a++)
	{
		pid = fork();
		if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);
	}
	return (infinite_while());
}
