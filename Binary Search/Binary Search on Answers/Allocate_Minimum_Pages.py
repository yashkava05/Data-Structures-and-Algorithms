# https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        
        # if there are more students than books, not possible to give one book to each student.
        if k > n:
            return -1
            
        low = max(arr)
        high = sum(arr) # if all pages are given to a single student.
        
        result = high # var to store our final answer
        
        while low <= high:
            
            mid = (low + high) // 2
            
            # checking if it's possible to allocate all books to k students
            # such that no student reads more than mid number of pages.
            if self.is_feasible(arr, k, mid):
                
                result = mid # saving the mid as an answer if it works
                
                # going to the left to find a potential smaller answer
                high = mid - 1
            else:
                # mid is too small, very less pages per student and so students exceed k
                low = mid + 1
            
        return result
        
    # performing a feasibility check to see if we can allocate all books 
    # to k students such that no student reads more than mid number of pages.
    def is_feasible(self, arr, k, max_pages):
        # starting with the first student
        students = 1
        
        # running sum of pages for the curr student.
        current_sum = 0
        
        # going through each book from left to right.
        for pages in arr:
            if current_sum + pages > max_pages:
                # current student is greater than mid, so assigning it to the next student.
                students += 1
                current_sum = pages
                
                # if number of students exceeds given number k
                if students > k:
                    return False
            
            else:
                current_sum += pages
            # current student can take this book
                
        
        return True # if managed with <= k students, it's feasible.
        
        
        
