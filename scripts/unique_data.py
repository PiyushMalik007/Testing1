def uniq(duplicates):
    try:
        with open(duplicate_file,"r") as input_file, open(unique_file,"w") as output_file:
            sets=set(input_file)
            sets_sort=sorted(sets)
            for unique_values in sets_sort:
                print(unique_values)
                output_file.writelines(unique_values)
    except Exception as e:
        print(f"Error as {e}")

if __name__ == "__main__":

    # duplicate_file="/home/ghost/Research/Python/scripts/raw_data.txt"
    # unique_file="uniq_data.txt"
    duplicate_file=f"/home/ghost/work/yeshiva/{input('Enter the file name with duplicate data :')}"
    unique_file=f"/home/ghost/work/yeshiva/{input('Enter the file name for uniq extracted data :')}"
uniq(duplicate_file)