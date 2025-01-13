import random
import time
import shutil
import sys

FRAME_DELAY = 0.05
DURATION = 5
CHARS = ['1', '0', ' ']  
CSI = "\x1b["  

def matrix_effect(duration=DURATION):
    """Affiche un effet Matrix dans le terminal."""
    cols, lines = shutil.get_terminal_size()
    end_time = time.time() + duration

    sys.stdout.write(f"{CSI}?25l")
    sys.stdout.flush()

    matrix = [" " for _ in range(cols)]
    speed = [random.randint(1, 5) for _ in range(cols)]

    try:
        while time.time() < end_time:
            for i in range(cols):
                if random.random() > 0.5:
                    char = random.choice(CHARS)
                    matrix[i] = char
                    sys.stdout.write(f"{CSI}{random.randint(1, lines)};{i}f")
                    sys.stdout.write(f"{CSI}32m{char}\033[0m")  
                    sys.stdout.flush()

                if speed[i] > 0:
                    speed[i] -= 1
                else:
                    speed[i] = random.randint(1, 5)
                    sys.stdout.write(f"{CSI}{lines};{i}f")
                    sys.stdout.write(" ")  
                    sys.stdout.flush()

            time.sleep(FRAME_DELAY)

    finally:
        sys.stdout.write(f"{CSI}2J")  
        sys.stdout.write(f"{CSI}0m")
        sys.stdout.write(f"{CSI}?25h")
        sys.stdout.flush()
        print("\033[92m✅ Le système est stabilisé.\033[0m\n")
