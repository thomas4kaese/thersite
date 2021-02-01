# thersite
small python script for calculating tar dew points using ECN thersite calculator ("complete model", https://www.thersites.nl/completemodel.aspx)

# Usage

Call with arguments:

arguments
 - f / --file	(path to input file - see template)
 - o / --output	(path to output file - will be created)
 - u / -- unit	(K or C, C is default)


# Examples

python thersite.py -f <path-to-txt.txt>
 -> output to console, linewise

python thersite.py -f <path-to-txt.txt> -o <path-to-output>
 -> saves results linewise to output file, will be overwritten

python thersite.py -f <path-to-txt.txt> -o <path-to-output> -u C
-> like previous example, but in C
  
# Known issues
- if dew point is N/A (typically because of too low temperatures), the result will be skipped
- todo: check for N/A values when assessing results from page
