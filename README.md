# 🐷 28PX PIG | NFT AUTO GENERATE

จัดทำขึ้นเพื่อให้ความรู้ในการสร้าง NFT แบบ อัตโนมัติ

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

## Setting

1. Install Python
2. Install Pip และ Pip Package

```sh
pip install python-decouple
```

3. Setup .env Create **.env**

```sh
COUNT=12 <-- จำนวนภาพ
INPUT_FILE_TYPE=.PNG <-- นามสกุลไฟล์ที่นำเข้า
OUTPUT_FILE_TYPE=.png <-- นามสกุลไฟล์ที่ส่งออก
```

4. Run

```sh
py gen.py
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
Image ID: 11 duplicate! to Image ID: 1 <-- รูปที่ 11 ซ้ำกับรุปที่ 1
Create Image ID: 12 -> DONE
Image ID: 12 duplicate! to Image ID: 2 <-- รูปที่ 12 ซ้ำกับรุปที่ 2
END
```

## คำอธิบายเพิ่มเติม

```sh
รูปภาพทั้งหมดจะถูกเก็บไว้ที่ images โฟลเดอร์

images/
-- 1_Background
-- 2_Skin
-- 3_Body
-- 4_Head
-- 5_Eyes
-- 6_Mouth

NOTE 1: ลำดับการทับกันของ Layer จะขึ้นอยู่กับเลขด้านหน้า images โฟลเดอร์ 1_*, 2_*, 3_* ตามลำดับ

NOTE 2: สามารถเพิ่มหรือลดจำนวน เครื่องประดับได้ เช่น ผู้ใช้อยากเพิ่มแขนตัวละครก็ให้สร้างโฟลเดอร์ 7_Arm เพิ่ม
```

```sh
รูปภาพทั้งหมดที่ถูกสร้างจะออกมาใน output/images โฟลเดอร์

images/
-- 1.png
-- 2.png
-- 3.png
```

```sh
สุดท้ายโปรแกรมจะสร้าง properties ให้ด้วยตามชื่อไฟล์ output/properties โฟลเดอร์

properties/
-- 1.txt
-- 2.txt
-- 3.txt

ตัวอย่าง
[{"name": "Background", "value": "Pink"}, 
{"name": "Skin", "value": "Pinky"}, 
{"name": "Body", "value": "Sun Flower T-Shirt"}, 
{"name": "Head", "value": "Banana"}, 
{"name": "Eyes", "value": "Chill Eyes"}, 
{"name": "Mouth", "value": "Pink Bubblegum"}]
```

## สนับสนุนผู้พัฒนา

🐷 28PX PIG

เป็น Pixel Art Pig Avatar AI Generated

โดยจะมีทั้งหมด 3,333 ชิ้น เป็น NFT ที่ซื้องานผ่านทาง Smart Contract
ทางเว็บไซต์

✅https://69pixel-nft.club/pig

🚀https://opensea.io/collection/28px-pig

69pixel team

May the pig be with you. 🐖
