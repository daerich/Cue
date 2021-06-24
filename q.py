import sys
import glob
import os

def string_surge(left,right,center):
    res=[]
    for x in left:
        res.append(x)
    for x in center:
        res.append(x)
    for x in right:
        res.append(x)
    return ''.join(res)


def glue_print(lst,mode=0): # Mode == 0 -> Print local include
    for it in lst:        # Mode == 1 -> Print sysdir include
        if mode == 1:
            print("#include <" + it + " >")
        else:
            print('#include "' + it + ' "')

def is_whitespace(char):
    
    return char == "\n" or char == "\t" or char == " " or char == "\t"


def strgen(line,lastline,chars,path):
    res=[]
    strlst=chars.split(',')
    for x in range(0,len(strlst)): # Correct splitting artifacts
            strlst[x]=strlst[x].replace('{','')
            strlst[x]=strlst[x].replace('}','')
    
    if path == '':
        path=os.getcwd()
    for strn in strlst:
        strn=string_surge(line,'',strn) + lastline  # Generate file list
        for file in os.listdir(path):
            if strn == file:
                res.append(file)
    return res

def strparse(chars,path):  
    lwb=None
    if (lwb := chars.find("{")) != -1: # Determine mode
        upb=None
        if (upb := chars.find("}")) != -1:
            return strgen(chars[0:lwb],chars[upb+1:len(chars)],chars[lwb:upb],path)
    elif chars.find("*") != -1:
        return glob.glob(path+chars)
    else:
        return False

    
def scan_proc(line,envr):
    ind=line.find("#include")
    if ind != -1:
        if ind > 0:
            is_white=True
            for x in range(0,ind):
                if not is_whitespace(line[x]):
                    is_white=False
                    break
                if is_white:
                    if (ind2 := line.find("<")) == -1:
                        if (ind2 := line.find('"')) != -1:
                            res=strparse(line[ind2+1:line.rfind('"')],envr)
                            if res:
                                glue_print(res)
                                return True
                            else:
                                return False

                    elif (ind2 := line.find("<")) != -1:
                        res=strparse((line[ind2+1:line.rfind('>')]),envr)
                        if res:
                            glue_print(res,1)
                            return True
                        else:
                            return False
                
                else:
                    continue
        else:
            if (ind2 := line.find("<")) == -1:
                if (ind2 := line.find('"')) != -1:
                    res=strparse(line[ind2+1:line.rfind('"')],envr)
                    if res:
                        glue_print(res)
                        return True
                    else:
                        return False

            elif (ind2 := line.find("<")) != -1:
                    res=strparse((line[ind2+1:line.rfind('>')]),envr)
                    if res:
                        glue_print(res,1)
                        return True
                    else:
                        return False



def main():
    if len(sys.argv) <= 1:
        print("Usage:\n q [FILE...]\n"\
                " where FILE is a file to be processed")
        return
    for file in sys.argv:
        if file == sys.argv[0]:
            continue
        with open(file,"r") as f:
            if "LIBPATH" not in os.environ:
                pathn=""
            else:
                pathn=os.environ["LIBPATH"]
            while line := f.readline():
                if not scan_proc(line,pathn):
                    print(line)
                
main()
