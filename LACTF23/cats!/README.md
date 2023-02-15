## misc/CATS!
<details>
  <summary>Description</summary>
  
  > CATS OMG I CAN'T BELIEVE HOW MANY CATS ARE IN THIS IMAGE I NEED TO VISIT CAN YOU FIGURE OUT THE NAME OF THIS CAT HEAVEN? <br>
  > Answer is the domain of the website for this location. For example, if the answer was ucla, the flag would be lactf{ucla.edu}. <br> [CATS.jpeg](./CATS.jpeg)

</details>

Check the metadata file using Exiftool and got the bunch of information, we're dominant to `Location : Lanai Cat Sanctuary`

```bash
$ exiftool CATS.jpeg
ExifTool Version Number         : 12.40
File Name                       : CATS.jpeg
Directory                       : .
File Size                       : 4.7 MiB
File Modification Date/Time     : 2023:02:11 11:05:45+07:00
File Access Date/Time           : 2023:02:16 05:57:29+07:00
File Inode Change Date/Time     : 2023:02:11 11:05:45+07:00
File Permissions                : -rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : Apple
Camera Model Name               : iPhone SE (2nd generation)
Orientation                     : Rotate 90 CW
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : 15.5
Modify Date                     : 2022:06:17 12:52:05
Host Computer                   : iPhone SE (2nd generation)
Y Cb Cr Positioning             : Centered
Exposure Time                   : 1/144
F Number                        : 1.8
Exposure Program                : Program AE
ISO                             : 20
Exif Version                    : 0232
Date/Time Original              : 2022:06:17 12:52:05
Create Date                     : 2022:06:17 12:52:05
Offset Time                     : -10:00
Offset Time Original            : -10:00
Offset Time Digitized           : -10:00
Components Configuration        : Y, Cb, Cr, -
Shutter Speed Value             : 1/144
Aperture Value                  : 1.8
Brightness Value                : 6.672492018
Exposure Compensation           : 0
Metering Mode                   : Multi-segment
Flash                           : Off, Did not fire
Focal Length                    : 4.0 mm
Subject Area                    : 2013 1511 2217 1330
Run Time Flags                  : Valid
Run Time Value                  : 526663128177750
Run Time Scale                  : 1000000000
Run Time Epoch                  : 0
Acceleration Vector             : -0.06026777624 -0.8702277539 -0.4827761948
Sub Sec Time Original           : 057
Sub Sec Time Digitized          : 057
Flashpix Version                : 0100
Color Space                     : Uncalibrated
Exif Image Width                : 4032
Exif Image Height               : 3024
Sensing Method                  : One-chip color area
Scene Type                      : Directly photographed
Exposure Mode                   : Auto
White Balance                   : Auto
Focal Length In 35mm Format     : 28 mm
Scene Capture Type              : Standard
Lens Info                       : 3.99000001mm f/1.8
Lens Make                       : Apple
Lens Model                      : iPhone SE (2nd generation) back camera 3.99mm f/1.8
Composite Image                 : General Composite Image
GPS Version ID                  : 2.3.0.0
GPS Map Datum                   : WGS-84
Compression                     : JPEG (old-style)
Thumbnail Offset                : 2478
Thumbnail Length                : 11136
Current IPTC Digest             : 50350e5c967628d3532b5317912bff65
Coded Character Set             : UTF8
Envelope Record Version         : 4
Sub-location                    : Lanai Cat Sanctuary
Province-State                  : HI
Country-Primary Location Code   : US
Country-Primary Location Name   : United States
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 12.42
Country Code                    : US
Location                        : Lanai Cat Sanctuary
Location Created City           : Lanai City
Location Created Country Code   : US
Location Created Country Name   : United States
Location Created Province State : HI
Location Created Sublocation    : Lanai Cat Sanctuary
City                            : Lanai City
Country                         : United States
State                           : HI
Metadata Date                   : 2023:02:09 15:48:44-08:00
Profile CMM Type                : Apple Computer Inc.
Profile Version                 : 4.0.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2022:01:01 00:00:00
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Apple Computer Inc.
Device Model                    :
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Apple Computer Inc.
Profile ID                      : ecfda38e388547c36db4bd4f7ada182f
Profile Description             : Display P3
Profile Copyright               : Copyright Apple Inc., 2022
Media White Point               : 0.96419 1 0.82489
Red Matrix Column               : 0.51512 0.2412 -0.00105
Green Matrix Column             : 0.29198 0.69225 0.04189
Blue Matrix Column              : 0.1571 0.06657 0.78407
Red Tone Reproduction Curve     : (Binary data 32 bytes, use -b option to extract)
Chromatic Adaptation            : 1.04788 0.02292 -0.0502 0.02959 0.99048 -0.01706 -0.00923 0.01508 0.75168
Blue Tone Reproduction Curve    : (Binary data 32 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 32 bytes, use -b option to extract)
Image Width                     : 4032
Image Height                    : 3024
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Run Time Since Power Up         : 6 days 2:17:43
Aperture                        : 1.8
Image Size                      : 4032x3024
Megapixels                      : 12.2
Scale Factor To 35 mm Equivalent: 7.0
Shutter Speed                   : 1/144
Create Date                     : 2022:06:17 12:52:05.057-10:00
Date/Time Original              : 2022:06:17 12:52:05.057-10:00
Modify Date                     : 2022:06:17 12:52:05-10:00
Thumbnail Image                 : (Binary data 11136 bytes, use -b option to extract)
GPS Latitude                    : 20 deg 47' 27.52" N
GPS Longitude                   : 156 deg 57' 50.03" W
GPS Latitude Ref                : North
GPS Longitude Ref               : West
Circle Of Confusion             : 0.004 mm
Field Of View                   : 65.5 deg
Focal Length                    : 4.0 mm (35 mm equivalent: 28.0 mm)
GPS Position                    : 20 deg 47' 27.52" N, 156 deg 57' 50.03" W
Hyperfocal Distance             : 2.07 m
Light Value                     : 11.2
Lens ID                         : iPhone SE (2nd generation) back camera 3.99mm f/1.8
```

Then you can just googling it, got the domain for a flag is `lanaicatsanctuary.org`

<details>
  <summary>FLAG</summary>
  
  `lactf{lanaicatsanctuary.org}`
  
</details>
