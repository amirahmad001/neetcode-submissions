class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check in row
        for i in range(len(board)):
            row_arr_i = board[i:i+1]
            #flattened_list = list(itertools.chain.from_iterable(row_arr_i))
            if self.isvalid(row_arr_i[0]) == False:
                return False


        #check in col
        for i in range(len(board)):
            col_arr_i = [r[i:i+1] for r in board]
            #flattened_list = list(itertools.chain.from_iterable(row_arr_i))
            col_arr_i_flat = [r[i] for r in board]
            #print(col_arr_i_flat)
            if self.isvalid(col_arr_i_flat) == False:
                return False

        #check in square (3*3)
        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                # sqare = [row[j:j+3] for row in board[i:i+3]]
                square = [
                    num
                    for row in board[i:i+3]
                    for num in row[j:j+3]
                    ]
                print("square=",square)
                if self.isvalid(square) == False:
                    return False
        return True



    def isvalid(self,arr:list[str]) -> bool:
        print(arr)
        temp_set = set()
        #print("tested")
        for i in arr:
            if i in temp_set:
                #print(i,temp_set)
                if i != '.':
                    return False
            else:
                temp_set.add(i)
        #print("done")
        return True
        



        