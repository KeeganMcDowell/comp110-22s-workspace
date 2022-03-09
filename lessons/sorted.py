def sorted(a_list: list[int]) -> list[int]:
    sorted_list: list[int] = [0]
    idx: int = 0
    while idx < len(a_list):
        aidx: int = 0
        if a_list[idx] > sorted_list[aidx]:
            sorted_list.append(a_list[idx])
        else:
            aidx += 1
        idx += 1
    return sorted_list