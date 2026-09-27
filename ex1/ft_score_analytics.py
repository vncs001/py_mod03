#! python3
import sys


def score_display(lst: list[str]):
    try:
        lst_nbr: list[int] = []
        for arg in lst[1:]:
            try:
                score = int(arg)
                lst_nbr.append(score)
            except ValueError:
                print(f"Invalid parameter: {arg}")
        if len(lst_nbr) < 1:
            raise ValueError("")
        print(f"Scores processed: {lst_nbr}")
        print(f"Total players: {len(lst_nbr)}")
        print(f"Total score: {sum(lst_nbr)}")
        print(f"Average score: {sum(lst_nbr)/len(lst_nbr)}")
        print(f"High score: {max(lst_nbr)}")
        print(f"Low score: {min(lst_nbr)}")
        print(f"Score range: {max(lst_nbr) - min(lst_nbr)}")
    except ValueError:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ..."
              )


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_display(sys.argv)
