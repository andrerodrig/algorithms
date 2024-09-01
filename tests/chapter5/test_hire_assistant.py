from algorithms.chapter5.hire_assistant import hire_assistant, Candidate


def test_hire_assistant():
    candidates = [
        Candidate(),
        Candidate(),
        Candidate(),
        Candidate(),
        Candidate(),
        Candidate(),
        Candidate(),
        Candidate(),
        Candidate(),
    ]
    hired_index = hire_assistant(candidates=candidates)

    max_candidate_score = max([candidate.score for candidate in candidates])
    expected_index = next(
        i for i, cand in enumerate(candidates) if cand.score == max_candidate_score
    )
    print(hired_index)

    assert hired_index == expected_index