package sorts

import (
	"math/rand"
	"slices"
	"testing"
)

func getCases() ([][]int, [][]int) {
	c := [][]int{
		{1},
		{1, 2, 3, 4, 5, 6, 7},
		{4, 1, 6, 4},
		{3, 1, 2},
		{2, 1},
		{7, 6, 5, 4, 3, 2, 1},
		{},
		{3, 7, 8, 5, 2, 1, 9, 5, 4},
	}

	e := [][]int{
		{1},
		{1, 2, 3, 4, 5, 6, 7},
		{1, 4, 4, 6},
		{1, 2, 3},
		{1, 2},
		{1, 2, 3, 4, 5, 6, 7},
		{},
		{1, 2, 3, 4, 5, 5, 7, 8, 9},
	}

	return c, e
}

func getRandomCases() [][]int {
	var cases [][]int
	lengths := []int{10, 50, 100, 1000, 10000}
	for _, l := range lengths {
		var rndVec []int
		for j := 0; j < l; j++ {
			rndVec = append(rndVec, rand.Intn(l))
		}
		cases = append(cases, rndVec)
	}

	return cases
}

func TestBubbleSort(t *testing.T) {
	c, e := getCases()
	for i := 0; i < len(c); i++ {
		sorted := BubbleSort(c[i])
		res := slices.Compare(e[i], sorted)
		if res != 0 {
			t.Errorf("Test Case %d FAILED -- expected: %v, got %v", i, e[i], sorted)
		}
	}
}

func TestInsertionSort(t *testing.T) {
	c := getRandomCases()
	for i := 0; i < len(c); i++ {
		sorted := InsertionSort(c[i])
		expected := BubbleSort(c[i])
		res := slices.Compare(expected, sorted)
		if res != 0 {
			t.Errorf("Test Case %d FAILED -- expected: %v, got %v", i, expected, sorted)
		}
	}
}

func TestSelectionSort(t *testing.T) {
	c := getRandomCases()
	for i := 0; i < len(c); i++ {
		sorted := SelectionSort(c[i])
		expected := BubbleSort(c[i])
		res := slices.Compare(expected, sorted)
		if res != 0 {
			t.Errorf("Test Case %d FAILED -- expected: %v, got %v", i, expected, sorted)
		}
	}
}

func TestQuickSort(t *testing.T) {
	c := getRandomCases()
	for i := 0; i < len(c); i++ {
		sorted := QuickSort(c[i])
		expected := BubbleSort(c[i])
		res := slices.Compare(expected, sorted)
		if res != 0 {
			t.Errorf("Test Case %d FAILED -- expected: %v, got %v", i, expected, sorted)
		}
	}
}
