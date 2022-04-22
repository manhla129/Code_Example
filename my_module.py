#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ngto(a):
    '''kiểm tra số nguyên tố'''
    flag = True
    for i in range(2,a//2+1):
        if a%i==0:
            flag = False
            break
    return flag

def isSimple(num):
    '''kiểm tra số nguyên tố'''
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True

def giaithua(number):
    '''Hàm tính giai thừa của 1 số tự nhiên'''
    if number == 0:
        return 1
    else:
        gt = 1
        for i in range(1, number+1):
            gt *= i
        return gt

def max_min(a, b, c=10):
    '''Tìm max, min của 3 số, số thứ 3 mặc định là 10'''
    max = a if a>b and a>c else b if b>c else c
    min = a if a<b and a<c else b if b<c else c
    return max, min

