from math import floor
import sys


[N, M] = map(int, sys.stdin.readline().split(" "))

if (N == 1):
    print(1);
if (N == 2):
    move_count = M / 2;
    if (move_count > floor(move_count)):
        move_count = floor(move_count+1);
    if (move_count > 4):
        move_count = 4;
    print(floor(move_count));
if (N > 2):
    if (M > 6):
        move_count = M-2;
    elif (4 < M <= 6):
        move_count = 4;
    else:
        move_count = M;
    print(move_count);
