class Solution:
    def reverseStack(self, st):
        if len(st) <= 1:
            return  # base case: nothing to reverse
        
        top = st.pop()            # hold the top element
        self.reverseStack(st)     # reverse the rest
        self.insertAtBottom(st, top)  # put it at the bottom
    
    def insertAtBottom(self, st, item):
        if len(st) == 0:
            st.append(item)       # stack is empty, just push
            return
        
        top = st.pop()            # temporarily remove top
        self.insertAtBottom(st, item)  # recurse to reach bottom
        st.append(top)            # put the removed element back
