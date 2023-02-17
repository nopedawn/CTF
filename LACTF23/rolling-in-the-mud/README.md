## crypto/rolling-in-the-mud

<details>
	<summary>Description</summary>
  
  > uugh, these pigs in my pen are making a complete mess! They're rolling all over the place! <br>
  > Anyway, can you decode this cipher they gave me, almost throwing it at me while rolling around? <br>
  > Answer in lowercase with symbols. In the image, { and } are characters that should appear in your flag, and replace spaces with `_`. <br> [cipher.ong](./cipher.png)
</details>

We're given an image, this image looks like the pigpen cipher, but after we decode it with [dcode.fr](https://www.dcode.fr/pigpen-cipher) the result it's not make sense

<image src="./cipher.png" width="500px">

```
EOMB MC VCAL 
EBU PAUNT 
CNAPPPJ FNI 
CNAPPPJ FNI 
CNAPPPJ DUGIP
```

By the challenge name and description `rolling`, we can assumed to flipped the image horizontally 180 degrees, and get perfect results then wrap it to make it lowercase

<image src="./cipher-flipped.png" width="500px">
  
```
LACTF ROLLING
AND ROLLING
AND ROLLING
UNTIL THE
PIGS GO HOME
```

<details>
  <summary>FLAG</summary>
  
  > `lactf{rolling_and_rolling_and_rolling_until_the_pigs_go_home}`

</details>
