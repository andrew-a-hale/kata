package sorts

// bubble large elements to the end of the list by swapping adjacent pairs
func BubbleSort(xs []int) []int {
	for i := 0; i < len(xs); i++ {
		for j := 0; j < len(xs)-i-1; j++ {
			if xs[j] > xs[j+1] {
				xs[j], xs[j+1] = xs[j+1], xs[j]
			}
		}
	}

	return xs
}

// sort list up to i by dragging ith element to its position by adjacent swaps
func InsertionSort(xs []int) []int {
	for i := 1; i < len(xs); i++ {
		tmp := xs[i]
		j := i - 1
		for ; j > -1 && tmp < xs[j]; j-- {
			xs[j+1] = xs[j]
		}
		xs[j+1] = tmp
	}

	return xs
}

// find the minimum value and swap min index with i
func SelectionSort(xs []int) []int {
	for i := 0; i < len(xs); i++ {
		min := i
		for j := i; j < len(xs); j++ {
			if xs[j] < xs[min] {
				min = j
			}
		}
		xs[i], xs[min] = xs[min], xs[i]
	}

	return xs
}

// recursively solve regions left and right of the pivot
func QuickSort(xs []int) []int {
	if len(xs) < 2 {
		return xs
	}

	pivot := xs[len(xs)/2]
	lo, hi := 0, len(xs)-1
	for lo < hi {
		for xs[lo] < pivot {
			lo++
		}
		for xs[hi] > pivot {
			hi--
		}
		if lo < hi {
			xs[lo], xs[hi] = xs[hi], xs[lo]
			lo++
		}
	}

	copy(xs[:lo], QuickSort(xs[:lo]))
	copy(xs[hi:], QuickSort(xs[hi:]))
	return xs
}
