import numpy as np 
class DataAnalytics:
    
    def create_1D_array(self):
        n = int(input("Enter the number of element you want to enter:"))
        l = [int(input("Enter the element: ")) for i in range(n)]
        array = np.array(l)
        return array
    def create_2D_array(self):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of the columns: "))
        print(f"Enter {rows*cols} elements for the array: ")
        l = [int(input("Enter the element: ")) for i in range(rows*cols)]
        array = np.array(l).reshape(rows,cols)
        return array
    def create_3D_array(self):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of the columns: "))
        print(f"Enter {rows*cols} elements for the array: ")
        l = [int(input("Enter the element: ")) for i in range(rows*cols)]
        array = np.array(l).reshape(2,rows,cols)
        a = []
        a.append(array)
        return array
    def search_value(self,array):
        elem = int(input("Enter the elem to be searched: "))
        is_elem_founded = False
        for i in array:
            for j in i:
                if j == elem:
                    is_elem_founded = True
                if is_elem_founded:
                    print("Elem is founded")
                else:
                    print("Elem not availabel")
obj = DataAnalytics()
while True:
    print("Welcome to the NumPy Analyzer!")
    print("===========================================")
    print("Choose an option:")
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Select the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        option = int(input("Enter your choice: "))
        if option == 1:
            array = obj.create_1D_array()
            print("\nArray created successfully: \n")
            print(array)
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            options = int(input("Enter your choice: "))
            if options == 1:
                index = int(input("Enter any index: "))
                print(f"Your value is {array[index]}")
            elif options == 2:
                start_val = int(input("Enter the start index val: "))
                end_val = int(input("Enter the end val: "))
                print(f"Your range/slice is {array[start_val:end_val]}")
            elif options == 3:
                break
            else:
                print("You have entered the wrong options..")
        elif option == 2:
            array = obj.create_2D_array()
            print("\nArray created successfully !\n")
            print(array)
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            opt = int(input("Enter your choice: "))
            if opt == 1:
                row_index = int(input("Enter the row index: "))
                col_index = int(input("Enter the col index: "))
                print(f"Your value is {array[row_index][col_index]}")
            elif opt == 2:
                start_val = int(input("Enter the start index val: "))
                end_val = int(input("Enter the end val: "))
                print(f"Your range/slice is {array[start_val:end_val]}")
            elif opt == 3:
                break
            else:
                print("You have entered the wrong options !.!")
        elif option == 3:
            array = obj.create_3D_array()
            print("\nArray created successfully !\n")
            print(array)
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            opt = int(input("Enter your choice: "))
            if opt == 1:
                block_index = int(input("Enter block index (0 or 1): "))
                row_index = int(input("Enter the row index: "))
                col_index = int(input("Enter the col index: "))
                print(f"Your value is {array[block_index][row_index][col_index]}")
            elif opt == 2:
                block_index = int(input("Enter block index (0 or 1): "))
                start_val = int(input("Enter the start index val: "))
                end_val = int(input("Enter the end val: "))
                print(f"Your range/slice is {array[block_index,start_val:end_val,:]}")
            elif opt == 3:
                break
            else:
                print("You have entered the wrong options !.!")
        else:
            print("You have entered the wrong option.. ")
    elif choice == 2:
        array1 = obj.create_2D_array()
        array2 = obj.create_2D_array()
        print("Choose a mathematical operation:")
        print("1. Addition")
        print("2. Subtractio")
        print("3. Multiplication")
        print("4. Division")
        value = int(input("Enter vour choice:  "))
        if value == 1:
            print(array1+array2)
        elif value == 2:
            print(array1-array2)
        elif value == 3:
            print(array1*array2)
        elif value == 4:
            print(array1/array2)
        else:
            print("\nYou have entered the wrong number")
    elif choice == 3:
        array1 = obj.create_2D_array()
        print(array1)

        array2 = obj.create_2D_array()
        print(array2)
        print("Choose an option ")
        print("1. Combine Arrays")
        print("2. Split Arrays")
        new = int(input("Enter your choice: "))
        if new == 1:
           combined_arrays = np.vstack(array1,array2)
           print(combined_arrays) 
        elif new == 2:
            splitted_arrays = np.vsplit(array1)
            print(splitted_arrays)
        else:
            print("You have entered the wrong options. ")
    elif choice == 4:
        array = obj.create_2D_array()
        print(array)
        print("Choose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        data_filter = int(input("Enter your choice: "))
        if data_filter == 1:
            obj.search_value(array)
        elif data_filter == 2:
            sorted_array = np.sort(array)
            print(f"Original Array: {array}")
            print(f"Sorted Array: {sorted_array}")
        elif data_filter == 3:
            val = int(input("Enter any value: "))
            filtered_arrays = array[array<val]
            print(f"Filtered array (All elements ehich are lesser than {val}): {filtered_arrays}")
        else:
            print("You have entered the wrong option.")
    elif choice == 5:
        array = obj.create_2D_array()
        print(array)
        print("Choose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        new_one = int(input("Enter your choice: "))
        if new_one == 1:
            print(f"Sum: {np.sum(array)}")
        elif new_one == 2:
            print(f"Mean: {np.mean(array)}")
        elif new_one == 3:
            print(f"Median: {np.median(array)}")
        elif new_one == 4:
            print(f"Stardard Deviation: {np.std(array)}")
        elif new_one == 5:
            print(f"Variation: {np.var(array)}")
        else:
            print("Wrong operation entered !") 
    elif choice == 6:
        print("\nThank you for using the NumPy Analyzer! Goodbye!")
        break
    else:
        print("You have entered the wrong choice ")