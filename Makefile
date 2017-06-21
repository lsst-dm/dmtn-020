#export TEXMFHOME = lsst-texmf/texmf

DMTN-020.pdf: *.tex
	xelatex DMTN-020
	makeglossaries DMTN-020
	bibtex DMTN-020
	xelatex DMTN-020
	makeglossaries DMTN-020
	bibtex DMTN-020
	xelatex DMTN-020
	xelatex DMTN-020
