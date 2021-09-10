import json
import os
from PIL import Image

CONFIG = json.loads(open('config.json', 'r').read())

COUNT = int(CONFIG['COUNT'])
INPUT_FILE_TYPE = CONFIG['INPUT_FILE_TYPE']
OUTPUT_FILE_TYPE = CONFIG['OUTPUT_FILE_TYPE']

def matching(image_file_list, image_id):
    composite = None
    for image_file in image_file_list:

        foreground = None
        if image_file.find("None") == -1:
            foreground = Image.open(image_file).convert('RGBA')

        if foreground:
            if composite:
                composite = Image.alpha_composite(composite, foreground)
            else:
                composite = foreground

    output_path = 'output/images/' + str(image_id) + OUTPUT_FILE_TYPE
    composite.save(output_path)

def create():

    STORE=[]
    propertyNameList = os.listdir('images')
    # print('Property Name List:', propertyNameList)
    
    propertyValueList=[]
    for propertyName in propertyNameList:
        propertyValueList.append([w.replace('.PNG', '') for w in os.listdir('images/' + propertyName)])
    # print('Property Value List:', propertyValueList)

    for image_id in range(1, COUNT + 1):
        image_file_list = []
        properties = []
        i=0
        for propertyValue in propertyValueList:
            properties.append({
                "name": ((propertyNameList[i]).split('_'))[1], 
                "value": propertyValue[image_id % len(propertyValue)]
            })
            image_file='images/' + propertyNameList[i] + '/' + propertyValue[image_id % len(propertyValue)] + INPUT_FILE_TYPE
            image_file_list.append(image_file)
            i=i+1

        # print('Image File List:', image_file_list)

        print('Create Image ID:', image_id, '-> DONE' )

        matching(image_file_list, image_id)

        if(len(STORE) == 0):
            STORE.append(image_file_list)  
        else:
            for i in range(len(STORE)):
                if STORE[i] == image_file_list:
                    print("Image ID:", image_id, "duplicate! to Image ID:", i + 1)
                    break

            STORE.append(image_file_list)
    
        f = open('output/properties/' + str(image_id) + '.txt', "w")
        f.write(json.dumps(properties))
        f.close()

    return 'END'
 
########################################################################
# Main flow of execution
########################################################################

if __name__ == '__main__':
    print(create())
