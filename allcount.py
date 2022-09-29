from array import *
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

    count_array = []

    data_set = set()

    item_count = 0

    done = 0

    #read in all filenames
    while done == 0:

      try:
          #Get the name of a file
          filename = input('Enter a file name (or 0 to finish, count, process, and display results): ')

          if filename == "0":
            done = 1
            break
          else:
            filenames.append( filename )

      except Exception as e:
          print( "Loop exited becuase:", end="" )
          print( type(e) , end="" )
          print( "at " + line )
          done = 1

    #read each one
    for filename in filenames:

      try:

          #Open the file and read in the unique data, update the total count
          infile = open(filename, 'r')

          contents = infile.read().strip().split()

          #Close the file
          infile.close()

          data_set.update( contents )

          item_count += len(contents)

          print( "Reading in: ", end="" )
          print( filename )

          print( "The number of data points is now: ", end="" )
          print( item_count )

      except IOError:
          print('An error occurred trying to read the file: ', end="" ) 
          print( filename )
          exit()

      except ValueError:
          print('Non-numeric data found in the file')
          exit()

      except Exception as e:
          print( "Read loop exited becuase:", end="" )
          print( type(e) , end="" )
          print( "at " + line )
          exit()

      except:
          print('An error has occurred')
          exit()


    sorted_set = sorted( map(int,data_set) )

    for elem in sorted_set:
      count_array.append( 0 )

    print( "Total Unique Items: ", end="" )
    print( len(sorted_set) )

    print( "Total Items: ", end="" )
    print( item_count )

    average = 0.0

    #process each one
    for filename in filenames:

      total = 0.0

      try:

          infile = open(filename, 'r')

          contents = infile.read().strip().split()

          #Close the file
          infile.close()

          print( "Processing : ", end="" )
          print( filename )

          print( "Counting items" )
          tracking = 0
          one_tenth = int( len(contents) / 10 )

          #begin counting items
          for item in contents:
    
            #value = int(item)
  
            #begin index lookup
            index = sorted_set.index( int(item) )

            new_count = (count_array[index]+1)
            count_array[index] = new_count
        
            total += int(item)

            #for elem in sorted_set:

            #  if value == int(elem):
            #    new_count = (count_array[index]+1)
            #    count_array[index] = new_count
            #    break
            #  index+=1
            #end index looup

            tracking += 1
            if tracking % one_tenth == 0:
              print( 100 * tracking/len(contents), end="" )
              print( " precent completed..." )
          #end counting items

      except Exception as e:
          print( "Process loop exited becuase:", end="" )
          print( type(e) , end="" )
          print( "at " + line )
          exit()

      average += (total / len(contents)) / len(filenames)

    print( "Average of all: ", end="" )
    print( average )

    print( "Total Unique Items: ", end="" )
    print( len(sorted_set) )

    print( "Total Items: ", end="" )
    print( item_count )

    #print the counted data
    index = 0
    for elem in sorted_set:

      elem_count = count_array[index]

      print( "[", end="" )
      print( index, end="" )
      print( "] Value( ", end="" )
      print( elem, end="" )
      print( " ) || Count( ", end="" )
      print( elem_count, end="" )
      print( " ) || Average =  ", end="" )
      print( elem_count/item_count )

      index+=1

main()