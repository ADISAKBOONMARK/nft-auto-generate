import json
import os
from PIL import Image

CONFIG = json.loads(open('config.json', 'r').read())

NAME =  CONFIG['NAME']
DESCRIPTION = CONFIG['DESCRIPTION']
IMAGE_URL = CONFIG['IMAGE_URL']

def set_properties():

    metadata_files = os.listdir('output/metadata')
    metadata_files.remove(".keep")

    for file_id in range(1, len(metadata_files)):

        metadata = json.loads(open('output/metadata/%s' % file_id, 'r').read())

        metadata["name"] = NAME + " #" + str(file_id)
        metadata["image"] = IMAGE_URL + str(file_id) + '.png'
        metadata["description"] = DESCRIPTION
    
        print(metadata["image"])

        f = open('output/metadata/%s' % file_id, 'w')

        f.write(json.dumps(metadata))
        f.close()
        
    return 'END'
 
########################################################################
# Main flow of execution
########################################################################

if __name__ == '__main__':
    print(set_properties())