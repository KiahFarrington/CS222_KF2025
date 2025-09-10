'''

blah blah blah
'''

def main():
    try:
        studentList = {}
        fileInput = open("studentsInfo.txt", 'r')
        students = fileInput.readlines()
        fileInput.close()
        for s in students:
            parts = s.split(',')
            studentList[parts[0]] = [parts[1], parts[2], parts[3], parts[4]]
        #for v in studentList.values():
        #    print(v)
        for k, v in studentList.items():
            if v[2] == "Math":
                print(k + " " + v[0]+", "+v[1]) 
    except FileNotFoundError:
        print("File not found")

main()