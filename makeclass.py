
import sys
import pickle

def computeModeratedMarks(file1, file2):

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
            sList[0] = int(sList[0])
            sList[2] = int(sList[2])
        except IndexError:
            print("Undefined Index")
            sys.exit()
        except (ValueError, TypeError):
            print("Unsuccessful conversion to int")
            sys.exit()

        pickle.dump(sList, fOut)
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
    
    computeModeratedMarks(file1, file2)

    

if __name__=='__main__':
    main()
