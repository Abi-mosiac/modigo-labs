def path_hits_blocked(blocked, path):
    # TODO: check whether any position in `path` also appears in `blocked`
    for block in blocked:
        if block in path:
            return True 
    return False

print(path_hits_blocked({(1,1), (2,2)}, [(0,0),(1,1)]))