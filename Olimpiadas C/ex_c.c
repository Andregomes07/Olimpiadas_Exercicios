#include <stdio.h>

int main(void) {
	int N;
	if (scanf("%d", &N) != 1) {
		return 0;
	}

	int count = 0;
	int max_altura = 0;
	for (int i = 0; i < N; ++i) {
		int h;
		if (scanf("%d", &h) != 1) {
			return 0;
		}
		if (h > max_altura) {
			++count;
			max_altura = h;
		}
	}

	printf("%d\n", count);
	return 0;
}

