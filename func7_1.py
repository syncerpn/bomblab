# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:57:50 2023

@author: NghiaServer
"""

class Node:
    def __init__(self, v, l=0, r=0):
        self.v = v
        self.l = l
        self.r = r

n41 = Node(0x00000001,0,0)
n42 = Node(0x00000007,0,0)
n43 = Node(0x00000014,0,0)
n44 = Node(0x00000023,0,0)
n45 = Node(0x00000028,0,0)
n46 = Node(0x0000002f,0,0)
n47 = Node(0x00000063,0,0)
n48 = Node(0x000003e9,0,0)
n32 = Node(0x00000016,n43,n44)
n33 = Node(0x0000002d,n45,n46)
n31 = Node(0x00000006,n41,n42)
n34 = Node(0x0000006b,n47,n48)
n21 = Node(0x00000008,n31,n32)
n22 = Node(0x00000032,n33,n34)
n1  = Node(0x00000024,n21,n22)

def fun(di, si):
    if (di == 0):
        return -1, di, si
    dx = di.v
    
    if dx > si:
        di = di.l
        ax, di, si = fun(di, si)
        ax += ax
        return ax, di, si
    elif dx == si:
        return 0, di, si
    else:
        di = di.r
        ax, di, si = fun(di, si)
        ax = ax + ax + 1
        return ax, di, si

di = n1
for i in range(1001):
    ax, _, _ = fun(di, i)
    if ax == 2:
        print(i, ax)