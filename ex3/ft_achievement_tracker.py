#! python3
import random


def gen_player_achievements() -> set[str]:
    achievements: list[str] = [
                                "Luck Duck", "First Blood", "Go Get Some Sun",
                                "The Part Where He Kills You", "Snake Eater",
                                "Little Rocket Man", "Dastardly",
                                "Why Would You Do That?",
                                "So Serious?", "Mister Chief",
                                "Don't Tase Me, Bro",
                                "Ah, e tal, sou bué da rebelde",
                                "Go Ahead, Free-Form Jazz",
                                "Oops", "Plumber's Virtual Academy", "Irony",
                                "We're All Mad Here"]
    total = random.randint(1, len(achievements))
    plyr_achvs: set[str] = set(random.sample(achievements, total))

    return plyr_achvs


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    diff: set[str] = set()
    comm: set[str] = set()

    for player in players:
        print(f"Player {player}: {players[player]}\n")

    for achvs in players.values():
        diff = diff.union(achvs)
        if comm == set():
            comm = achvs
        else:
            comm = comm.intersection(achvs)

    print(f"All distinct achievements: {diff}\n")
    print(f"Common achievemens: {comm}\n")

    for name, achvs in players.items():
        other: set[str] = set()
        for other_name, other_achvs in players.items():
            if other_name != name:
                other = other.union(other_achvs)
        exclusive = achvs.difference(other)
        print(f"Only {name} has: {exclusive}")

    print("\n")

    for name, achvs in players.items():
        other: set[str] = set()
        for other_name, other_achvs in players.items():
            if other_name != name:
                other = other.union(other_achvs)
        missing = other.difference(achvs)
        print(f"{name} is missing: {missing}")
