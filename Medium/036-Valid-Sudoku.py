# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# Algorithm:
# Check for dublicates in all rows, columns and 3x3 subgrids.
# These subgrids can have their own indexes (0, 1, 2).
# This conversion from original o-8 indexes in a 9x9 cell grid requires integer division: r//3, c//3


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        grids = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                curr_position_on_the_board = board[r][c]
                subgrid_index_conversion = (math.floor(r/3), math.floor(c/3))

                # Skip empty cells
                if curr_position_on_the_board == ".":
                    continue

                # Check for dublicates
                if (curr_position_on_the_board in rows[r] or 
                    curr_position_on_the_board in columns[c] or
                    curr_position_on_the_board in grids[subgrid_index_conversion]):
                    return False

                # Update rows, columns, grids
                rows[r].add(curr_position_on_the_board)
                columns[c].add(curr_position_on_the_board)
                grids[subgrid_index_conversion].add(curr_position_on_the_board)

        return True


