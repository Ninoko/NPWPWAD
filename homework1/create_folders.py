import os
import random
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
TIMES = ['morning', 'evening']

if __name__ == "__main__":
    for day in DAYS:
        for time in TIMES:
            path: str = os.path.join(day, time)
            os.makedirs(path, exist_ok=True)
            model: str = random.choice(list('ABC'))
            output: int = random.randint(0, 1000)
            computation_time: int = random.randint(0, 1000)
            with open(os.path.join(path, "Solutions.csv"), "w") as f:
                f.write("Model; Output value; Time of computation;\n")
                f.write(f"{model} ; {output} ; {computation_time}s;")
