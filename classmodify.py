import sys
import pickle

def computeModeratedMarks(file1, file2, addPercent):
    '''
    Objective: To compute moderated marks of students
    Input Parameters: file1, file2: file names - string values
    addPercent – numeric value
    Return Value: None
    Final outcome: A new file – file2 of moderated marks is produced
    '''
    try:
        fIn = open(file1, 'r')
        fOut = open(file2,'wb')
    except IOError:
        print("Problem in opening the file")
        sys.exit() 
    line = fIn.readline()
    while(line != ''):
        sList = line.split(',')
        try:
            rollNo = int(sList[0])
            name = sList[1]
            marks = int(sList[2])
        except IndexError:
            print("Undefined Index")
            sys.exit()
        except (ValueError, TypeError):
            print("Unsuccessful conversion to int")
            sys.exit()
        maxMarks= 100
        moderatedMarks = int(marks) + ((addPercent * maxMarks)/100)
        if moderatedMarks > 100:
            moderatedMarks = 100

        lst = [rollNo, name, moderatedMarks]
        pickle.dump(lst, fOut)
        line = fIn.readline() 
    fIn.close()
    fOut.close()
    fOut = open(file2, 'rb')
    while True:
        try:
            print(pickle.load(fOut))
        except EOFError:
            break

def main():
    '''
    Objective: To compute moderated marks based on user input
    Input Parameter: None
    Return Value: None
    '''
    import sys
    sys.path.append("/home/administrator")
    file1 = input('Enter name of file containing marks:')
    file2 = input('Enter output file for moderated marks:')
    addPercent = int(input('Enter moderation percentage:'))
    computeModeratedMarks(file1, file2, addPercent)
    
if __name__=='__main__':
    main()
