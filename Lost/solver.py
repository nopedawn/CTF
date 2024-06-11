from Crypto.Util.number import long_to_bytes

# Given values
n = 5113166966960118603250666870544315753374750136060769465485822149528706374700934720443689630473991177661169179462100732951725871457633686010946951736764639
c = 329402637167950119278220170950190680807120980712143610290182242567212843996710001488280098771626903975534140478814872389359418514658167263670496584963653
cor_m = 724154397787031699242933363312913323086319394176220093419616667612889538090840511507392245976984201647543870740055095781645802588721

# Calculate the square of cor_m
cor_m_square = pow(cor_m, 2, n)

# Since m^2 = c and (m - x)^2 = cor_m^2 for some small x, we can say that c - cor_m^2 = 2*m*x - x^2 = k (mod n)
# k is a small number because x is small, so we can simply calculate it by brute force
k = (c - cor_m_square) % n
for x in range(2**160):
    m_square = (cor_m_square + 2*cor_m*x - x*x) % n
    if m_square == c:
        m = (cor_m + x) % n
        break

# Convert the message from number to bytes
flag = long_to_bytes(m)
print(flag)
