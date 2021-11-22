# 🐷 28PX PIG | NFT AUTO GENERATE

It was created to provide knowledge on how to create an automated NFT.

## Reference

Opensea Developer Tutorials: https://docs.opensea.io/docs/developer-tutorials

## Required Software

- Python [Download](https://www.python.org/downloads/)
- Pip [Download](https://pip.pypa.io/en/stable/getting-started/)

## Required IDE

- Visual Studio Code (VSCode) [Download](https://code.visualstudio.com/)

## Download

```sh
git clone https://github.com/ADISAKBOONMARK/nft-auto-generate.git
```

## For Artist 🎨

1. Setup config.json

```sh
{
    "COUNT": "12",                                  
    "INPUT_FILE_TYPE": ".png",                      
    "OUTPUT_FILE_TYPE": ".png"                      
    "NAME": "name",                                 
    "DESCRIPTION": "description",                  
    "IMAGE_URL": "https://domain.com/image/"        
}
```

2. Run

```sh
#== Windows ==#
./gen.exe
./set-properties.exe
```

```sh
#== Linux ==#
./gen
./set-properties
```

```sh
#== Mac ==#
./gen
./set-properties
```

## For Dev 🔥

1. Install Python
2. Install Pip

```sh
pip install Image
```

3. Setup config.json

```sh
{
    "COUNT": "12",                                  
    "INPUT_FILE_TYPE": ".png",                      
    "OUTPUT_FILE_TYPE": ".png"                      
    "NAME": "name",                                 
    "DESCRIPTION": "description",                   
    "IMAGE_URL": "https://domain.com/image/"        
}
```

4. Run generate images

```sh
py gen.py
#== OR ==#
python gen.py
```

5. Output

```sh
Create Image ID: 1 -> DONE
Create Image ID: 2 -> DONE
Create Image ID: 3 -> DONE
Create Image ID: 4 -> DONE
Create Image ID: 5 -> DONE
Create Image ID: 6 -> DONE
Create Image ID: 7 -> DONE
Create Image ID: 8 -> DONE
Create Image ID: 9 -> DONE
Create Image ID: 10 -> DONE
Create Image ID: 11 -> DONE
Image ID: 11 duplicate! to Image ID: 1 
Create Image ID: 12 -> DONE
Image ID: 12 duplicate! to Image ID: 2 
END
```

6. Run set properties images

```sh
py set-properties.py
#== OR ==#
python set-properties.py
```

7. Output

```sh
https://domain.com/image/1.png
https://domain.com/image/2.png
https://domain.com/image/3.png
https://domain.com/image/4.png
https://domain.com/image/5.png
https://domain.com/image/6.png
https://domain.com/image/7.png
https://domain.com/image/8.png
https://domain.com/image/9.png
https://domain.com/image/10.png
https://domain.com/image/11.png
END
```

## Explanation

```sh
All images are stored in the "images" folder.

images/
-- 1_Background
-- 2_Skin
-- 3_Body
-- 4_Head
-- 5_Eyes
-- 6_Mouth

NOTE 1: The layer overlap order is based on the number in front of the images folder 1_*, 2_*, 3_* respectively.

NOTE 2: Can increase or decrease the number. For example if you want to add an arm to your character. You can create an additional 7_Arm folder.
```

```sh
All images created will come out in output/images folder.

images/
-- 1.png
-- 2.png
-- 3.png
```

```sh
Finally, the program will generate metadata for you according to the file name. output/metadata folder.

metadata/
-- 1
-- 2
-- 3

Example

{
  "name": "name #1",
  "description": "description",
  "image": "https://domain.com/image/1.png",
  "attributes": [
    {
      "trait_type": "Background",
      "value": "Pink"
    },
    {
      "trait_type": "Skin",
      "value": "Pinky"
    },
    {
      "trait_type": "Body",
      "value": "Sun Flower T-Shirt"
    },
    {
      "trait_type": "Eyes",
      "value": "Chill Eyes"
    },
    {
      "trait_type": "Head",
      "value": "Banana"
    },
    {
      "trait_type": "Mouth",
      "value": "Pink Bubblegum"
    }
  ]
}
