with open('about_me.txt','r') as f:
    # print(f.read())  # The full script is printed to what was appeded earlier.
    # print(f.read(50))
    # print(f.read(50))  # print functions when ask for 50 gives me the first 50 values adding a print similar to 50 give me the next 50
   # print(f.readline(100)) # give me the first line but no matter the value i submits i stay on that line
   # for i in range(1,5):
      #print(f.readline())
      # print(f.readlines(1)) # i get full line information for 1
      # print(f.readlines(1)) # goes to the next line prints out
      # print(f.readlines(10))# goes to third line and prints
      # print(f.readlines(10)) # now with commenting out the first two prints it takes me back to the first 2 lines and rprints
      # print(f.readlines(100)) # so with this give me 3rd line but goes to next one
      # print(f.readlines(-1)) # IT READS EVERYTHING,BASICALLY RETURN REMAINING LINES.
      A = f.read(50)

      lines_list = []
      for i in range(1,5):
        lines_list.append(f.readline())


      C = print(f.readlines(100))

      print(f'First 50 characters {A}')
      print(f'Next four lines, as list by line: {lines_list}')
      print(f'Next 100 characters, as list by line, rounded up to complete lines{C}')