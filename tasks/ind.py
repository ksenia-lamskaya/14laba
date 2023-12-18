#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun1(type='max'):
    def fun2(list):
        if type == 'max':
            return max(list)
        else:
            return min(list)
    return fun2

if __name__ == "__main__":
    num = [1, 2, 5, 7, 3, 0]
    test_max = fun1()
    result = test_max(num)
    print("Результат выполнения программы: ", result)