
def data_cleaning(filename):

    with open(filename,'r') as file1:
      content = file1.readlines()
      content = [i.strip('\n') for i in content if '\n' in i ]
      content = [i for i in content if i!=""]
      content = [i for i in content if len(i) !=1]
      content = [i for i in content if i =='top of pages']

    with open('output.txt','w') as final:
        for i in content:
            final.write(i+"\n")

    return content


print(data_cleaning('countries.txt'))