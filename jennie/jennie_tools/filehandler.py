import json, os
import urllib.request

class FileHandler():
    def replace_file_from_link(self, file_link, output_path):
        '''
        If output_path and link is proper,
        delete old file and download new file on the same path.
        '''
        if not os.path.isfile(output_path):
            print ("invalid file {}".format(output_path))
            return False

        if file_link[:10] != "https://" or file_link[:10] != "http://" :
            print ("invalid link, Link must be of type http or https. LINK {}".format(output_path))
            return False

        if output_path.split("/")[-1] != file_link.split("/")[-1]:
            print ("Output file name is different from input file path.")
            return False

        os.system("rm -rf {}".format(output_path))
        urllib.request.urlretrieve(file_link, output_path)
        return True



