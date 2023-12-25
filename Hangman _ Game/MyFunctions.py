# class Util:
#     @staticmethod
#     def read_choice(msg, start = 1, end = 1):
#         while True:
#             try:
#                 num = int(input(msg))
#             except:
#                 print("ERROR!! Number is expected")
#                 print("Try Again\n")
#                 continue
#             else:
#                 if not (1 <= num <= end):
#                     print(f"ERROR!! Number between {start} and {end} is expected")
#                     print("Try Again\n")
#                     continue

#             return num
        
#     @staticmethod
#     def isyes(msg):
#         if input("\n\n" + msg) in ['y', 'Y']:
#             return True

#         return False

#     @staticmethod
#     def Draw_Line(character, space_size, char_frequency):
#         print(" "*space_size, end = '')

#         for i in range(char_frequency):
#             print(character, end = '')

#         print()

#     @staticmethod
#     def LoadtxtDataAsDict(file_name, delimeter):

#         data = {}

#         file = open(file_name, 'r')
#         for line in file.readlines():
#             if line != "":
#                 elements = line.split(delimeter)
#                 data[elements[0]] = float(elements[1])
#                 del elements
        
#         file.close()

#         return data
    
#     @staticmethod
#     def LoadtxtData(file_name):

#         data = []

#         file = open(file_name, 'r')
#         for line in file.readlines():
#             if line != "":
#                 data.append(line.strip())
        
#         file.close()

#         return data
    
#     @staticmethod
#     def StoreDictDataAstxt(file_name, delimeter, data):
#         file = open(file_name, 'w')
#         if data != dict():
#             for key in data:
#                 file.write(key + delimeter + str(data[key]) + '\n')

#         file.close()

#     @staticmethod
#     def is_String_True_False(string):
#         if string == "True":
#             return True
#         elif string == "False":
#             return False
#         else:
#             return None

    # def Draw_Header_Screen(msg, spaces = 25):
    #         Draw_Line('*', spaces, len(msg) + 12)
    #         print(" "*spaces + "*" + " "*5 + msg + " "*5 + '*')
    #         Draw_Line('*', spaces, len(msg) + 12)

    #         print()


def read_choice(msg, start = 1, end = 1):
    while True:
        try:
            num = int(input(msg))
        except:
            print("ERROR!! Number is expected")
            print("Try Again\n")
            continue
        else:
            if not (1 <= num <= end):
                print(f"ERROR!! Number between {start} and {end} is expected")
                print("Try Again\n")
                continue

        return num
    

def isyes(msg):
    print()
    
    while True:
        answer = input("\n" + msg)

        if answer in ['y', 'Y']:
            return True
        
        if answer in ['N', 'n']:
            return False
        
        print("Error!! input NOT acceptable\nTry Again")
    


def Draw_Line(character, space_size, char_frequency):
    print(" "*space_size, end = '')

    for i in range(char_frequency):
        print(character, end = '')

    print()


def LoadtxtDataAsDict(file_name, delimeter):

    data = {}

    file = open(file_name, 'r')
    for line in file.readlines():
        if line != "":
            elements = line.split(delimeter)
            data[elements[0]] = float(elements[1])
            del elements
    
    file.close()

    return data


def LoadtxtData(file_name):

    data = []

    file = open(file_name, 'r')
    for line in file.readlines():
        if line != "":
            data.append(line.strip())
    
    file.close()

    return data


def StoreDictDataAstxt(file_name, delimeter, data):
    file = open(file_name, 'w')
    if data != dict():
        for key in data:
            file.write(key + delimeter + str(data[key]) + '\n')

    file.close()

def Draw_Header_Screen(msg, spaces = 25):
        Draw_Line('*', spaces, len(msg) + 12)
        print(" "*spaces + "*" + " "*5 + msg + " "*5 + '*')
        Draw_Line('*', spaces, len(msg) + 12)

        print()

def is_String_True_False(string):
    if string == "True":
        return True
    elif string == "False":
        return False
    else:
        return None