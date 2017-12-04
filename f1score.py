def F1_score(test_set, solution_set):
    tp, fp, tn, fn = 0, 0, 0, 0

    for name in solution_set:
        if name in test_set:
            tp += 1.0
        elif name not in test_set:
            fn += 1.0

    for name in test_set:
        if name not in solution_set:
            fp += 1.0

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)


    f1_score = 2 * (precision * recall) / (precision + recall)

    # print tp, fp, fn
    return f1_score


# print F1_score(["ab", "b", "c", "e", "f"], ["ab", "b", "d"])
