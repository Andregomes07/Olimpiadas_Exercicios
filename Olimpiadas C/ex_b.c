#include <stdio.h>

int main(void) {
	long long A, L, C;
	if (scanf("%lld %lld %lld", &A, &L, &C) != 3) {
		return 0;
	}

	long long volume = A * L * C;
	int ok = (volume >= 50 && A >= 3) ? 1 : 0;

	printf("%d\n", ok);
	return 0;
}

