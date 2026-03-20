class Solution:
    
    def insert(self, st, temp):
        
        # if the stack is empty or top element is less than temp, we can push
        if not st or st[-1] <= temp:
            st.append(temp)
            return
        
        # if the top elem is greater than temp, pop it.
        top = st.pop()
        
        # recursively inserting temp into the smaller stack.
        self.insert(st, temp)
        
        # put the removed element back on top
        st.append(top)
    
    def sortStack(self, st):
        
        # this function mainly removes the elements one by one using recursion.
        if st:
            # removing the top element
            temp = st.pop()
            
            # recursively returning the reminaing elems
            self.sortStack(st)
            
            # inserting the removed elems in the sorted position
            self.insert(st, temp)
            
        return st
