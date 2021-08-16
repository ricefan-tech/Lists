#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:27:24 2021

@author: rui
"""

class LinkedList:
    
    class ListNode:
        
        def __init__(self, value):
            self.value=value
            self.next=None
            
    def __init__(self):
        self.head=None
        
    def __append__(self, newNode):
        if self.head==None:
            self.head=newNode
        else:
            tmp=self.head
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=newNode
            
    def __prepend__(self, newNode):
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        
    def __delete__(self, node):
        if self.head is node:
            self.head=self.head.next
        else:
            tmp=self.head
            while tmp.next is not node:
                tmp=tmp.next
            tmp.next=tmp.next.next