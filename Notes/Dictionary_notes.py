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


def midterm_example():
    print("\n\nmidterm example:")
    midterm = {
        "Alice": 90, 
        "Bob" : 93, 
        "Carol" : 70, 
        "Dave" : 100, 
        "Eve" : 97
    }
    print(midterm["Bob"])         # prints 93
    print( midterm.values())      #allll values = gives you dict_values([90, 93, 70, 100, 97])
    print(type(midterm.values())) # <class 'dict_values'> - its a iterable, & dynamic ... group
    for v in midterm.values():
        print(v) 
    
    #keys
    print(midterm.keys())         #alll keys = dict_keys(['Alice', 'Bob', 'Carol', 'Dave', 'Eve'])
    for k in midterm.keys():
        print(k)
    
    for k in midterm:        # keys / same as above loop
        print(k)
    
    ################################################################################################################
    print(midterm.items())      #dict_items([('Alice', 90), ('Bob', 93), ('Carol', 70), ('Dave', 100), ('Eve', 97)])
                                #gives you each entry as a tuple, ('key', value)
                                
    for key, value in midterm.items(): #key becomes "Alice", "Bob", "Carol" ... etc
        print(key, "→", value)         #values becomes 90 , 93, 70 ... etc 
    ###You dont have to use items###
    for k in midterm:
        print("key:", k, "- value:", midterm[k])
        # so, Loop over midterm dict → same as midterm.keys()
                                                  
    print(len(midterm)) # len = 5 : counts how many keys exist in the dictionary
    
    
def mid_dictionaries():
    print("\n\nmid level dictionary examples:")
    grades = {
    "Alice": [90, 85, 92],
    "Bob":   [78, 81, 74],
    "Harry": [56 ,42, 90, 70]
    }
    
    print(grades["Alice"]) # output: [90, 85, 92]
    print(grades["Alice"][1]) # looks at key "alice" : in [90, 85, 92]
                              # goes to index 1, retrieves: 85
    
    #student & their list  
    for name, scores in grades.items(): # loops through all students & their list
        print(name, "scores:", scores)
    
    #looping through each indivdual score
    for name, scores in grades.items(): # name key, then scores = [90, 85, 92] (list)
        for s in scores:                # s = each item in [90, 85, 92] (list)
            print(name, "got", s)



def complex_dictionaries(): 
    print("\n\nHIGH level dictionary examples:")
    school = { #Outer dictionary → students
        "Alice": { #Inner dictionary
            "age": 20,
            "major": "Math",
            "grades": [90, 85, 92]
        },
        "Bob": { #Inner dictionary
            "age": 21,
            "major": "CS",
            "grades": [78, 81, 74]
        },
        "Harry": { #Inner dictionary → each students details
            "age" : 19,
            "major": "Art",
            "grades": [90, 92, 78] # grades inside each student → a list of numbers
        }
    }
    
    #layering
    print(school["Alice"]) #returns inner dictionary
    print(school["Alice"]["major"]) # Outer key → inner key
    print(school["Bob"]["grades"][0]) #Dict → dict → list index
    
    for name, info in school.items():
        print("\n---", name, "---")

        for field, value in info.items():
            print(field, ":", value)
       
    #diging into grades, inside inner dict     
    for name, info in school.items():
        print(name, "grades:")
        
        for grades in info["grades"]: #info dict, each students, look @ grade key to loop through
            print("  ", grades) # will loop through all of "Alice" grades, under "grade" key

#midterm_example()
mid_dictionaries()    
complex_dictionaries()
#https://www.youtube.com/watch?v=LlIqrWJaBcQ 