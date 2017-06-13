#export TEXMFHOME = lsst-texmf/texmf

DMTN-020.pdf: *.tex
	latexmk -bibtex -pdf -f LDM-020.tex

