#include <stdio.h>

int main(void) {
	int N, K;
	if (scanf("%d %d", &N, &K) != 2) {
		return 0;
	}

	int possible = 0;
	for (int i = 0; i < N; ++i) {
		char line[1005];
		if (scanf("%s", line) != 1) {
			return 0;
		}

		int run = 0;
		for (int j = 0; line[j] != '\0'; ++j) {
			if (line[j] == '.') {
				++run;
				if (run >= K) {
					possible = 1;
					break;
				}
			} else {
				run = 0;
			}
		}

		if (possible) {
			// Ainda precisamos consumir as linhas restantes, se houver
			for (int r = i + 1; r < N; ++r) {
				if (scanf("%s", line) != 1) {
					return 0;
				}
			}
			break;
		}
	}

	printf("%d\n", possible);
	return 0;
}

