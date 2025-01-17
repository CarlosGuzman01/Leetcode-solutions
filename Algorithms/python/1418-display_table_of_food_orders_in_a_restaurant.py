class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foodItems = set()

        tableMap =  {}

        for arr in orders:
            name, table, food = arr
            table = int(table)

            foodItems.add(food)

            if table in tableMap:
                if food in tableMap[table]:
                    value = int(tableMap[table][food])
                    value += 1
                    tableMap[table][food] = str(value)
                else:
                    tableMap[table][food] = "1"
            
            else:
                newMap = {}
                newMap[food] = "1" 
                tableMap[table] = newMap
        
        food = sorted(foodItems)
        food.insert(0, "Table")
        

        answer = []
        answer.append(food)

        
        map2 = dict(sorted(tableMap.items()))

        for table in map2:
            arr = [str(table)]
            for i in range(1, len(food)):
                if food[i] in map2[table]:
                    arr.append(map2[table][food[i]])
                else:
                    arr.append("0")
            answer.append(arr)
                
        return answer




              

        
