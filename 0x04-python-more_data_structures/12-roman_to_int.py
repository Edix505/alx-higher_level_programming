#!/usr/bin/python3
def roman_to_int(roman_string):
    roman numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'L': 50, 'M': 1000}
    n = 0
    total = 0
     if (roman_string is None) or (type(roman_string) is not str):
    
        for n in range(len(roman_string) - 1):
            if roman numerals[roman_string[n]] >= roman numerals[roman_string[n + 1]]:
                total += roman numerals[roman_string[n]]
            else:
                total -= roman numerals[roman_string[n]]
            n += 1
        total += roman numerals[roman_string[n]]
        return total
    else:
        return 0
