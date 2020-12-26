''' This is a code for Todo Command-Line Utility. It helps you manage your daily task and work'''
import sys
import argparse
import datetime

#this function place the text in todo.txt in proper manner
def copytoorg():   
    infile = "todo.txt"
    outfile = "copy.txt"

    delete_list = ["1", "2", "3", "4","5","6","7","8","9","10"]
    fin = open(infile,"r+")
    fout = open(outfile, "w+")
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
        fout.write(line)
    fin.truncate(0)
    fin.close()
    fout.close()
    
    with open("copy.txt","r+") as f:
        with open("todo.txt", "w") as f1:
            for line in f:
                f1.write(line)
        f.truncate(0)

#this is help utility
def help1():
    print("Usage :-\n")
    print('$ ./todo add "todo item"' + "  " + "# ADD a New todo\n" )
    print('$ ./todo ls' + "               " + "# Show remaining todos\n" )
    print('$ ./todo delete NUMBER' + "    " + "# Delete a todo\n" )
    print('$ ./todo done NUMBER' + "      " + "# Complete a todo\n" )
    print('$ ./todo help' + "             " + "# Show usage\n" )
    print('$ ./todo report' + "           " + "# Statistics\n" )
    return("type help for more information")


#this function add the todo in the list
def addtodo(args):
    try:
        print("ADDED : "+ args.add)
        args = sys.argv[2]
        fp = open("todo.txt", "a")
        fp.write(args)
        fp.write('\n')
        return("Added Successfully")
        fp.close()
    except Exception as e:
        print("expected one more argument")
        print("type 'help' for more information")
    
   

#This function list the todo on command line
def showtodo(args):
    try:
        fp = open("todo.txt", "r+")
        count = 1
        while True:
            content = fp.readline()
            if content == "":
                break
            else:
                print(count,":",content)
                count += 1
        return("All todo listed above need to be completed")
    except Exception as e:
        print("expected one more argument")
        print("type 'help' for more information")



   
# This fuction transfer the completd todo to done.txt
def donetodo(args):
    args = sys.argv[2]
    f3 = open("todo.txt","r")
    count = 0
    lines = f3.readlines()
    for line in lines :
        count = count + 1

    num = int(args)
    if(count < num):
        print("Error: todo task " + args + " does not exist")
    f3.close()
    with open('todo.txt', 'r') as program:
        data = program.readlines()

    with open('todo.txt', 'w') as program:
        for(number, line) in enumerate(data):
            program.write('%d  %s' % (number + 1, line))
    
    file1 = open('todo.txt', 'r+')
    file2 = open('done.txt', 'a')
    d = datetime.datetime.now() 
    for line in file1.readlines(): 
        if(line.startswith(args)): 
            file2.write('todo completed at %s.\n' %(d))
            file2.write(line)
            file2.write('\n')
            print("todo completed: "+line) 
   
    f = open("todo.txt", "r+")
    f1 = open("todo.txt", "r+")
    while True:
        line = f.readline().lower()
        f.truncate(0)
        if line == "":
            break
        if args not in line:
            f1.write(line)
    f.close()
    return("type help for more information and usage")
 
                
    
#this fumction shows help
def showhelp(args):
    #print(args.help)
    print("Usage :-\n")
    print('$ ./todo add "todo item"' + "  " + "# ADD a New todo\n" )
    print('$ ./todo ls' + "               " + "# Show remaining todos\n" )
    print('$ ./todo delete NUMBER' + "    " + "# Delete a todo\n" )
    print('$ ./todo done NUMBER' + "      " + "# Complete a todo\n" )
    print('$ ./todo help' + "             " + "# Show usage\n" )
    print('$ ./todo report' + "           " + "# Statistics\n" )
    return("type help for more information")

#this function show report 
def showreport(args):
    f1 = open("todo.txt", "r")
    count = 0
    lines = f1.read().lower()
    List1 = lines.split("\n") 
    for j in List1: 
        if j: 
            count = count + 1
    f2 = open("done.txt", "w+")
    countt = 0
    lineess = f2.read().lower()
    List2 = lineess.split("\n") 
    for i in List2: 
        if i: 
            countt = countt + 1
    d = datetime.datetime.now()
    print(d)
    print("Pending :", count) 
    print("Completed :", countt)
    return("todo statistics")

#This function deletes the todo
def deletetodo(args):
    args = sys.argv[2]
    f3 = open("todo.txt","r")
    count = 0
    lines = f3.readlines()
    for line in lines :
        count = count + 1
    num = int(args)
    if count < num:
        print("Error: todo task " + args + " does not exist")
    else:
        print("todo :" +args)
        print("Successfully Deleted")
    f3.close()
    with open('todo.txt', 'r') as program:
         data = program.readlines()
    with open('todo.txt', 'r+') as program:
        for (number, line) in enumerate(data):
            program.write('%d  %s' % (number + 1, line))
    f = open("todo.txt", "r+")
    f1 = open("todo.txt", "r+")
    while True:
        line = f.readline()
        f.truncate(0)
        if line == "":
            break
        if args not in line:
            f1.write(line)
    f.close()
    return("type help for more information")
   
    


      




    
#this is a 'add' argument
def add():
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', default="add", action='store',help = "Add a new todo" )

    args = parser.parse_args()
    sys.stdout.write(str(addtodo(args)))
    #print(args.add)
#This is 'ls' argument
def lists():
    parser = argparse.ArgumentParser()
    parser.add_argument('ls', default="ls", help = "Show remaining todos" )

    args = parser.parse_args()
    sys.stdout.write(str(showtodo(args)))
    #print(args.add)
#This is '--del' argument
def delete():
    parser = argparse.ArgumentParser()
    parser.add_argument('--del', default="--del", help = "Delete a todo" )
   
    args = parser.parse_args()
    sys.stdout.write(str(deletetodo(args)))
    #print(args.add)
#This is 'report' argument
def report():
    parser = argparse.ArgumentParser()
    parser.add_argument('report', default="report",  action='store',help = "Statistics" )

    args = parser.parse_args()
    sys.stdout.write(str(showreport(args)))
    #print(args.add)

#This is 'help' argument
def help():
    parser = argparse.ArgumentParser()
    parser.add_argument('help', default="help", action='store',help = "Show help" )

    args = parser.parse_args()
    sys.stdout.write(str(showhelp(args)))
    #print(args.add)
#This is '--done' argument
def done():
    parser = argparse.ArgumentParser()
    parser.add_argument('--done', default="--done",  action='store',help = "Complete a todo" )

    args = parser.parse_args()
    sys.stdout.write(str(donetodo(args)))
    #print(args.add)






#Driver code/main function
if __name__ == "__main__":
    try:
        if sys.argv[1] == "--add":
            add()
        if sys.argv[1] == "ls":
            lists()
        if sys.argv[1] == "--del":
            delete()
            copytoorg()
        if sys.argv[1] == "--done":
            done()
            copytoorg()
        if sys.argv[1] == "report":
            report()
        if sys.argv[1] == "help":
            help()
    except Exception as e:
        help1()
        print("type 'help' for more information")

    

   