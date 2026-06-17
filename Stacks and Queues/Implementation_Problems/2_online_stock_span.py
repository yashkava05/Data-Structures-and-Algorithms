class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # everyday contributes to a span of atleast one
        span = 1

        # pop all days with prices <= current
        while self.stack and self.stack[-1][0] <= price:
            # adding the span of the popped day into the current one
            span += self.stack[-1][-1]

            # removing the last day as it wont be an answer again
            self.stack.pop()

        # pushing the current price with its total accumulated stock
        self.stack.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
