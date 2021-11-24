from collections import defaultdict


class DGraph:
    """ Directed Graph Class """

    def __init__(self, numNodes, edges):
        self.numNodes = numNodes
        self.adjList = defaultdict(list)
        for v1, v2 in edges:
            self.adjList[v1].append(v2)

    def canFinish(self, course, visited):
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


if __name__ == '__main__':
    numCourses = 4
    preRequisites = [[1, 0], [1, 2], [3, 1], [0, 3]]
    courseSchedule = DGraph(numCourses, preRequisites)
    print(canFinishCourseSchedule(courseSchedule))
