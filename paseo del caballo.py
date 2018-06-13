from pprint import pprint

board = [[0 for y in range(8)] for x in range(8)]
counter = 2


def show_board():
    pprint(board)


def moviment_valid():
    return [
        [1, 2], [-1, 2], [-1, -2],
        [-2, 1], [2, 1], [2, -1],
        [-2, -1], [1, -2],
    ]


def search_moviment(row, column):
    global counter

    temporal = []
    dicc_router = {}

    for valide in moviment_valid():
        row_valide = row + valide[0]
        column_valide = column + valide[1]
        if 0 <= row_valide <= 7 and 0 <= column_valide <= 7:
            if not board[row_valide][column_valide]:
                temporal.append([row_valide, column_valide])
    dicc_router[(row, column)] = temporal
    dicc_router.update({'size': len(temporal)})
    return dicc_router


def main():
    row, column = 7, 7
    board[row][column] = 1
    global counter
    for iterator in range(63):
        dic = search_moviment(row=row, column=column)
        lista = sorted([search_moviment(*i) for i in dic.get((row, column))],
                       key=lambda x: x.get('size'))
        position_moviment = list(lista[0].keys())[0]
        row, column = position_moviment
        board[row][column] = counter
        counter += 1
    show_board()


main()
