'''
problem :- xmltodict.parse() isnt able to handle the special characters in the incoming raw data and the code is crashing
aim :- code should be able to handle the special data , even if while parsing the special characters are replaced by blank its fine 
'''

import xmltodict

raw_data = "<Title>Submittal Cover Sheet Typical &quot;.+Arrangement Pour Height 6.5m &amp; 5.7m</Title>"

parsed_data = xmltodict.parse(raw_data)

print(f"parsed_data :- {parsed_data}")
