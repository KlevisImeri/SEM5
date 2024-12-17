class AStarNodeSelector:
    def nextNode(self, search, openList, closedList):
        return  min(openList, key=lambda n: search.heur(n.location)+n.cost)
