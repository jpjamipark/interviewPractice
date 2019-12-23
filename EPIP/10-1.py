def merge_sorted_arrays(sorted_arrays):
	min_heap = []
	sorted_arrays_iter = [iter(x) for x in sorted_arrays]

	for i, it in enumerate(sorted_arrays_iter):
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap, (first_element,i))

	result = []
	while min_heap:
		smallest_entry, smallest_array_i = heapq.heappop(min_heap)
		smallest_array_iter = sorted_arrays_iters[smallest_array_i]
		result.append(smallest_entry)
		next_element = next(smallest_array_iter, None)
		if next_element is not None:
			heapq.heappush(min_heap, (next_element,smallest_array_i))
	return result

def merge_sorted_arrays(sorted_arrays):
	min_heap = []
	sorted_arrays_iter = [iter(l) for l in sorted_arrays ]
	for iterator in sorted_arrays_iter:
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap,(first_element,i))
	result = []
	while min_heap:
		smallest_entry, smallest_array_i = heapq.heappop(min_heap)
		smallest_array_iter = sorted_arrays_iter[smallest_array_i]
		val = next(smallest_array_iter, None)
		if val is not None:
			heapq.heappush(min_heap,(val,smallest_array_i))
	return result
