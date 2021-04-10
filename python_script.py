import os
import subprocess

a = input("enter directory: ") #argument to enter directory

if a == "?":
    print("-- If you want to recode all text files in a directory and subdirectories, enter : ./lab_21.sh directory encoding. The encoding type must be written in uppercase --")
    exit()

b = input("enter encoding: ") #argument to enter encoding

#cheking the validity of the entered encoding
cod_comm = 'iconv -l | grep "^{recipient}//"'
cod_comm = cod_comm.replace('{recipient}', b)

coding_1 = subprocess.run(cod_comm, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
coding = coding_1.stdout

if len(list(coding)) == 0:
    print(b + " is not valid encoding ")
    exit()


find_comm = 'find {recipient} -type f'
find_comm = find_comm.replace('{recipient}', a)

find_1 = subprocess.run(find_comm, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
find = find_1.stdout

file_1 = ''

for file in find:
    if file != '\n':
        file_1 += file
    else:
        # file type
        type_comm = "file --mime-type {argument} | cut -f 2 -d ' '"
        type_comm = type_comm.replace('{argument}', file_1)
        type_1 = subprocess.run(type_comm, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        typee = type_1.stdout

        # file encoding 
        encoding_comm = "file --mime-encoding {argument} | cut -f 2 -d ' '"
        encoding_comm = encoding_comm.replace('{argument}', file_1)
        encoding_1 = subprocess.run(encoding_comm, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        encoding = encoding_1.stdout

        encoding = encoding[0:-1]
        if str(typee) == "text/plain\n":
            iconv_comm = "iconv -c -o {argument} -f {argument_2}^^ -t {argument_1} {argument}"
            iconv_comm = iconv_comm.replace('{argument}', file_1)
            iconv_comm = iconv_comm.replace('{argument_1}', b)
            iconv_comm = iconv_comm.replace('{argument_2}', encoding)
            
            os.system(iconv_comm)

        file_1 = ''







