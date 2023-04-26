## Girl with a secret

<details>
  <summary>Description</summary>
  
  > [null]
  
  > Flag Format: CODEBY{}
  
</details>

Given a challenge in the form of a png [file](./task.png)

We checked the metadata of the file and found nothing suspicious

```bash
$ exiftool task.png
ExifTool Version Number         : 12.40
File Name                       : task.png
Directory                       : .
File Size                       : 887 KiB
File Modification Date/Time     : 2023:04:18 03:46:24+07:00
File Access Date/Time           : 2023:04:21 17:13:54+07:00
File Inode Change Date/Time     : 2023:04:21 17:12:30+07:00
File Permissions                : -rwxrwxrwx
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1350
Image Height                    : 1800
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1350x1800
Megapixels                      : 2.4
```

Then we checked the string contents and found no clue at all `$ strings task.png`

How about trying with `zsteg` maybe there is some hidden LSB data inside it, and there's it

```bash
$ zsteg task.png
b1,rgb,lsb,xy       .. text: "50:codeby{Be_c4r3FULL_NExT_TIMe_WIth_trAps_L1KE_Th1s}?"
b1,bgr,lsb,xy       .. file: OpenPGP Secret Key
b3,abgr,msb,xy      .. file: MPEG ADTS, layer I, v2, 256 kbps, Monaural
b4,b,msb,xy         .. file: MPEG ADTS, layer I, v2, 112 kbps, 24 kHz, JntStereo
```

<details>
  <summary>Flag</summary>
  
  > `codeby{Be_c4r3FULL_NExT_TIMe_WIth_trAps_L1KE_Th1s}`
  
</details>
