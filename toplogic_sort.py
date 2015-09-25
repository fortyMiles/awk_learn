open_files = open('node.data')

pred_count = {}
succ_list = {}
succ_count = {}

for line in open_files.readlines():
    nodes = line.rstrip().split(' ')

    if nodes[1] in pred_count:
        pred_count[nodes[1]] += 1
    else:
        pred_count[nodes[1]] = 1

    if nodes[0] not in pred_count:
        pred_count[nodes[0]] = 0

    if nodes[0] in succ_count:
        succ_count[nodes[0]] += 1
    else:
        succ_count[nodes[0]] = 1

    succ_list[nodes[0], succ_count[nodes[0]]] = nodes[1]

queue_begin = 0
queue_end = 0
queue = []
predct_length = len(pred_count)

for node in pred_count:
    if pred_count[node] == 0:
        queue.append(node)
        queue_end += 1


while queue_begin < queue_end:
    node = queue[queue_begin]
    queue_begin += 1
    print(node)

    if node in succ_count:  # if this node has successor(s)
        for i in range(succ_count[node]):
            succ_node = succ_list[node, i + 1]
            pred_count[succ_node] -= 1
            if pred_count[succ_node] == 0:
                queue_end += 1
                queue.append(succ_node)

if queue_end != predct_length:
    print(" tsort error: there is a cycle in input")
