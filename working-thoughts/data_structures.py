class LinkedList:   

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    #kind of a hacky solution to printing, should make this recursive
    def __str__(self):
        string = ""
        pointer = self
        while pointer != None:
            inPointer = pointer.val
            while inPointer != None:
                string += ("-->" + str(inPointer.val))
                inPointer = inPointer.next
            string += "\n"
            pointer = pointer.next
        return string


ll1 = [5,7,8,30]
ll2 = [10,20]
ll3 = [19,22,50]
ll4 = [28,35,40,45]

allLL = [ll1, ll2, ll3, ll4]
builtLL = []
for LL in allLL:
    newLL = None
    for item in reversed(LL):
        newLL = LinkedList(item, newLL)
    builtLL.append(newLL)

fullLL = None
for LL in reversed(builtLL):
    fullLL = LinkedList(LL, fullLL)

print(fullLL)
