def distance(o1, o2):
    if len(o1) != len(o2):
        raise ValueError("Las oraciones no miden lo mismo")

    return sum(a != b for a, b in zip(o1, o2))