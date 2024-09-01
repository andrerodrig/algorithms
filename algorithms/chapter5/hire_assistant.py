import random


class Candidate:
    def __init__(self) -> None:
        self.interviewed: bool = False
        self.score = -1

    def interview(self) -> None:
        self.interviewed = True
        self.score = random.randint(0, 10)


def hire_assistant(candidates: list[Candidate]) -> int:
    best_score = -1    # Dummy candidate
    best_index = -1
    for index, candidate in enumerate(candidates):
        candidate.interview()
        if candidate.score > best_score:
            best_index = index
            best_score = candidate.score

    return best_index