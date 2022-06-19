
def build_query(it, cmd, value):
    res = map(lambda v: v.strip(), it)
    if cmd == 'filter':
        res = filter(lambda v: value in v, res)
    if cmd == 'sort':
        value = bool(value)
        res = sorted(res, reverse=value)
    if cmd == 'unique':
        res = set(res)
    if cmd == 'limit':
        value = int(value)
        res = list(res)[:value]
    if cmd == 'map':
        value = int(value)
        res = map(lambda v: v.split(' ')[value], res)
    # match cmd:
    #     case 'filter':
    #         res = filter(lambda v: value in v, res)
    #     case 'sort':
    #         value = bool(value)
    #         res = sorted(res, reverse=value)
    #     case 'unique':
    #         res = set(res)
    #     case 'limit':
    #         value = int(value)
    #         res = list(res)[:value]
    #     case 'map':
    #         value = int(value)
    #        res = map(lambda v: v.split(' ')[value], res)

    return res