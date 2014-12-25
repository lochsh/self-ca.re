#include <time.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>

int count_lines(FILE *file)
{
	int ch;
	int lines = 0;
	
	while ((ch = fgetc(file)) != EOF) 
	{
		if (ch == '\n')
		{
			lines++;
		}
	}
	rewind(file);
	
	return lines;
}

char** read_lines(FILE *file, int K)
{
	int k, l;
	char **lines;
	
	lines = (char**) malloc(K * sizeof(char*));
	
	for (k = 0; k<K; k++)
	{
		lines[k] = (char*) malloc(32);
		if (lines == NULL)
		{
			perror("Error allocating memory for names");
			for (l = 0; l<k-1; l++)
			{
				free(lines[l]);
			}
			free(lines);
			return NULL;
		}
		
		if (fgets(lines[k], 32, file) == NULL)
		{
			printf("Not enough lines in file\n");
			for (l = 0; l<k; l++)
			{
				free(lines[l]);
			}
			free(lines);
			return NULL;
		}
	}
	
	return lines;
}

int main()
{
	int A, N, a, n;
	FILE *adj_file, *noun_file;
	char **adj, **noun;
	
	adj_file = fopen("adjectives.txt", "r");
	
	if (adj_file == NULL)
	{
		perror("Error opening adjectives file");
		return errno;
	}
	
	noun_file = fopen("nouns.txt", "r");
	
	if (noun_file == NULL)
	{
		perror("Error opening nouns file");
		fclose(adj_file);
		return errno;
	}
	
	A = count_lines(adj_file);
	N = count_lines(noun_file);
	srand(time(NULL));
	a = rand();
	n = rand();
	a = a%A;
	n = n%N;
	adj = read_lines(adj_file, A);
	noun = read_lines(noun_file, N);
	fclose(adj_file);
	fclose(noun_file);
	
	//quick fix to remove \n
	adj[a][strlen(adj[a]) - 1] = '\0';
	noun[n][strlen(noun[n]) - 1] = '\0';
	
	// ;o
	printf("You are a%s %s.\n", adj[a], noun[n]);
	
	return 0;
}
