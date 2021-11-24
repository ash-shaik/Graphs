from collections import defaultdict


class DGraph:
    """ Directed Graph Class """

    def __init__(self, numNodes, edges):
        self.numNodes = numNodes
        self.adjList = defaultdict(list)
        for v1, v2 in edges:
            self.adjList[v1].append(v2)

    def canFinish(self, course, visited):
        """
        A DFS of course recursing through the edges.
        :param course:
        :param visited:
        :return:
        """
        visited[course] = 1

        for preRequisite in self.adjList[course]:
            if visited[preRequisite] == 0:
                if not self.canFinish(preRequisite, visited): return False
            elif visited[preRequisite] == 1:
                return False
            visited[course] = 2
            return True


def canFinishCourseSchedule(courseSchedule):
    """
    Checks if a Course Schedule can be completed.
    Method Uses topological sort to determine this.
    :param courseSchedule:
    :return:
    """
    numCourses = courseSchedule.numNodes
    visited = [0 for _ in range(numCourses)]

    for course in range(numCourses):
        if visited[course] == 0:
            if not courseSchedule.canFinish(course, visited):
                return False
    return True


def alienDictionary(words):
    """
    #
    :param words: Already sorted words from alien language
    :return: Return a string of the unique letters in the new alien language
             sorted in lexicographically increasing order by the new language's rules.
    """
    adjList = {letter: set() for word in words for letter in word}
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        minLen = min(len(word1), len(word2))

        if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
            return ""
        for j in range(minLen):
            if word1[j] != word2[j]:
                adjList[word1[j]].add(word2[j])
                break
    visited = {}
    result = []

    def dfs(letter):
        if letter in visited:
            return visited[letter]
        visited[letter] = True
        for neighbor in adjList[letter]:
            if dfs(neighbor):
                return True
        visited[letter] = False
        result.append(letter)

    for letter in adjList:
        if dfs(letter):
            return ""
    result.reverse()
    return "".join(result)


def getCourseSchedule(numCourses, preRequisites):
    courses = defaultdict(list)
    visited = [0] * numCourses
    courseOrdering = []

    for current, preReq in preRequisites:
        courses[current].append(preReq)

    def dfs(course):
        visited[course] = 1

        for preRequisite in courses[course]:
            if visited[preRequisite] == 0:
                if not dfs(preRequisite): return False
            elif visited[preRequisite] == 1:
                return False
        visited[course] = 2
        courseOrdering.append(course)
        return True

    for course in range(numCourses):
        if visited[course] == 0:
            if not dfs(course):
                return [-1]
    return courseOrdering


if __name__ == '__main__':
    numCourses = 4
    preRequisites = [[1, 0], [1, 2], [3, 1], [0, 3]]
    courseSchedule = DGraph(numCourses, preRequisites)
    print(canFinishCourseSchedule(courseSchedule))

    print(alienDictionary(["wrt", "wrf", "er", "ett", "rftt"]))

    preRequisites = [[0, 1], [1, 2], [3, 4], [4, 5], [5, 6]]
    print(getCourseSchedule(7, preRequisites))
