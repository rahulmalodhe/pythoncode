from collections import deque
N = int(input())
bride_initial , groom_initial = list(input().split())
bride = list(bride_initial)
groom = list(groom_initial)

for i in range(N+2):
    if bride[0] == groom[0]:
        del bride[0]
        del groom[0]

    else:
        groom = deque(groom)
        groom.rotate(-1)
        groom = list(groom)
a = len(groom)
print(a)