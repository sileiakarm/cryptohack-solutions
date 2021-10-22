from PIL import Image

lemur = Image.open("lemur.png")
flag = Image.open("flag.png")

lemur_pix = lemur.load()
flag_pix = flag.load()

for i in range(lemur.size[0]): # for every pixel:
    for j in range(lemur.size[1]):
        l = lemur_pix[i,j]
        f = flag_pix[i,j]

        # XOR each part of the pixel tuple
        r = l[0] ^ f[0]
        g = l[1] ^ f[1]
        b = l[2] ^ f[2]

        # Store the resulatant tuple back into an image
        flag_pix[i,j] = (r, g, b)

flag.save("lemur_xor_result.png")
