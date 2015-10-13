def calculate_score(score_card):
    score = 0
    frames = score_card.split()
    return sum((score_frame(number, frames) for number in range(len(frames))))


def score_frame(number, score_list):
    if number == 9:
        return score_last_frame(score_list[number])
    current_frame = score_list[number]
    score = 0
    if current_frame[0] == "X":
        score = 10
        next_balls = score_list[number + 1]
        if len(next_balls) < 2:
            next_balls += score_list[number + 2]
        if next_balls[1] == "/":
            score += 10
        else:
            for bonus in next_balls[:2]:
                if bonus == "X":
                    score += 10
                else:
                    bonus = bonus if bonus != "-" else 0
                    score += int(bonus)
    elif current_frame[1] == "/":
        score = 10
        next_ball = score_list[number + 1]
        if next_ball[0] == "X":
            score += 10
        else:
            score += int(next_ball[0])
    else:
        score = sum((int(x) for x in current_frame if x is not "-"))
    
    return score


def score_last_frame(score):
    if score[0] == "X":
        if score[2] == "X":
            return 30
        elif score[2] == "/":
            return 20
        else:
            return 10 + sum(int(x) for x in score[1:3])
    elif score[1] == "/":
        bonus = 10 if score[2] == "X" else int(score[2])
        return 10 + bonus
    else:
        return sum(int(x) for x in score if x is not "-")


if __name__ == "__main__":
    print(calculate_score("X X X X X X X X X XXX"))
    print(calculate_score("X -/ X 5- 8/ 9- X 81 1- 4/X"))
    print(calculate_score("62 71  X 9- 8/  X  X 35 72 5/8"))
    print(calculate_score("62 71 X 9- 8/ X X 35 72 53"))
