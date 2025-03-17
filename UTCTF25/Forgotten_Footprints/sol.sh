strings disk.img \
    | grep -E '.{100,}' \
    | xxd -r -p \
    | grep -a -oE 'utflag\{[^}]+\}'