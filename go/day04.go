package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Day04 struct {
	fullOverlaps    int
	partialOverlaps int
}

func (self *Day04) Parse(line string) {
	pairs := strings.Split(line, ",")
	// assert len(pairs) == 2
	one := strings.Split(pairs[0], "-")
	var elf1 [2]int
	elf1[0], _ = strconv.Atoi(one[0])
	elf1[1], _ = strconv.Atoi(one[1])
	// assert len(elf1) == 2
	two := strings.Split(pairs[1], "-")
	var elf2 [2]int
	elf2[0], _ = strconv.Atoi(two[0])
	elf2[1], _ = strconv.Atoi(two[1])
	// assert len(elf2) == 2
	// full overlap when both ends of one of the ranges are fully inside the other
	if (elf1[0] <= elf2[0] && elf1[1] >= elf2[1]) || (elf1[0] >= elf2[0] && elf1[1] <= elf2[1]) {
		self.fullOverlaps += 1
	}
	// partial overlap if either end of each range is inside the other (one check is enough?)
	// or - alternative - if one end is before the other and vice versa
	if !(elf2[0] > elf1[1] || elf2[1] < elf1[0]) {
		self.partialOverlaps += 1
	}
}

func (self *Day04) Solve() {
	fmt.Printf("Fully overlapping sections: %d\n", self.fullOverlaps)
	fmt.Printf("Partially overlapping sections: %d\n", self.partialOverlaps)
}
