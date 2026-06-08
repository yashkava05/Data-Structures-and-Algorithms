class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # looping though the asteroids to perform collisions
        for ast in asteroids:
            # for collision, if the current asteroid is negative(left) and the top is positive(right), then there's a collision
            while stack and ast < 0 and stack[-1] > 0:
                # taking the diff of both the elements
                diff = ast + stack[-1]

                if diff < 0:
                    # current asteroid is bigger, so pop the stack top
                    stack.pop()
                elif diff > 0:
                    # stack top is bigger, destroy the current asteroid
                    ast = 0
                else:
                    ast = 0
                    stack.pop()

            if ast:
                stack.append(ast)

        return stack
