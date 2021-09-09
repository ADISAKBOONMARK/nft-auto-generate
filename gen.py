import json
import os
from PIL import Image
from decouple import config

COUNT = int(config('COUNT'))
INPUT_FILE_TYPE = config('INPUT_FILE_TYPE')
OUTPUT_FILE_TYPE = config('OUTPUT_FILE_TYPE')

########################################################################
# Utility code
########################################################################
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

        i=0
        for propertyValue in propertyValueList:
            image_file='images/' + propertyNameList[i] + '/' + propertyValue[image_id % len(propertyValue)] + INPUT_FILE_TYPE
            image_file_list.append(image_file)
            i=i+1

        # print('Image File List:', image_file_list)

        print('Create Token ID:', image_id, '-> DONE' )

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
        f.write(json.dumps(image_file_list))
        f.close()

    #     print('Create Token ID:',token_id,'-> DONE' )

    #     background = BACKGROUND[token_id % len(BACKGROUND)] 
    #     body = BODY[token_id % len(BODY)]
    #     eyes = EYES[token_id % len(EYES)] 
    #     head = HEAD[token_id % len(HEAD)] 
    #     mouth = MOUTH[token_id % len(MOUTH)]
    #     skin = SKIN[token_id % len(SKIN)]

    return 'END'
 
########################################################################
# Main flow of execution
########################################################################

if __name__ == '__main__':
    print(create())
