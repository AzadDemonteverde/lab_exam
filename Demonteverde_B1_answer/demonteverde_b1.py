def count_species(Exam_Table):

    file_content = []                       
    dictionary = {}                         

    file = open(file_name, "r")             
    content = file.readlines()              

    # print(content)
    for i in range(len(content)):           
        line = content[i].rstrip()          
        file_content.append(line)    

    file.close()

    for word in file_content:
        if word in dictionary.keys():       
            dictionary[word] += 1
        else:                              
            dictionary.update({word: 1})
    
    print(dictionary)

    with open("Exam_Table.csv", "w") as file:
        for word, count in dictionary.items():
            file.write("%s %s\n" % (word, count))

file_name = "Exam_Table.csv"
count_species(Exam_Table)

    