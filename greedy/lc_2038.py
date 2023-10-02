class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0

        # Iterate through the colors, excluding the edge pieces
        for i in range(1, len(colors) - 1):
            current = colors[i]
            prev = colors[i - 1]
            next_color = colors[i + 1]

            # Check if Alice can make a move here
            if current == 'A' and prev == 'A' and next_color == 'A':
                alice += 1  # Alice can remove 'A'

            # Check if Bob can make a move here
            elif current == 'B' and prev == 'B' and next_color == 'B':
                bob += 1  # Bob can remove 'B'

        # Determine the winner based on the scores
        return alice > bob
            
