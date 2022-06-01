class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        arr = sentence.split(" ")
        for i in range(len(arr)):
            a = arr[i]
            if a[0] == "$" and a[1:].isnumeric():
                val = int(a[1:])
                p = val - (val * discount /100)
                print(arr[i] , p)
                arr[i] = "${:.2f}".format(p)
        return " ".join(arr)