Call with arguments:

arguments
 - f / --file	(path to input file - see template)
 - o / --output	(path to output file - will be created)
 - u / -- unit	(K or C, C is default)


python thersite.py -f <path-to-txt.txt>
 -> output to console, linewise

python thersite.py -f <path-to-txt.txt> -o <path-to-output>
 -> saves results linewise to output file, will be overwritten

python thersite.py -f <path-to-txt.txt> -o <path-to-output> -u C
 -> like previous example, but in C
