import json
import os
from PIL import Image

def build_image(image_files, image_id):
    composite = None
    for image_file in image_files:

        foreground = None
        if image_file.find("None") == -1:
            foreground = Image.open(image_file).convert('RGBA')

        if foreground:
            if composite:
                composite = Image.alpha_composite(composite, foreground)
            else:
                composite = foreground

    output_path = '../../output/images/%s.png' % image_id
    composite.save(output_path)
   
def createArt(start, limit):

    STORE=[]
    
    SKIN = [w.replace('.PNG', '') for w in os.listdir('../../images/2_Skin')]

    BODY = [w.replace('.PNG', '') for w in os.listdir('../../images/3_Body')]
    BODY.append('None')

    EYES = [w.replace('.PNG', '') for w in os.listdir('../../images/4_Eyes')]

    for image_id in range(start, limit + 1):

        body = BODY[image_id % len(BODY)]
        eyes = EYES[image_id % len(EYES)] 
        skin = SKIN[image_id % len(SKIN)]

        properties=[]
        properties.append({
            "name": "Skin", 
            "value": skin
        })
        properties.append({
            "name": "Body", 
            "value": body
        })
        properties.append({
            "name": "Eyes", 
            "value": eyes
        })
        
        image_arr = ['../../images/2_Skin/' + skin + '.PNG',
                    '../../images/3_Body/' + body + '.PNG',
                    '../../images/4_Eyes/' + eyes + '.PNG',]

        build_image(image_arr,image_id)

        if(len(STORE) == 0):
            STORE.append(image_arr)  

        else:
            for i in range(len(STORE)):
                if STORE[i] == image_arr:
                    print("Image ID:", image_id, "duplicate! to Image ID:", i + 1)
                    break

            STORE.append(image_arr)

        print('Create Image ID:',image_id,'-> DONE' )

        f = open('../../output/properties/' + str(image_id) + '.txt', "w")
        f.write(json.dumps(properties))
        f.close()

        image_id=image_id+1

    return 'END'
 
########################################################################
# Main flow of execution
########################################################################

if __name__ == '__main__':
    
    start=1
    limit=5
    createArt(start, limit)
