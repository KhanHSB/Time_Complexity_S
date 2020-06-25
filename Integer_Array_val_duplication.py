test = [1,2,3,4,5,5,6,7,8,7,9,6,2,3]
test2 = [1,2,3,4,5,5,6,7,8,7,9,6,2,3,3,2]
def create_hashtable(input_list):
    #print("Test_input: ", test2)
    list_of_tuples = {} # empty dictionary to contain a list of tuples ( A number : Index of reptition)
    list_len = len(input_list) # length of the input list
    
    for i in range(0 , list_len-1):
        current_pointer  = input_list[i] # Points fo the current int
        search_pointer = input_list[i] # Points to the pointer searching for a copy of the integer
        counter = 0
        for j in range(i + 1, list_len): # Inner loop to search the remaining list for a copy.
            search_pointer = input_list[j]
            counter = counter + 1 
            
            if (search_pointer == current_pointer): # If copy is found.
                current_tuple = (search_pointer, counter) # Stores the value of the Current Number : Index of its repetition.
                #print(current_tuple) # WPNT
                # Check if counter is not in dictionary
                #print("Curr tuple 0", current_tuple[0], "ListKeys: " , list_of_tuples.keys())
                if (current_tuple[0] not in list_of_tuples.keys()): # $T$ 
                #    print("Not in Dict")
                    # If Current_tuple is not in dictionary / add to dictionary
                    # Dict [key] = value
                    list_of_tuples[current_tuple[0]] = current_tuple[1]
                # Check if counter is already in dictionary.
                elif(current_tuple[0] in list_of_tuples.keys()):
                #    print("In Dict")
                    key_current = current_tuple[0]
                    value_current = current_tuple[1]
                    
                    # Second / Check if the key's value is already the smallest 
                    if (list_of_tuples.get(key_current) > value_current):
                        list_of_tuples[key_current] = value_current
                    # If new value is smaller replace current value
                #print("****************************************")
    print (str(list_of_tuples))
    return list_of_tuples
    
                    
test_3 = {2: 3, 3: 1, 5: 1, 6: 5, 7: 2}

def find_smallest(input_dict):
    if (len(input_dict) == 0):
        return (-1)
    else:
        
        start_key = int(list(input_dict.keys())[0])
        
        lowest_value = input_dict[start_key]
        lowest_value_key = start_key
        
        for key in input_dict:

            if (lowest_value > input_dict[key]):
                lowest_value = input_dict[key]
                lowest_value_key = key
                
        print("LV: ", lowest_value_key, "LVC: ", lowest_value) 
        return lowest_value_key            
                        
        
    



def firstDuplicate(a):
    dictO = create_hashtable(a)
    smallest = find_smallest(dictO)
    
    print(smallest)
    return smallest

