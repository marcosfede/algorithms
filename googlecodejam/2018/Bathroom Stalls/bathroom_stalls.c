#include <stdio.h>
#include <stdlib.h>

typedef struct {
  unsigned long left;
  unsigned long right;
} stalls;

stalls place_one(unsigned long N);
stalls solve(unsigned long N, unsigned long K);

int main()
{
  stalls s;
  unsigned T, t;
  unsigned long N, K;

  scanf("%u", &T);
  for (t=1; t<=T; t++) {
    scanf("%lu %lu\n", &N, &K);
    s = solve(N, K);
    if (s.right < s.left) {
      printf("CASE #%u: %lu %lu\n", t, s.left, s.right);
    } else {
      printf("CASE #%u: %lu %lu\n", t, s.right, s.left);
    }
  }
  return 0;
}

stalls place_one(unsigned long N) {
  stalls ret;
  if (N%2 == 0) {
    ret.left = N/2 - 1;
    ret.right = N/2;
  } else {
    ret.left = ret.right = (N - 1)/2;
  }
  return ret;
}

stalls solve(unsigned long N, unsigned long K) {
  stalls ret = place_one(N);
  while (K > 1) {
    if (K%2 == 0) {
      ret = place_one(ret.right);
      K /= 2;
    } else {
      ret = place_one(ret.left);
      K = (K - 1)/2;
    }
  }
  return ret;
}
