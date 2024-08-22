from time import sleep

for c in range(10, -1, -1):
    print("\033[33m", c)
    sleep(.5)
print("\033[31mCatapababun! Bum! Pow!")
