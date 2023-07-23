class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        row = len(image)
        col = len(image[0])
        
        
        
        for i in range(col):
            holder = []
            for j in range(row):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0
                holder.append(image[i][j])
            holder.reverse()
            image[i] = holder
        return image

        