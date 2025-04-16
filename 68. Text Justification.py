class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []
        line , length = [] , 0 
        i = 0

        while i < len(words) :


            #adding spaces when line is completed
            if length + len(line) + len(words[i]) > maxWidth : 

                extra_spaces = maxWidth - length
                spaces = extra_spaces // max(1,len(line) -1) 
                remainder = extra_spaces % max(1,len(line) -1)

                for j in range(max(1,len(line) -1)) :

                    line[j] += " "*spaces

                    if remainder : 
                        line[j] += " "
                        remainder -=1


                res.append("".join(line))
                line , length = [] , 0 

            #concatenating the words as long as we can make them fit
            line.append(words[i])
            length += len(words[i])
            i += 1 


        # handling the last line

        last_line = " ".join(line)
        end_spaces = maxWidth - len(last_line)
        res.append(last_line + " "*end_spaces)

        return res
