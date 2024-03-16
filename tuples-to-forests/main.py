import gc
import itertools
import random
import time
from typing import Dict, List, Set

from node import TreeNode


def fast_dedup(arr: List[any]) -> List[any]:
    arr = sorted(arr)
    return list(k for k, _ in itertools.groupby(arr))


raw = [
    [1, 2],
    [2, 1],
    [3, 6],
    [7, 8],
    [3, 8],
    [9, 11],
    [10, 8],
    [9, 12],
    [12, 9],
    [9, 8],
    [16, 15],
    [3, 4],
    [17, 15],
    [18, 15],
    [3, 5],
]


def grouped_relationships(data: List[List[int]]) -> List[Dict[str, List]]:
    sources = [source for source, _ in data]
    targets = [target for _, target in data]
    source_nodes = {}
    target_nodes = {}
    for s in fast_dedup(sources):
        source_node = TreeNode({"id": s})
        targets_for_source = itertools.compress(targets, [x == s for x in sources])
        for t in targets_for_source:
            target_node = target_nodes.get(t, TreeNode({"id": t}))
            target_node.add_parent(source_node)
            target_nodes[t] = target_node
            source_node.add_child(target_node)
        source_nodes[s] = source_node

    groups = []
    for _, source in source_nodes.items():
        groups.append([parent for parent in source.get_related_parents()])
    groups = fast_dedup(groups)

    families = []
    for group in groups:
        targets = []
        for source in group:
            sources = source.get_children()
            targets.append(sources)
        targets = fast_dedup(itertools.chain.from_iterable(targets))
        families.append(
            {"sources": [group.get_id() for group in group], "targets": targets}
        )

    return families


def group_sources_targets(data: List[List[int]]) -> List[Dict[str, List[int]]]:
    grouped_data = []

    for source, target in data:
        group_found = False
        for i, group in enumerate(grouped_data):
            matched = source in group["sources"] or target in group["targets"]
            if matched and group_found:
                orphan = grouped_data.pop(i)
                grouped_data[first_match]["sources"].extend(
                    [
                        source
                        for source in orphan["sources"]
                        if source not in grouped_data[first_match]["sources"]
                    ]
                )
                grouped_data[first_match]["targets"].extend(
                    [
                        target
                        for target in orphan["targets"]
                        if target not in grouped_data[first_match]["targets"]
                    ]
                )
                break

            if matched and not group_found:
                first_match = i
                if source not in group["sources"]:
                    group["sources"].append(source)
                if target not in group["targets"]:
                    group["targets"].append(target)
                group_found = True

        if not group_found:
            grouped_data.append({"sources": [source], "targets": [target]})

    return grouped_data


def group_sources_targets_denested(data: List[List[int]]) -> List[List[Set[int]]]:
    grouped_data = []

    for source, target in data:
        group_found = False
        for i, group in enumerate(grouped_data):
            matched = source in group[0] or target in group[1]
            if matched and group_found:
                orphan = grouped_data.pop(i)
                grouped_data[first_match][0].update(orphan[0])
                grouped_data[first_match][1].update(orphan[1])
                break

            if matched and not group_found:
                first_match = i
                group[0].add(source)
                group[1].add(target)
                group_found = True

        if not group_found:
            grouped_data.append([set([source]), set([target])])

    return grouped_data


gc.disable()
print("dict-based")
for _ in range(10):
    data = random.sample(raw, k=len(raw))
    start_time = time.perf_counter_ns()
    group_sources_targets(data)
    print(time.perf_counter_ns() - start_time)

print("set-based")
for _ in range(10):
    data = random.sample(raw, k=len(raw))
    start_time = time.perf_counter_ns()
    group_sources_targets_denested(data)
    print(time.perf_counter_ns() - start_time)

print("tree-based")
for _ in range(10):
    data = random.sample(raw, k=len(raw))
    start_time = time.perf_counter_ns()
    grouped_relationships(data)
    print(time.perf_counter_ns() - start_time)
