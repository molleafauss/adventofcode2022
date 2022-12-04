package main

import (
	"bufio"
	"fmt"
	"os"
)

type Parser interface {
	Parse(line string)

	Solve()
}

func loader(filename string, parser Parser) {
	file, err := os.Open(filename)
	if err != nil {
		panic(fmt.Sprintf("Error opening input: %v\n", err))
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parser.Parse(line)
	}
	parser.Solve()
}

func main() {
	loader("../files/day01-calories.txt", &Day01{elves: make([]ElfFood, 10)})
}
