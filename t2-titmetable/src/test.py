import heapq

pq = []

heapq.heappush(pq, (8, 'teste8'))
heapq.heappush(pq, (5, 'teste5'))
heapq.heappush(pq, (4, 'teste4'))
heapq.heappush(pq, (6, 'teste6'))
heapq.heappush(pq, (10, 'teste10'))
heapq.heappush(pq, (7, 'teste7'))

while pq:
  print(heapq.heappop(pq))