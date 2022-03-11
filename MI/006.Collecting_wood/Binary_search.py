class solution:
    def wood_collected(self, tree, n, h):
        ret = 0
        for i in range(n):
            if tree[i] > h:
                ret += tree[i] - h
        return ret

    def find_height(self, tree, n, k):
        l = 0       #lower limit
        h = 0       #upper limit
        for i in range(n):
            h = max(h,tree[i])
        while(l<=h):
            mid = (l+h)//2
            val = self.wood_collected(tree, n, mid)
            if val == k:
                return mid
            elif val > k:
                l = mid + 1
            else:
                h = mid - 1
        return -1

n = int(input("Enter number of Trees"))
k =int(input("Enter the height at which tree needs to be cut down"))
print("Height of each Tree")
arr = []
for i in range(0,n):
    a = int(input(""))
    arr.append(a)
count = self.find_height( arr, n, k)
print(f"Wood collected by cutting trees are {count}")




