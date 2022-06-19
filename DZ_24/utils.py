import re
from typing import Iterator, Any

def slice_limit(it: Iterator, value: int) -> Iterator:
    i = 0
    for item in it:
        if i < value:
            yield item
        else:
            break
        i += 1


def build_query(it: Iterator, cmd: str, value: str) -> Iterator:
    res = map(lambda v: v.strip(), it)
    if cmd == 'filter':
        return filter(lambda v: value in v, res)
    if cmd == 'sort':
        return iter(sorted(res, reverse=bool(value)))
    if cmd == 'unique':
        return iter(set(res))
    if cmd == 'limit':
        return slice_limit(res, int(value))
    if cmd == 'map':
        return map(lambda v: v.split(' ')[int(value)], res)
    if cmd == 'regex':
        regex = re.compile(value)
        return filter(lambda x: regex.search(x), res)
    return res



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

