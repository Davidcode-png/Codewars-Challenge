import collections

class Solution:
	def ladderlength(self,beginWord: str, endWord: str, wordList) -> int:
		if endWord not in wordList:
			return 0

		# Creating a adjacency list having all word patterns
		nei = collections.defaultdict(list)
		wordList.append(beginWord)
		for word in wordList:
			for j in range(len(word)):
				pattern = word[:j] + "*" + word[j+1:]
				nei[pattern].append(word)

		# Now BFS Time (Breadth First Search)
		visited = set([beginWord])
		q = collections.deque([beginWord])
		res = 1

		while q:
			for i in range(q):
				word = q.popleft()
				if word == endWord:
					return res
				for j in range(len(word)):
					pattern = word[:j] + "*" + word[j+1:]
					for neighbor in nei[pattern]:
						if neighbor not in visited:
							visited.add(neighbor)
							q.append(neighbor)

			res += 1
		return 0
