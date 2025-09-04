'''
key, value pairs
midterm = {
        "Key": value, 
        "key" : value, 
        "key" : value, 
    } 
dic_name.values() --> values column
dic_name.keys() ---> keys column

dic_name["key"] --> give you value tied to it
dic_name["key"][2] --> go list, into list into -
dic_name.append(50) --> add at the end
dic_name.insert(1, 70) --> at _x_ index, insert _y_
'''

def main():
    midterm = {
        "Alice": 90, 
        "Bob" : 93, 
        "Carol" : 70, 
        "Dave" : 100, 
        "Eve" : 97
    }
    #print(midterm["Bob"])
    #print(midterm.values())
    #print(midterm.keys())
    #for m in midterm.values():
    #    print(m)
    print(len(midterm))
    for k, v in midterm.items():
        #print(k)
        #print(v)
        if k == "Carol":
            print("")
    
    exams = {
        "Alice" : [100, 75, 80],
        "Bob" : [50, 50, 10]
    }
    #print(len(exams))
    print(exams["Bob"][2])
    
main()