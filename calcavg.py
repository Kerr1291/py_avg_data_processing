
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

    use_ouliers = input('Cull outliers? (Enter 0 or 1): ')

    outlier_min = 0.0
    outlier_max = 0.0

    if int(use_ouliers) != 0 :
    
      outlier_min = input('Enter bottom range of outlier: ')
      outlier_max = input('Enter upper range of outlier: ')
    

    if len(filenames) > 0:

      for filename in filenames:

        total = 0.0
        length = 0.0
        average = 0.0

        try:

            #Open the file
            infile = open(filename, 'r')

            contents = infile.read().strip().split()

            length = len(contents)

            for num in contents:
                            
                if int(use_ouliers) != 0 :
  
                  if float(num) < float(outlier_min):
                    length -= 1
                    continue

                  if float(num) > float(outlier_max):
                    length -= 1
                    continue

                amount = float(num)
                total += amount
                # more code here

            average = total / length # you can use the builtin len() method to get the length of contents instead of counting yourself

            print( "Total data points ", end="" )
            print( length, end="" )

            if int(use_ouliers) != 0 :
              print( " | Outliers Ignored = ", end="" )
              print( len(contents) - length, end="" )
            
            print( "  | Average of ", end="" )
            print( filename, end="" )
            print( " = ", end="" )
            print( average )

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

          length = len(contents)

          for num in contents:
                          
              if int(use_ouliers) != 0 :

                if float(num) < float(outlier_min):
                  length -= 1
                  continue

                if float(num) > float(outlier_max):
                  length -= 1
                  continue

              amount = float(num)
              total += amount
              # more code here

          average = total / length # you can use the builtin len() method to get the length of contents instead of counting yourself

          print( "Total data points ", end="" )
          print( length, end="" )

          if int(use_ouliers) != 0 :
            print( " | Outliers Ignored = ", end="" )
            print( len(contents) - length, end="" )
          
          print( "  | Average of ", end="" )
          print( filename, end="" )
          print( " = ", end="" )
          print( average )

          #Close the file
          infile.close()

      except IOError:
          print('An error occurred trying to read the file.')

      except ValueError:
          print('Non-numeric data found in the file')

      except:
          print('An error has occurred')


main()