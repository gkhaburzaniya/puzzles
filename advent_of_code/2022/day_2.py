puzzle_input = open("day_2_input.txt")

translation = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
               'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
bad_translation = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}


def bad_score_throw(opponent, player):
    opponent, player = translation[opponent], bad_translation[player]
    score = 0
    if player == 'Rock':
        score += 1
    elif player == 'Paper':
        score += 2
    elif player == 'Scissors':
        score += 3

    if opponent == player:
        score += 3
    elif opponent == 'Rock' and player == 'Paper':
        score += 6
    elif opponent == 'Paper' and player == 'Scissors':
        score += 6
    elif opponent == 'Scissors' and player == 'Rock':
        score += 6
    return score


def score_throw(opponent, outcome):
    opponent, outcome = translation[opponent], translation[outcome]
    score = 0

    if outcome == 'Lose':
        if opponent == 'Rock':
            score += 3
        elif opponent == 'Paper':
            score += 1
        elif opponent == 'Scissors':
            score += 2
    elif outcome == 'Draw':
        score += 3
        if opponent == 'Rock':
            score += 1
        elif opponent == 'Paper':
            score += 2
        elif opponent == 'Scissors':
            score += 3
    elif outcome == 'Win':
        score += 6
        if opponent == 'Rock':
            score += 2
        elif opponent == 'Paper':
            score += 3
        elif opponent == 'Scissors':
            score += 1
    return score


bad_total_score = 0
total_score = 0
for line in puzzle_input:
    bad_total_score += bad_score_throw(*line.split())
    total_score += score_throw(*line.split())

print(bad_total_score)
print(total_score)
