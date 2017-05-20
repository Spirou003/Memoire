import os, sys

if (len(sys.argv) != 2):
    print "Require one arg"
    quit()
#
name = sys.argv[1]
os.system("mkdir _out")
os.system("latex -halt-on-error -interaction=batchmode -output-directory=_out "+name+".tex > NUL 2> NUL")

os.system("latex -halt-on-error  -output-directory=_out "+name+".tex")
os.system("dvips -q* _out/"+name+".dvi")
os.system("ps2pdf "+name+".ps")
