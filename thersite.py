import re
import requests
import argparse


def collect_tar_dewpoints(inputfile, outputfile = None, unit='C'):
    # return dew points of selected tar species using the ECN thersite tar dewpoint calculator

    # arguments:
    #   - inputfile is thersite-readable input (cf. template)
    #   - outputfile a custom file to save calculated dewpoints, optional
    #   - unit: temperature in C or K for Celsius or Kelvin
    
    # go to thersite homepage, save cookie and html which has info we need to pass back later
    response = requests.get('https://thersites.nl/completemodel.aspx')
    content = response.text
    jar = response.cookies

    # strings to look out for in the html, we look for the text in between (.+?)
    pattern_viewstate = """__VIEWSTATE" value="(.+?)" />"""
    pattern_viewstategen = """__VIEWSTATEGENERATOR" value="(.+?)" />"""
    pattern_eventvalidation = """"__EVENTVALIDATION" value="(.+?)" />"""

    # find the strings in the html 
    viewstate = re.search(pattern_viewstate, content).group(1)
    viewstategen = re.search(pattern_viewstategen, content).group(1)
    eventvalidation = re.search(pattern_eventvalidation, content).group(1)

    # now we begin to construct our POST statement
    
    # first create the passed parameters (equivalent to curl -F)
    files = {
        'master$body$impFile': (inputfile, open(inputfile, 'rb')),
        '__VIEWSTATE': (None, viewstate),
        '__VIEWSTATEGENERATOR': (None, viewstategen),
        '__EVENTVALIDATION': (None, eventvalidation),
        'master$body$btnImport': (None, 'Import')
    }

    # we need this certain header in order to make the request work (equivalent to curl -H)
    headers = {
        'Host': 'www.thersites.nl',
        'Origin': 'https://www.thersites.nl',
        'Referer': 'https://www.thersites.nl/completemodel.aspx'
    }

    # post the request to the site, hook up files, header and the cookie (equivalent to  curl -b/c) we saved before
    response = requests.post('https://thersites.nl/completemodel.aspx', cookies=jar, files=files, headers=headers)

    # get the response, from this html answer we are going to extract the dew points now
    content_response = response.text

    # we look for the dew point in K, so we extract all text between the K and the Celsius values from the html
    start = content_response.find("Dew point (K)") + len("Dew point (K)")
    end = content_response.find("Dew point (&deg;C)")
    dewpoints = content_response[start:end]

    # in the remaining string, we look for float-similar data by a regular expression
    dewpoints_list = re.findall("\d+\.\d+", dewpoints)
    dewpoints_list = [float(x) for x in dewpoints_list]

    # calculate temperature in Celsius instead of Kelvin
    if unit == 'C':
        dewpoints_list = [x - 273.15 for x in dewpoints_list]
        
    print(dewpoints_list)

    # if output flag is called, we write the dewpoints linewise to a file
    if outputfile:   
        with open(outputfile, 'w') as f:
            for item in dewpoints_list:
                # f.write("%s\n" % item)
                f.write(f"{item:.1f}\n")
            f.close()
        

if __name__ == "__main__":
   # define args (file and output file)
    parser = argparse.ArgumentParser(description='Define input file for thersites.nl')
    parser.add_argument('-f', '--file', help='path to input file', required=True)
    parser.add_argument('-o', '--output', help='path to output file', required=False)
    parser.add_argument('-u', '--unit', help='C or K', required=False)
    args = vars(parser.parse_args())
    
    collect_tar_dewpoints(args['file'], args["output"], args['unit'])
    