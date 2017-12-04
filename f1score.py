def F1_score(test_set, solution_set):
    tp, fp, fn = 0, 0, 0 # Ikke interessert i true negative

    if len(solution_set) == 0 and len(test_set) == 0:
        return 1


    for name in solution_set:
        if name in test_set:
            tp += 1.0
        elif name not in test_set:
            fn += 1.0

    for name in test_set:
        if name not in solution_set:
            fp += 1.0

    try:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)


        f1_score = 2 * (precision * recall) / (precision + recall)
    except ZeroDivisionError:
        return 0

    return f1_score


print F1_score(["c", "e", "f"], ["ab", "b", "d"])
