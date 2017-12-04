def F1_score(test_set, solution_set):
    tp, fp, fn = 0, 0, 0 # Ikke interessert i true negative

    if len(solution_set) == 0 and len(test_set) == 0:
        return 1


    for name in solution_set:
        if name in test_set:
            tp += 1.0
        else:
            for value in test_set:
                if value in name:
                    tp += 1
                elif name not in test_set:
                    fn += 1.0
                else:
                    if value not in solution_set:
                        fp += 1.0

    try:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)


        f1_score = 2 * (precision * recall) / (precision + recall)
    except ZeroDivisionError:
        return 0

    print tp, fp, fn
    return f1_score


# print F1_score(["ab", "c"], ["ab", "e"])
# print F1_score(["donald trump"], ["president donald trump"])
