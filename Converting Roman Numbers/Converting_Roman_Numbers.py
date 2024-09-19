def double_letter_numbers(numerical_input):
    answer = 0
    if "CM" in numerical_input:
        answer += 900
        numerical_input = numerical_input.replace("CM", "")
    if "CD" in numerical_input:
        answer += 400
        numerical_input = numerical_input.replace("CD", "")
    if "XC" in numerical_input:
        answer += 90
        numerical_input = numerical_input.replace("XC", "")
    if "XL" in numerical_input:
        answer += 40
        numerical_input = numerical_input.replace("XL", "")
    if "IX" in numerical_input:
        answer += 9
        numerical_input = numerical_input.replace("IX", "")
    if "IV" in numerical_input:
        answer += 4
        numerical_input = numerical_input.replace("IV", "")
        
    return numerical_input, answer


def roman_to_int(numerical_input):
    
    numerical_input, answer = double_letter_numbers(numerical_input)
    
    for i in numerical_input:
        
        match i:
            case 'M':
                answer += 1000
            case 'D':
                answer += 500
            case 'C':
                answer += 100
            case 'L':
                answer += 50
            case 'X':
                answer += 10
            case 'V':
                answer += 5
            case 'I':
                answer += 1
            case _: 
                print('The was a letter that is not a roman number')
                break
            
    return answer



numerical_input = input('Enter the roman numerals you want to convert: ').upper()
print('The roman numerals you entered translates to ', roman_to_int(numerical_input))

