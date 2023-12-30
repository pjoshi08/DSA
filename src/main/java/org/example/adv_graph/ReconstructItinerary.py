class Solution:
    # Time Limited exceeded for below solution
    def findItinerary2(self, tickets):
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res

    def findItinerary(self, tickets):
        graph = {}
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        for src in graph.keys():
            graph[src].sort(reverse=True)
            # sort children in descending order so that we can pop last element
            # instead of pop out first element which is costly operation
        stack = []
        res = []
        stack.append("JFK")
        # Start with JFK as starting point and keep adding the next child to traverse
        # for the last airport at the top of the stack. If we reach to an airport from where
        # we can't go further, then add it to the result. This airport should be the last to go
        # since we can't go anywhere from here. That's why we return the reverse of the result.
        # After this backtrack to the top of the airport in the stack and continue to traverse
        # its children

        while stack:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0:
                # Check if elem is in graph as there may be a case when there is no out edge from
                # an airport. In that case, it won't be present as a key in the graph
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
                # If there is no further children to traverse then add that airport to res.
                # This airport should be the last to go since we can't go anywhere from this,
                # that's why we return the reverse of the result
        return res[::-1]
