from stack_and_queue.stack import Stack
    
def validate_brackets(input):
    try:
        if input == '': return 'invalid input'
        save_open = Stack()
        save_close =''
        success = [['(',')'], ['[',']'], ['{','}']]

        for char in input:
            if char == '(' or char == '[' or char == '{' :
                    save_open.push(char)
            if char == ')' or char == ']' or char == '}' :
                save_close = char
                result = [save_open.pop(),save_close]
                if result not in success:
                    return False
        return True

    except:
        return 'invalid input'

print (validate_brackets("{}"))
print (validate_brackets("{}(){}"))
print (validate_brackets("()[[Extra Characters]]"))
print (validate_brackets("(){}[[]]"))
print (validate_brackets("{}{Code}[Fellows](())"))
print (validate_brackets("[({}]"))
print (validate_brackets("(]("))
print (validate_brackets("{(})"))  



####### Trial 1 ####### 

def  validate(input):
    openning_brackets = Stack()
    closing_brackets = Stack()

    for char in input: 
        if char == '(' or char == '[' or char == '{' :
            openning_brackets.push(char)
        if char == ')' or char == ']' or char == '}' :
            closing_brackets.push(char)

    if '(]' in input or  '(}' in input or '[)' in input or  '[}' in input or '{)' in input or '{]' in input :
        return False

    while openning_brackets.top:
        result = [openning_brackets.pop(),closing_brackets.pop()]
        if result != ['(',')'] and result != ['[',']'] and result != ['{','}'] :
            return False
    return True
