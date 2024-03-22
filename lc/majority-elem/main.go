package main

var nums []int = []int{2, 2, 1, 1, 1, 2, 2}

func main() {
	var cand, count int
	for _, j := range nums {
		switch {
		case count == 0:
			cand = j
			count++
		case cand == j:
			count++
		case cand != j:
			count--
		}
	}

	println(cand)
}
