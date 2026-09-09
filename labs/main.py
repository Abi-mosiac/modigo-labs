def unmatched_skus(warehouse_a, warehouse_b):
    # TODO: compute the symmetric difference using union/intersection/difference,
    # without using ^ or .symmetric_difference()
    a = warehouse_a - warehouse_b
    b = warehouse_b - warehouse_a
    return a.union(b)