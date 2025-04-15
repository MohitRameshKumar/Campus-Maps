classrooms = ['A', 'B', 'C', 'D', 'E']

distances = {
    ('A', 'B') : 4,
    ('A', 'C') : 2,
    ('B', 'C') : 1,
    ('B', 'D') : 2,
    ('C', 'D') : 4,
    ('C', 'E') : 5,
    ('E', 'D') : 1,
}

start = 'A'
end = 'D'

def minimum(distances, unexplored):
    return min(unexplored, key=lambda k: distances[k])

def dijkstra(airports, lines, start, end):
    distances = {airport: float('inf') for airport in airports}
    distances[start] = 0
    previous = {airport: None for airport in airports}
    unexplored = set(airports)

    while unexplored:
        current = minimum(distances, unexplored)
        if current == end:
            break
        unexplored.remove(current)

        for (src, dst), time in lines.items():
            if src == current and dst in unexplored:
                alt = distances[current] + time
                if alt < distances[dst]:
                    distances[dst] = alt
                    previous[dst] = current
            elif dst == current and src in unexplored:
                alt = distances[current] + time
                if alt < distances[src]:
                    distances[src] = alt
                    previous[src] = current

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]

    return distances[end], path

time, path = dijkstra(classrooms, distances, start, end)
print(f"Minimum time: {time}")
print(f"Path: {' -> '.join(path)}")

