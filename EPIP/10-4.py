def get_k_closest(pointList, k):
	max_heap = []
	for i in range(k):
		point = pointList[i]
		dist = -1*(point[0]*point[0]+point[1]*point[1]+point[2]*point[2])
		heapq.heappush(max_heap, (dist,pointList[i]))
	for i in range(k, len(pointList)):
		point = pointList[i]
		dist = -1*(point[0]*point[0]+point[1]*point[1]+point[2]*point[2])
		if(max_heap[0][0] < dist):
			heapq.heappushpop(max_heap, (dist, pointList[i]))
	return [val[1] for val in max_heap]


