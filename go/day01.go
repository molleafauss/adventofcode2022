package main

import (
	"fmt"
	"sort"
	"strconv"
)

type ElfFood struct {
	num      int
	calories int
}

type Day01 struct {
	elf         int
	elfCalories int
	elves       []ElfFood
}

func (self *Day01) Parse(line string) {
	if line == "" {
		fmt.Printf("Elf n. %d holding %d calories\n", self.elf, self.elfCalories)
		self.elves = append(self.elves, ElfFood{self.elf, self.elfCalories})
		self.elf++
		self.elfCalories = 0
	} else {
		cal, err := strconv.Atoi(line)
		if err != nil {
			fmt.Printf("Invalid line: %s - %v\n", line, err)
		}
		self.elfCalories += cal
	}
}

func (self *Day01) Solve() {
	sort.Slice(self.elves, func(i, j int) bool {
		return self.elves[i].calories > self.elves[j].calories
	})
	fmt.Printf("Highest calories: %d\n", self.elves[0].calories)
	var top3 = 0
	for i := 0; i < 3; i++ {
		top3 += self.elves[i].calories
	}
	fmt.Printf("Top 3 calories: %d\n", top3)
}
