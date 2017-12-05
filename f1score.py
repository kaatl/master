import re

def F1_score(solution_list, test_list):
    print "listene", solution_list, test_list
    tp, fp, fn = 0.0, 0.0, 0.0 # Ikke interessert i true negative

    if len(solution_list[0]) == 0 and len(test_list[0]) == 0:
        print 1.0
        return 1.0

    if len(solution_list[0]) > 0 and len(test_list[0]) == 0:
        print 0.0
        return 0.0

    for solution_value in solution_list:
        s_list = solution_value.split()

        if len(solution_value.replace("-", " ").split()) <= 2:
            match = [t for t in test_list if any(s in t for s in s_list)]

            if match:
                tp += 1.0
            else:
                fn += 1.0
        else:
            liste = solution_value.replace("-", " ").split()
            match_bool = False
            for i in range(len(liste) - 1):
                match_bool = False
                first = liste[i]
                second = liste[i + 1]

                bigram = first + " " + second
                print bigram

                match = any(bigram in t for t in test_list)

                if match:
                    match_bool = True

            if match_bool:
                tp += 1.0
            else:
                fn += 1.0

    for test_value in test_list:
        t_list = test_value.split()

        match = [s for s in solution_list if any(t in s for t in t_list)]
        match2 = [t for t in test_list if any(s in t for s in s_list)]

        if not match and not match2:
            fp += 1.0

    print tp, fp, fn

    try:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        print "score", 2 * (precision * recall) / (precision + recall)
        return (2 * (precision * recall) / (precision + recall))
    except ZeroDivisionError:
        return 0.0



# print F1_score(['sweden'], [''])
# print F1_score(["ab", "c", "f"], ["ab", "c", "e"])
# print F1_score(["president donald trump"], ["president"])
# print F1_score(['moroccan', 'german', 'north rhine-westphalia', 'united states'], ['moroccan', 'german', 'north', 'united states'])
# print F1_score(["president donald trump"], ["president"])
# print F1_score(["president donald trump"], ["donald trump"])
# print F1_score(['president chen shui-bian', 'taipei', 'china'], ['taiwan', 'chen shui-bian', 'taipei', 'china'])
