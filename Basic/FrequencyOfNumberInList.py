## take input from user for the no. elements that it will enter

ele_count = int(input("Please enter the no. of elements that you will be entering: "))

## take the elements as input and save it in a list
elements = [int(input(f"Enter {num}th element: ")) for num in range(ele_count)]

''' 
now that we have the list of elements, we will parse through the list and save the occurance count of each
element in a dictionary with the element being the key
'''
occ_count = {}
for ele in elements:
    if ele in occ_count.keys():
        occ_count[ele] += 1
    else:
        occ_count[ele] = 1

print(occ_count)
