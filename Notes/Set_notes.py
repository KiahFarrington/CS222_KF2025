'''
{} = for dictionaires & sets
[] = for list

set = un-ordered collection. the order you put it in != the order it will output
- also, no duplicates

list
- ordered list = you give a list of 1,2,3,4 then it will be 1,2,3,4
- duplicate elements
'''
def main():
    fruits = {"apple", "banana", "cherry"}
    print(fruits)
    fruits.add("orange") # adds bc unique
    print(fruits)
    fruits.add("banana") # doesnt add bc not unique
    print(fruits)
    miscellaneous = {"Alice", 50, True, "Bob", 100, 55.23, True} #mixed data type
    print(miscellaneous)
    for m in miscellaneous:
        print(m)

'''
More set notes:
- set = unordered collection
- no duplicates allowed
- mixed data types allowed
- create: 
- varName  = {"item1", "item2"}
- varName2 = set([1,2,3,4])

methods:
    .add(items) --> adds new elements
    .remove(item) --> removes 'item', error if not found
    .discard(item) --> no error if item doesn't exist 
    .pop() --> removes random element
    .clear() --> clears all elements   
    len(set) --> length of set 

'''     
# common for math function, some methods and use of sets:
def ab():
    A =     {1 ,2 ,3 ,4}
    B = set([3, 4, 5, 6])
    print(A.union(B)) # A & B == {1,2,3,4,5,6}
    print(A.intersection(B)) # Overlap = {3, 4}
    print(A.difference(B)) # A-B == {1,2} == unique in A compared to B
    print(B.difference(A)) # B-A == {5,6} == unique in B compared to A

main()
#ab()