'''
1.) open() the file
2.) read/write - using methods like .read(), .readlines(), .write().
3.) close() the file

open(filename, mode) is how you access a file.
    Mode determines what you can do:
    'r' → read (file must exist)
    'w' → write (creates/overwrites)
    'a' → append (adds to end, creates if not exists)
    'r+' → read & write
open() returns a file object.

Think: If a file is huge, do I want to load it all at once or read it line by line?
##read all at once##
data = file.read()       # ONE giant string (whole file)
lines = file.readlines() # LIST of strings, one per line

##line by line##
'''

def main():    
    try: # .read()
        fileInput = open("notes/students_info_notes.txt", 'r')
        all_text = fileInput.read() #reads entire file into one giant string   
        print("---- .read() ----")          #000000001,Smith,Alice,Chemistry,3.92
        print(all_text)                     #000000002,Jones,Bob,Math,3.30
        print("---- .read() done ----\n")   #000000003,Pollard,Carol,Math,3.9
        fileInput.close()
        
        #readlines()
        print("---- .readlines() ----")                         # [
        fileInput = open("notes/students_info_notes.txt", 'r')  #   '000000001,Smith,Alice,Chemistry,3.92\n', 
        students = fileInput.readlines()                        #   '000000002,Jones,Bob,Math,3.30\n', 
        print(students)                                         #   '000000003,Pollard,Carol,Math,3.9'
        print("---- .readlines() done ----\n")                  # ]                                    
        fileInput.close()                            #  each line is put in'', and all of it is an array [] / list 
        
        studentList = {}
        for s in students:          #s = "000000001,Smith,Alice,Chemistry,3.92\n"
            parts = s.split(',')    # ['000000001', 'Smith', 'Alice', 'Chemistry', '3.92\n']
            print(parts) 
            studentList[parts[0]] = [parts[1], parts[2], parts[3], parts[4]] #key = ID, value = [last, first, major, gpa]
        
        print("\n---- studentList ----")   
        print(studentList)
        # {
        #  '000000001': ['Smith', 'Alice', 'Chemistry', '3.92'], 
        #  '000000002': ['Jones', 'Bob', 'Math', '3.30'], 
        #  '000000003': ['Pollard', 'Carol', 'Math', '3.9']
        # }
        print("---- studentList done----") 
        
        print("\n---- print values ----")                   
        for v in studentList.values(): # not the keys, just the values
            print(v)
        
        print("\n---- print keys ----")     
        for v in studentList.keys(): # just keys
            print(v)

        print("\n---- sorted for Math majors ----")
        for k, v in studentList.items():
            if v[2] == "Math":
                print(k + " " + v[0]+", "+v[1]) 
                
        writeFileNotes(studentList)
    
    except FileNotFoundError:
        print("File not found")


def writeFileNotes(studentList): 
    try:
        # Open a file for writing (creates or overwrites)
        fileOutput = open("notes/students_info_copy.txt", 'w')
        
        for k, v in studentList.items():
            # k is the ID, v is a list of [last, first, major, gpa]
            # Build a CSV-style line (comma-separated, ending with newline)
            line = f"{k},{v[0]},{v[1]},{v[2]},{v[3]}\n"

            # Actually write the string to the file
            fileOutput.write(line)

        # Always close when done to flush the buffer
        fileOutput.close()
        print("\nstudents_summary.txt has been written.")
    except OSError:
        print("Error writing to file")


main()