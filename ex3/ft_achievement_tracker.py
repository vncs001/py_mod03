#! python3
import sys
import random

def gen_player_achievements() -> set[str]:
    achievements: list[str] = ["Luck Duck", "First Blood", "Go Get Some Sun",
        "The Part Where He Kills You", "Snake Eater",
        "Little Rocket Man", "Dastardly", "Why Would You Do That?",
        "So Serious?", "Mister Chief", "Don't Tase Me, Bro",
        "Ah, e tal, sou bué da rebelde", "Go Ahead, Free-Form Jazz",
        "Oops", "Plumber's Virtual Academy", "Irony", "We're All Mad Here"]
    total = random.randint(1, len(achievements))
    plyr_achvs: set[str] = set(random.sample(achievements, total))
    return plyr_achvs


if __name__ == "__main__":
    print("Oi")
