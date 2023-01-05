def get_level(level_id):
    id =  level_id
    with open(id, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))

# print(get_level("levels.txt"))