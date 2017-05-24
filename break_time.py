import webbrowser
import time

count =0;
while count<3:
    time.sleep(10)  # time is in seconds
    webbrowser.open("https://www.youtube.com/channel/UC1D6CKzuMctHydbPEHuZudA")
    count=count+1

# # # # #!/usr/bin/python3
# # # #
# # # # str = 'Hello World!'
# # # #
# # # # print (str)          # Prints complete string
# # # # print (str[0])       # Prints first character of the string
# # # # print (str[2:5])     # Prints characters starting from 3rd to 5th
# # # # print (str[2:])      # Prints string starting from 3rd character
# # # # print (str * 2)      # Prints string two times
# # # # print (str + "TEST") # Prints concatenated string
# # #
# # #
# # # #!/usr/bin/python3
# # #
# # # list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# # # tinylist = [123, 'john']
# # #
# # # print (list)          # Prints complete list
# # # print (list[0])       # Prints first element of the list
# # # print (list[1:3])     # Prints elements starting from 2nd till 3rd
# # # print (list[2:])      # Prints elements starting from 3rd element
# # # print (tinylist * 2)  # Prints list two times
# # # print (list + tinylist) # Prints concatenated lists
# #
# #
# # #!/usr/bin/python3
# #
# # tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# # tinytuple = (123, 'john')
# #
# # print (tuple)           # Prints complete tuple
# # print (tuple[0])        # Prints first element of the tuple
# # print (tuple[1:3])      # Prints elements starting from 2nd till 3rd
# # print (tuple[2:])       # Prints elements starting from 3rd element
# # print (tinytuple * 2)   # Prints tuple two times
# # print (tuple + tinytuple) # Prints concatenated tuple
#
#
# #!/usr/bin/python3
#
# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"
#
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
#
#
# print (dict['one'])       # Prints value for 'one' key
# print (dict[2])           # Prints value for 2 key
# print (tinydict)          # Prints complete dictionary
# print (tinydict.keys())   # Prints all the keys
# print (tinydict.values()) # Prints all the values


# print(10**2)