# coding: utf-8
def bubb(list_to_sort, reverse=False):
    done = False
    l = list_to_sort.copy()
    while not done:
        done = True
        for k in range(len(l) - 1):
            if l[k] > l[k + 1]:
                l[k], l[k + 1] = l[k + 1], l[k]
                done = False
                print("Not done")
    return l
