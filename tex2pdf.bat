echo off
mkdir _out 2> NUL
latex -halt-on-error -interaction=batchmode -output-directory=_out %1.tex > NUL 2> NUL
echo on
latex -halt-on-error -interaction=batchmode -output-directory=_out %1.tex
dvips -q* _out/%1.dvi
ps2pdf %1.ps