import urllib.request
def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):

    def countingsort(lst, i):
        # buckets: where character counts are stored
        buckets = [0] * 256
        # counter: stores intermediate answers
        inter = [""] * len(lst)
        # Starts at last character and goes to first
        for x in lst:
            # counts number of each char
            buckets[x[i]] +=1
        # adds previous val to each bucket
        for j in range(256):
            buckets[j] += buckets[j - 1]
        # adds character to output array
        for k in range(len(lst)-1,-1,-1):
            inter[buckets[lst[k][i]]-1] = lst[k]
            buckets[lst[k][i]] -= 1
        return inter

    if type(book_url) is str:
      file = urllib.request.urlopen(book_url).read().decode()
      mylist = file.split()
    if type(book_url) is list:
      mylist = book_url

    #finds longest character
    longest = len(mylist[0])
    for i in mylist:
        if len(i) > longest:
            longest = len(i)

    # pads strings with space
    for i in range(0, len(mylist)):
        if len(mylist[i]) < longest:
            mylist[i] = mylist[i] + "\0" * (longest - len(mylist[i]))

    #turns each string to byte
    for i in range(len(mylist)):
        mylist[i] = mylist[i].encode('ascii', 'replace')

    #radix sort using counting sort
    listToSort = mylist
    for i in range(longest-1, -1, -1):
        listToSort = countingsort(listToSort, i)
    for i in range(len(mylist)):
        listToSort[i] = listToSort[i].decode("ASCII").strip("\0")
    return listToSort
