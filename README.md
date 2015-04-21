# GraVer (Graph, Vertex)

[![Build Status](https://travis-ci.org/krzysztof-magosa/graver.svg?branch=master)](https://travis-ci.org/krzysztof-magosa/graver)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/krzysztof-magosa/graver/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/krzysztof-magosa/graver/?branch=master)

My little experiment in Python with graphs and Dijkstra algo.  
Don't treat it too seriously, it's done just for fun :-)

## Example
```python
from graver import DirectedGraph
from graver import shortest_path

graph = DirectedGraph()

graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')

graph.add_edge('a', 'b', weight=1)
graph.add_edge('b', 'c', weight=1)

path = shortest_path(graph, 'a', 'c')

# Below function will fail because
# graph is directed, so there is
# no path from c to a
shortest_path(graph, 'c', 'a')
```
