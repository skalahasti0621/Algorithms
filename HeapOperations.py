from heapq import heappush, heappop, heapify


class MinHeap:
    def __init__(self):
        self.heap=[]

    # parent value (i-1)/2
    def parent(self,i):
        return (i-1)/2

    #insert a new key K
    def insertKey(self,k):
        heappush(self.heap,k)
    
    # Decrease the value of key at index i to new_val
    # It is assumed that new_val is smaller than heap(i)
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while(i!=0 and self.heap[self.parent(i)]> self.heap[i]):
            #swap heap[i] with heap[parent[i]]
            self.heap[i], self.heap[self.parent(i)]=(
                self.heap[self.parent(i)],self.heap[i])
            

    

    def getMinimum(self):
        return self.heap[0]

    def extractMin(self):
        return heappop(self.heap)
    


    