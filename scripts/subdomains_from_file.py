import re

def sub_extract(raw_data):
    try:
        with open(raw_data,"r") as raw_file, open(new_file,"w") as newfile:
            for lines in raw_file:
                stripped_lines=lines.strip()
                pattern=r"([a-zA-Z0-9.-]+)\.([a-zA-Z0-9.-]+)$"
                matching=re.match(pattern,stripped_lines)
                if matching:
                    result=matching.group(1)
                    print(result)
                    newfile.writelines(result+"\n")

    except Exception as e:
        print(f"An Error occured :{e}")

if __name__ == "__main__":
    file_for_input=input("Enter the name of the file you want to scan :")
    file_for_output=input("Enter the name of the file you want to save the input in :")
    raw_file=f"/home/ghost/work/yeshiva/{file_for_input}"
    new_file=f"/home/ghost/work/yeshiva/{file_for_output}"
sub_extract(raw_file)