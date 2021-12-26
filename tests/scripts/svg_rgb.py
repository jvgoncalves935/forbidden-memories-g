import os
import re
from os import listdir
from os.path import isfile, join

substr_stroke = '<path stroke="'

def file_to_list(file_name):
    file = open(file_name,"r")
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    file.close()
    return lines

def change_line(line):
    #Find the rgba color
    
    substr_rgba = re.search('rgba(.*?)"',line)
    
    #The line doesn't have a rgba
    if(substr_rgba == None):
        return line
    
    substr = substr_rgba.group(1)[1:-1]
    substr_full = substr_rgba.group(0)
    aux_tuple = tuple(map(float,substr.split(',')))
    final_tuple = (int(aux_tuple[0]),int(aux_tuple[1]),int(aux_tuple[2]))
    line_split = line.split(substr_full)
    #print(substr)
    final_line = line_split[0] + rgba_to_hex(final_tuple)+'"' + line_split[1]
    return final_line

def rgba_to_hex(rgba):
    return '#{:02x}{:02x}{:02x}'.format(*rgba)

def main():
    folder = os.path.dirname(os.getcwd())+"\\fonts\\svg\\"
    final_folder = os.path.dirname(os.getcwd())+"\\fonts\\svg2\\"

    files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    for file_path in files:
        new_file = open(final_folder+os.path.basename(file_path),"w")
        
        for f in file_to_list(file_path):
            new_line = change_line(f)
        #    print(new_line)
            new_file.write(new_line+'\n')
        #print('')

        new_file.close()
        #break
    #print(rgba_to_hex((12,28,200,22)))
    return

if __name__== "__main__":
    main()