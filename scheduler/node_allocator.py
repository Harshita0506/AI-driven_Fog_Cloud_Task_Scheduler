import heapq             #to make nodes(heaps) in environment

def create_nodes(prefix, count):                #create node in selected environment
    nodes = [(0.0, f"{prefix}-{i+1}") for i in range(count)]
    heapq.heapify(nodes)
    return nodes

def allocate_node(heap, task_load):       #take the root node(pop it)
    load, node = heapq.heappop(heap)
    load += task_load                       #add task_load to node _load
    heapq.heappush(heap, (load, node))      # after updating the node load , add the node back to the heap
    return node

def apply_decay(heap, decay):  #some tasks get completed so ther free up the space
    updated = []
    while heap:
        load, node = heapq.heappop(heap)
        load = max(0, load - decay)         #maintain node_load by substracting some load from  it
        updated.append((load, node))        #add the node to updated list
    heapq.heapify(updated)                  #heapify update
    return updated
