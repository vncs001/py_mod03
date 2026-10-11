#!python3
import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    players: list[str] = [
                "Thorin", "balin", "dwalin",
                "Fili", "Kili", "Oin", "víli", "thrainor",
                "Gloin", "Dori",  "Kazad",
                "Bifur", "bofur", "bombur", "dain", "rurik",
        ]
    print(f"Initial list of players: {players}\n")

    cap: list[str] = []
    not_cap: list[str] = []
    for player in players:
        if player == player.capitalize():
            cap.append(player)
        else:
            not_cap.append(player)
            cap.append(player.capitalize())
    print(f"New list with all names capitalized: {cap}")
    print(f"New list of capitalized names only: {not_cap}\n")

    players_scores: list[tuple[str, int]] = []
    for player in cap:
        players_scores.append((player, random.randint(0, 1000)))
    print(f"Score dict: {players_scores}")

    score_list: list[int] = []
    for _, scores in players_scores:
        score_list.append(scores)
    average = round(sum(score_list) / len(score_list), 2)
    print(f"Score average is {average}\n")

    top5: list[tuple[str, int]] = []

    for name, score in players_scores:
        higher = 0
        for _, other in players_scores:
            if other > score:
                higher += 1
        if higher < 5:
            top5.append((name, score))

    print(f"High scores: {top5}")
