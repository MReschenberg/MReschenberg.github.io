#include <stdio.h>
int main() {
	int *p, x;
	int arr[5] = {1000, 2000, 3000, 4000, 5000};
	int *p2;
	p = NULL;
	x = 5000
	p = &x;
	printf("%d %d %u %u\n", x, *p, p, &x);
	p2 = arr;
	*(p2+1) = *p;
	*p = *p2 + *(p2 + 2);
	p2++;
	printf("%d %d %d %u\n", x, *p, *p2, p2);
	return 0;
}