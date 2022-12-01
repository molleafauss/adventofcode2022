"""
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""
if __name__ == '__main__':
    elf = 0
    elf_calories = 0
    max_calories = 0
    with open("01a-calories.txt") as f:
        for l in f:
            l = l.strip()
            if not l:
                print("Elf n. {} holding {} calories".format(elf, elf_calories))
                if elf_calories > max_calories:
                    max_calories = elf_calories
                elf_calories = 0
                elf += 1
                continue
            elf_calories += int(l)
    if elf_calories > max_calories:
        max_calories = elf_calories
    print("Saw {} elves: maximum: {}".format(elf, max_calories))