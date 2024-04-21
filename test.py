from exec_cmd import exec_cat_on_file

with open("input.txt", "r") as file:
    contents = file.read()
    output, error = exec_cat_on_file(contents)
    print("output : |" +output  + "|")
    print("error : |" + error + "|")
