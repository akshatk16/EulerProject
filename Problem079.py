from time import time
from collections import defaultdict, deque


start = time()


def valid_digits(keys):
	digits = set()
	for num in keys:
		for dig in num:
			digits.add(dig)
	return digits


def precedence(key):
	l = len(key)
	for i in range(l - 1):
		for j in range(i + 1, l):
			yield key[i], key[j]


def make_graph(keys):
	graph = defaultdict(set)
	for key in keys:
		for x, y in precedence(key):
			graph[x].add(y)
	return graph


def shortest_path(start, graph, digits):
	queue = deque([(start, [start])])
	while queue:
		curr, path = queue.popleft()
		neighbours = graph.get(curr, [])
		for neighbour in neighbours:
			new_path = path + [neighbour]
			if not digits - set(new_path):
				return (len(new_path), new_path)
			queue.append((neighbour, new_path))


def solve(keylog):
	digits = valid_digits(keylog)
	graph = make_graph(keylog)
	solution = []
	for vertex in graph:
		code = shortest_path(vertex, graph, digits)
		if code:
			solution.append(code)
	return solution


if __name__ == "__main__":

	file = open("p079_keylog.txt", "r")
	t = file.read()
	keys = t.strip().split('\n')

	solution = solve(keys)

	sol = str()
	for i, j in solution:
		for k in j:
			sol += k
	print(sol)


end = time()
print(int((end-start)*1000), "ms")
