class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_numbers = {}
        box_1 = {}
        box_2 = {}
        box_3 = {}
        column_1 = {}
        column_2 = {}
        column_3 = {}
        column_4 = {}
        column_5 = {}
        column_6 = {}
        column_7 = {}
        column_8 = {}
        column_9 = {}


        for ir, row in enumerate(board):
            for ii, item in enumerate(row):
                if item == ".":
                    continue
                
                # for row
                if item in row_numbers:
                    return False
                row_numbers[item] = item

                # for column
                if ii == 0:
                    if item in column_1 or item in box_1:
                        return False
                    column_1[item] = item
                    box_1[item] = item
                elif ii == 1:
                    if item in column_2 or item in box_1:
                        return False
                    column_2[item] = item
                    box_1[item] = item
                elif ii == 2:
                    if item in column_3 or item in box_1:
                        return False
                    column_3[item] = item
                    box_1[item] = item

                elif ii == 3:
                    if item in column_4 or item in box_2:
                        return False
                    column_4[item] = item
                    box_2[item] = item
                elif ii == 4:
                    if item in column_5 or item in box_2:
                        return False
                    column_5[item] = item
                    box_2[item] = item
                elif ii == 5:
                    if item in column_6 or item in box_2:
                        return False
                    column_6[item] = item
                    box_2[item] = item

                elif ii == 6:
                    if item in column_7 or item in box_3:
                        return False
                    column_7[item] = item
                    box_3[item] = item
                elif ii == 7:
                    if item in column_8 or item in box_3:
                        return False
                    column_8[item] = item
                    box_3[item] = item
                elif ii == 8:
                    if item in column_9 or item in box_3:
                        return False
                    column_9[item] = item
                    box_3[item] = item

            # reset blocks
            if ir == 2 or ir == 5:
                box_1 = {}
                box_2 = {}
                box_3 = {}

            # reset row
            row_numbers = {}
            
        

        return True

        # row check
        # 