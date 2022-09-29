
import sys

def main():

    filenames = []

    if len(sys.argv) > 1:

      index = 0
      for arg in sys.argv:
        if index > 0:
            filenames.append( arg )
          
        index += 1


    print( "Imported command line files: ", end="" )
    print( filenames )

    if len(filenames) > 0:

      for filename in filenames:

        print( "Reading: ", end="" )
        print( filename )

        total = 0.0
        length = 0.0
        average = 0.0

        try:

            #Open the file
            infile = open(filename, 'r')

            contents = infile.read().strip().split()

            count_value = input('Enter a the value to count: ')

            count = 0

            for num in contents:
                amount = float(num)
                total += amount
                if num == count_value:
                  count += 1

            average = total / len(contents) # you can use the builtin len() method to get the length of contents instead of counting yourself

            print( "The Number of data points is: " )
            print( len(contents) )
            print( "The average is: " )
            print( average )
            print( "The number of times your item appears is : " )
            print( count )
            print( "The percentage of total your item in total is : " )
            print( count/len(contents) )

            #Close the file
            infile.close()

        except IOError:
            print('An error occurred trying to read the file.')

        except ValueError:
            print('Non-numeric data found in the file')

        except:
            print('An error has occurred')

    else:

        total = 0.0
        length = 0.0
        average = 0.0

        try:
            #Get the name of a file
            filename = input('Enter a file name: ')

            #Open the file
            infile = open(filename, 'r')

            contents = infile.read().strip().split()

            count_value = input('Enter a the value to count: ')

            count = 0

            for num in contents:
                amount = float(num)
                total += amount
                if num == count_value:
                  count += 1

            average = total / len(contents) # you can use the builtin len() method to get the length of contents instead of counting yourself

            print( "The Number of data points is: " )
            print( len(contents) )
            print( "The average is: " )
            print( average )
            print( "The number of times your item appears is : " )
            print( count )
            print( "The percentage of total your item in total is : " )
            print( count/len(contents) )

            #Close the file
            infile.close()

        except IOError:
            print('An error occurred trying to read the file.')

        except ValueError:
            print('Non-numeric data found in the file')

        except:
            print('An error has occurred')


main()