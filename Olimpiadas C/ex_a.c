#include <stdio.h>

int main(void) {
	long long N, M;
	if (scanf("%lld %lld", &N, &M) != 2) {
		return 0;
	}

	long long res = N / M;
	printf("%lld\n", res);

	return 0;
}

