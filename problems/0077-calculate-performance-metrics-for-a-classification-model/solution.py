
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    # Implement your code here
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for a, p in zip(actual, predicted):
        if a == 1 and p == 1:
            TP += 1
        elif a == 0 and p == 0:
            TN += 1
        elif a == 0 and p == 1:
            FP += 1
        elif a == 1 and p == 0:
            FN += 1
    confusion_matrix = [[TP, FN], [FP, TN]]
    accuracy = (TP+TN) / (TP+TN+FP+FN)
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    f1 = 2 * precision*recall/(precision+recall)
    specificity = TN/(TN+FP)
    negativePredictive = TN/(TN+FN)
    return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
