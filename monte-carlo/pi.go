package main

import (
	"fmt"
	"math/rand"
)

const (
	TOTAL_RUNS = 1000000
)

func main() {
	var runs [TOTAL_RUNS]bool

	for i := 0; i < TOTAL_RUNS; i++ {
		x, y := rand.Float64(), rand.Float64()

		if x*x+y*y < 1 {
			runs[i] = true
		}
	}

	hits := 0
	for _, x := range runs {
		if x {
			hits++
		}
	}

	fmt.Println(4 * float32(hits) / float32(TOTAL_RUNS))
}
