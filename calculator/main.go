package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Op string

const (
	QUIT     Op = "q"
	PLUS     Op = "+"
	MINUS    Op = "-"
	MULTIPLY Op = "*"
	DIVIDE   Op = "/"
)

func getInput(reader *bufio.Reader) (string, error) {
	s, err := reader.ReadString('\n')
	if err != nil {
		return "", fmt.Errorf("Failed to read input: %v\n", err)
	}

	s = strings.TrimSpace(s)
	if Op(s) == QUIT {
		fmt.Println("Quitting...")
		os.Exit(0)
	}

	return s, nil
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	done := false
	for !done {
		var input string
		fmt.Printf("Please enter a number: \n")
		input, err := getInput(reader)
		if err != nil {
			log.Fatalf("failed to get input: %v\n", err)
		}

		n1, err := strconv.ParseInt(input, 10, 32)
		if err != nil {
			log.Fatalf("failed to get number: %v\n", err)
		}

		fmt.Printf("Please enter a number: \n")
		input, err = getInput(reader)
		if err != nil {
			log.Fatalf("failed to get input: %v\n", err)
		}

		n2, err := strconv.ParseInt(input, 10, 32)
		if err != nil {
			log.Fatalf("failed to get number: %v\n", err)
		}

		fmt.Printf("Please enter a operation (+, -, *, /): \n")
		input, err = getInput(reader)
		if err != nil {
			log.Fatalf("failed to get input: %v\n", err)
		}

		switch op := Op(input); op {
		case PLUS:
			fmt.Printf("%d %s %d = %d\n", n1, op, n2, n1+n2)
			done = true
		case MINUS:
			fmt.Printf("%d %s %d = %d\n", n1, op, n2, n1-n2)
			done = true
		case MULTIPLY:
			fmt.Printf("%d %s %d = %d\n", n1, op, n2, n1*n2)
			done = true
		case DIVIDE:
			fmt.Printf("%d %s %d = %d\n", n1, op, n2, n1/n2)
			done = true
		default:
			fmt.Printf("failed to match an operation: %s\n", op)
			fmt.Printf("Try Again!\n")
		}
	}
}
