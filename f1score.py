def F1_score(test_list, solution_list):
    tp, fp, fn = 0, 0, 0 # Ikke interessert i true negative

    if len(solution_list) == 0 and len(test_list) == 0:
        return 1

    for solution_value in solution_list:
        s_list = solution_value.split()

        match = [t for t in test_list if any(s in t for s in s_list)]

        if match:
            tp += 1.0
        else:
            fn += 1.0

    for test_value in test_list:
        t_list = test_value.split()

        match = [s for s in solution_list if any(t in s for t in t_list)]

        if not match:
            fp += 1.0

    try:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)

        # print tp, fp, fn
        return (2 * (precision * recall) / (precision + recall))
    except ZeroDivisionError:
        return 0


# print F1_score(["ab", "c", "f"], ["ab", "c", "e"])
# print F1_score(["donald trump"], ["president donald trump"])
# print F1_score(["president donald trump"], ["donald trump"])
