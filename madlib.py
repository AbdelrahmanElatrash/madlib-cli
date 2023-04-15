import re

welcome_message='''
welcom in our game  madlib
in this game we will ask you to enter some words 
adjective and noun from comand line

then we will put what you enters in the text and 
print it to see it 

i hope you willget fun
'''

print(welcome_message)

def read_template(file_path):
    """
    Args:
        param1 : the path of the file
    Returns:
        data that inside the file
    
     Raises:
          unvalid path
    """
    try :
        with open(file_path, mode='r') as f :
            data=f.read()
            data_list=data.split("\n")
            
            return data
    except FileNotFoundError as e :
        raise e 





    


def parse_template(str):
    """
    Args:
        param1 : string with defult data that come from the file in read_template function
    Returns:
        string with variable holder for world that we will replace
        tuble contine the name of what we need for variable holder
    
     Raises:
          unvalid data type other than string
    """
    pattern = r"\{(.*?)\}"
    matches = re.findall(pattern, str)
    expected_parts=tuple(matches)

    pattern = r"\{(.*?)\}"
    expected_stripped = re.sub(pattern, "{}", str)
    
    return [expected_stripped, expected_parts]





def user_input(t):
    """
    Args:
        param1 : tuble with defult data that come from the file in parse_template function
                contine the name of what we need for variable holder
    Returns:
        
        tuble contine the user data that was prompt
    
     Raises:
          unvalid data type that cann't iterate
    """
    input_list=[]
    
    for item in t:
        input_data=input(f'enter {item} : ') 
        input_list.append(input_data)
    return tuple(input_list)
    
    



def merge(str,t): 
    """
    Args:
        param1 : string with variable holder for world that we will replace
        param2 : tuble contine the user data that was prompt
    Returns:
        
        string contine the user data nested than variable holder
    
     Raises:
          unvalid data type 
    """
    result=str.format(*t)
    return result



if __name__=="__main__":
    data=read_template('file.txt')   # call the function and save data in var
    expected_parts=parse_template(data)[1]
    input_tubles=user_input(expected_parts)
    expected_stripped=parse_template(data)[0]
    print(merge(expected_stripped,input_tubles))