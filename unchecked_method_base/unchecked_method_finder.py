# We try to extract the source code based on the results of the ripgrep
# First we read the first node of the file line, and locate the function by the path and number of line
# Second, we find the entire function body by the brace matching "{" 
# If the line is end with  {, then to find the final }
# Otherwise, we find the nearest {, and repeat the method above.
# We loaded the lines of a funciton to the output file.

import os
import csv

rg_result_file = "../ripgrep/unchecked_numbers.txt"

rust_src_path = "../../refs/rust/library/"

output_file = "./output.txt"

def read_rg_result(input_file,src_path, output_file):
    csv_head = ["Path","Library","Start_line","End_line","Func"]
    with open ("data.csv","w") as w:
        writer = csv.writer(w)
        writer.writerow(csv_head)
        with open(input_file, "r") as f:
            for line in f.readlines():
                items = line.split()
                source= items[0].split(":")
                function_path = source[0]
                function_path = os.path.join(src_path,function_path)
                line_number = int(source[1])
                endchar = items[-1]

                # print(function_path,line_number,endchar)
                # having gotten the function path and the line_number, we have to locate it and get the end line number by brace match
                start_line_number, end_line_number,source_code = get_source_code(function_path, line_number, endchar)
                source_code = "".join(source_code)
                library = "null"
                data_node = [function_path,library,start_line_number,end_line_number,source_code]
                # print(data_node)
                writer.writerow(data_node)
                # break



def get_source_code(path, start_line_number, endchar) -> tuple[int,int, list[str]]:
    if endchar != '{':
        return start_line_number,0,[]
    with open(path, "r") as f:
        lines = f.readlines()

    idx = start_line_number - 1
    func_body = []
    brace_stack = []

    for i in range(idx, len(lines)):
        func_body.append(lines[i])
        if '{' in lines[i]:
            brace_stack.append('{')
            idx = i
            break
    for i in range(idx+1, len(lines)):
        func_body.append(lines[i])
        
        for char in lines[i]:
            if char == '{':
                brace_stack.append('{')
            elif char == '}':
                brace_stack.pop()
                if not brace_stack:
                    f.close()
                    return start_line_number, i+1, func_body
                
        




if __name__=="__main__":
    print("hello")
    read_rg_result(rg_result_file,rust_src_path,output_file)
