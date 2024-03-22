package main

import (
	"container/heap"
)

type Task struct {
	id       byte
	index    int
	priority int
}
type TaskQueue []*Task

func (h TaskQueue) Len() int           { return len(h) }
func (h TaskQueue) Less(i, j int) bool { return h[i].priority > h[j].priority }
func (h TaskQueue) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
	h[i].index = i
	h[j].index = j
}
func (h *TaskQueue) Push(x any) {
	n := len(*h)
	task := x.(*Task)
	task.index = n
	*h = append(*h, task)
}
func (h *TaskQueue) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func scheduler(tasks []byte, n int) int {
	freq := make(map[byte]int)
	for _, task := range tasks {
		freq[task]++
	}

	h := make(TaskQueue, len(freq))
	i := 0
	for id, priority := range freq {
		h[i] = &Task{id: id, index: i, priority: priority}
		i++
	}
	heap.Init(&h)

	used := make(map[byte]int)
	cycles := 0
	for len(freq) > 0 {
		if len(h) > 0 {
			task, _ := heap.Pop(&h).(*Task)

			// consume task
			used[task.id] = n + 1
			freq[task.id]--
			if freq[task.id] == 0 {
				delete(freq, task.id)
			}
		}

		// decrement timeout
		for k := range used {
			used[k]--
			if used[k] == 0 && freq[k] > 0 {
				heap.Push(&h, &Task{id: k, index: -1, priority: freq[k]})
			}
		}

		cycles++
	}

	return cycles
}

func main() {
	var tasks []byte = []byte{'A', 'A', 'A', 'B', 'B', 'B'}
	var timeout int = 2
	println(scheduler(tasks, timeout))
}
