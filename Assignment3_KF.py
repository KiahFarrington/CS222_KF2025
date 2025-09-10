def main():
    keepLooping = False
    while not keepLooping:
        print("Choose an option:\n\t1) Search by Last Name\n\t2) Search by Major\n\t3) Quit")
        userInput = input("Pick: ")
        
        if(userInput == "1)"):
            lastNameSearch()           
        elif(userInput == "2)"):
            majorSearch()     
        elif(userInput == "3)"):
            keepLooping = True
            print("Goodbye!")
        else:
            print("Your input didn't match, enter 1), 2), or 3)\n")
            
            
def lastNameSearch():
    lastName = input("Last name you are looking for: ")
    students = openFileForUse() 
    studentList = convertToDictionary(students)
    
    print("All results matching", lastName) 
    for id,otherInfo in studentList.items():
        if lastName == otherInfo[0]:
            print(f"ID: {id} | Name: {otherInfo[0]:>10},{otherInfo[1]:>8} | Major: {otherInfo[2]:>10} | GPA: {otherInfo[3]}", end="")
            #trying print f, {} for variables, otherInfo = all info in dict, : means format, > means right alighn, num @ end tells width           


def majorSearch():
    major = input("Major you are looking for: ")
    students = openFileForUse()  
    studentDic = convertToDictionary(students)
    
    print("All results matching:", major) 
    for id,otherInfo in studentDic.items():
        if major == otherInfo[2]:
            print(f"ID: {id} | Name: {otherInfo[0]:>10},{otherInfo[1]:>8} | Major: {otherInfo[2]:>4} | GPA: {otherInfo[3]}", end="")
            #trying print f, {} for variables, otherInfo = all info in dict, : means format, > means right alighn, num @ end tells width
 
  
def convertToDictionary(students):
    studentDictionary = {}
    for s in students:
        parts = s.split(',')
        studentDictionary[parts[0]] = parts[1:]   
    return studentDictionary    


def openFileForUse():
   fileInput = open("Assignment3_Student_Info.txt", 'r')
   students = fileInput.readlines()
   fileInput.close()
   return students

main()