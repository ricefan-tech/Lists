#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:27:24 2021

@author: rui
"""

from collections import deque

class LinkedList:
    
    
    
    class ListNode:
        
        def __init__(self, value):
            self.value=value
            self.next=None 
            self.length=0

    
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
        self.length+=1
        
    def __prepend__(self, newNode):
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        LinkedList.length+=1
        
    def __delete__(self, node):
        if self.head is node:
            self.head=self.head.next
        else:
            tmp=self.head
            while tmp.next is not node:
                tmp=tmp.next
                if tmp.next==None:
                    print("Node not in linked list")
                    return
            tmp.next=tmp.next.next
            self.length-=1
            
    def __iter__(self):
        self.counter=self.head
        return self
    
    def __next__(self):
        if self.counter==None:
            raise StopIteration
        else:
            curr_val=self.counter.value
            self.counter=self.counter.next
        return curr_val
    
    def removeDups(self):
        '''remove duplicate nodes in linked list'''
        
        if self.head is not None:
            s={self.head}
            tmp=self.head
            while tmp.next is not None:
                if tmp.next not in s:
                    s.add(tmp.next)
                else:
                    tmp.next=tmp.next.next
                    self.length-=1
                    
    def return_k_last(self,k):
        '''returns k last element in linked list'''
        
        steps=self.length-k
        tmp=self.head
        for i in range(steps):
            tmp=tmp.next
        return tmp
    
    
    def check_loop(self):
        '''checks whether lopo exists and returns node of lopo beginning  if so'''
            
        slow=self.head
        fast=self.head
        while(slow!=None and fast !=None):
            slow=slow.next
            fast=fast.next.next
            if slow is fast:
                break
        if slow==None or fast==None:
            return None
        slow=self.head
    
        while fast is not slow:
            slow=slow.next
            fast=fast.next
            
        return fast
            
    def check_palin(self):
        '''check whether linkedlist is a palindrome'''
        
        stack=deque()
        slow= self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            stack.append(slow)
            slow=slow.next
            fast=fast.next.next
        
        if fast == None:
            #meaning list has even length
            stack.append(slow)
            
        while slow!=None:
            ele=stack.pop()
            if ele.vaue!=slow.value:
                return False
            slow=slow.next
        
        return True
            
    def check_palin_rec(self):
        '''check whether linkedlist is a palindrome recursively'''
        
        _,res= self.compare_palin(self.head, self.length)
        return res
    
    def compare_palin(self, head,length):
        '''recursive helper function'''
        
        if length==0:
            return head, True 
        if length==1:
            return head.next, True

        res=self.compare_palin(head.next, length-2)
        comparenode=res[0]
        if not res[1]:
            return None, False
        
        return res[0].next, res[0].value==head.value
        
    
    
    
    
    
    
    
    
    
    
    