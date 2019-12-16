import operator
def a():
    with open ("chat.txt", "r") as myfile:
        content = myfile.readlines()
        content = [x.strip() for x in content]
    #print(content)
    num_list = []
    l1 = []
    l2 = []
    for w in content:
        l1 = [x for x in w.split(' ')]
        l2.append(l1)
    #print(l2)
    for w in l2:
        for i in w:
            if i.isnumeric():
                if i not in num_list:
                    num_list.append(i)           
    #print(num_list)
    dict = {}
    for i in num_list:
        weight = 0
        for l in content:
            if i in l:
                if "G:" in l:
                    weight+=2
                elif "M:" in l:
                    weight+=1
        dict[i] = weight
    #print(dict)
    flag = 0
    for i in dict:
        for j in dict:
            if dict[i] == dict[j] and i != j:
                flag = 1
                break
    if flag==0:            
        maximum = max(dict.items(), key=operator.itemgetter(1))[0]
        #print(maximum)
        if maximum == "19" or  maximum == "20":
            print("Date")
        else:
            print("No Date")
    else:
        print("No Date")
a()
