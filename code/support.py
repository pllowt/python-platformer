from csv import reader


def import_csv_layout(path: str) -> list:
    """
    imports csv and returns list of each row
    of the file which is also a list
    :param path:
    :return: list of lists [[]]
    """
    terrain_map = []
    with open(path) as level_map:
        level = reader(level_map, delimiter=',')
        for row in level:
            terrain_map.append(list(row))
        return terrain_map
