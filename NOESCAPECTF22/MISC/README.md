# MISC

<br>

## Welcome to NECTF
<img src="../img/1.jpg" width="400">

Just inspect it <b>CTRL + SHIFT + I</b>

<img src="../img/2.jpg">

<details>
  <summary>FLAG :</summary>
  
  `NECTF{w3LC0M3_t0_N3CTF}`

</details>

<br>

## Bad Cake
<img src="../img/3.jpg" width="400">

Here's a source of the `.dat` file

```
‰PNG

   
IHDR   õ   õ    ­Úì¹  ‚IDATxÚíÚAŽã0ÑÜÿÒ3Ë‚H©/Ê@$–W‰#ûy š"ùú×ñx©V­ZµjÕªUÿºúõýx;ù}­é)ßÖ~ütÝá%³»W­Zõõj°>½}vÃøégŸþZ¸{ÕªU÷PƒËø:\|þ
¼"Æ'«V­ZõäfæˆÆÿáyù%U«V­:UïIZË?S­Zµê`‡:OF¿\Ë|{UAµjÕ‡©óhùK=ØñQ­Zõ9j<Ô£tÞçˆÚ´T¹iGµjÕç¨A<,üÅÙ—ù½gÕªU7Qƒž)
Ðà[‘iï#ŸÐS­ZõÕê¼9…Q°ÀbS8Ê˜U«VÝDu7¢æØªG›çÒ“U­Zõõjçm¥y2Ò¼©ZµêžjšñÑ-ójÞ˜Ô+³»jÕªoVÓ@QÞ7ÅHš6ƒ’¡jÕª¯V—ç>»%÷M6UT«V}˜šÎŒDþ¨oB;¹ôÿg¡ª Zµê³Õó¬’¶8öŒDÁ=ÊWU«VÝDm·£¼¼'¢Û ý2—¢ZµêKÕùú´Z8î´ÄWy1ŒTµjÕ·¨é2`4ŽŽ¸€vn^sT­Zuwu4.Bã+Ý}ƒU¢õT«VÝXM£`¥­
öÜ4U¥…B2—¢Zµê«Ô‹Sl ð‚8¦ö;-«\ÕªU_ Î|L¥¼¿®ÜŸjÕª›¨iŒŒ>‚"cÔ½ßñ·ªU«¾^M÷ÒåÖmT_ÜS2T­Zu5H-Aô¥«Ð²ä¼^™w_T«V}¿:ol€þÈ£jaÔ ©÷>T«V}¢:ÚZGm
ÚPÙ“Ü–Þ\ªU«¾Y½{`…6vç'ƒ9âRW­Zõ±jdÒ¥³¶j¾‡ST«V­:!ÉŸx‹ÍÞRW­Zõ±j#çñš¶G@’’ò¶jÕªÛ©+E¼ÊtÝnÓ'–ÅpÕªU_ ®¸¢Û¯<„Ê›EµjÕ÷«£àY9…nÚAÎe®ªU«n¢¦G¥íÚ(Í|¯Zµê&êè~+ûkx‚m>Xg¤ªU«¾OM/¼§=µi£õ¾$²ªU«î¡žçty¥™&ÍWóÌUµjÕª—H$”súê\ŠjÕª›«ic#ïä.– £g¢Zµê&jðãh$¤›óU¢Ç3UÕªU¦1rÑmÕS_ÚUQ­ZõÕêF‡jÕªU«V­Zõoÿ³üNÇ¯Ðf<    IEND®B`‚
```

I just realised there’s a PNG information in `.dat` file so I accidentaly just change the `.dat` format to `.png` format, and how unexpected the `.png` file contain a image of QR-Code

<img src="../img/4.jpg" width="300">

After scanning the QR-Code here’s the result, there's message in base64

```bash
NGUgNDUgNDMgNTQgNDYgN2IgNTQgNDggMzEgMjQgNWYgMzEgMjQgNWYgNTkgMzAgNTUgNTIgNWYgNDcgNGYgMzAgNDQgNWYgNDMgNDAgNGIgMzMgN2Q=
```

Then after I decoded base64, we got Hex

```bash
$ echo 'NGUgNDUgNDMgNTQgNDYgN2IgNTQgNDggMzEgMjQgNWYgMzEgMjQgNWYgNTkgMzAgNTUgNTIgNWYgNDcgNGYgMzAgNDQgNWYgNDMgNDAgNGIgMzMgN2Q=' | base64 -d
```

<img src="../img/5.jpg">

We can use https://asciitohex.com to decoded Hex into ASCII

<img src="../img/6.jpg" width="350">

<details>
  <summary>FLAG :</summary>
  
  `NECTF{TH1$_1$_Y0UR_GO0D_C@K3}`

</details>