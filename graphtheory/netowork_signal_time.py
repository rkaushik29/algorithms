import heapq

def network_delay_time(times, N, K):
    graph = {}
    for u, v, w in times:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    dist = {node: float('inf') for node in range(1, N + 1)}
    min_heap = [(0, K)]

    while min_heap:
        cur_dist, cur_node = heapq.heappop(min_heap)

        if cur_dist > dist[cur_node]:
            continue

        dist[cur_node] = cur_dist
        if cur_node in graph:
            for neighbor, weight in graph[cur_node]:
                new_dist = cur_dist + weight
                if new_dist < dist[neighbor]:
                    heapq.heappush(min_heap, (new_dist, neighbor))
                    dist[neighbor] = new_dist

    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1
