# Unicode-Byte-Extractor-for-Hashcat
This Python script takes a Unicode input string, converts it into two sets of hexadecimal representations (byte1 and byte2), removes duplicate bytes from each set, and presents the unique byte1 and byte2 values as separate outputs.

# How to Use

1. Clone the repository or download the script.

```bash
git clone https://github.com/Nielymmah/Unicode-Byte-Extractor-for-Hashcat.git
```
2. Specify your Unicode (Foreign Language Characters) input string inside the quotation marks:

```python
# Input Unicode string
unicode_string = "é¢¡£¤¥¦§¨©ª«¬­®¯°±²³´µ¶¹¸º»¼½¾¿ÀÁÂÃÄ×£"
```

3. Run the script with your Unicode input string.

```bash
python Uni2Hex.py
```

4. Copy the generated unique byte1 and byte2 values in your hashcat command.

Example:

```bash
hashcat.exe -m 0 md5.hash -a 3 -1 "byte1" -2 "byte2" -3 ?1?2 --hex-charset 'ikn?3w?3myk?3y!' -o SolvedMD5.txt
```

This is the full command for attacking an MD5 hash that includes Unicode characters in the password. 
We define and use Masks -1 and -2, which are combined into -3 for simplicity. 
It's important to understand that this command is specifically designed for Mask attacks, 
offering the choice of using either Brute-force (-a 3) or Hybrid modes (-a 6/7) exclusively.

Best of luck with your password cracking endeavors! If you found this script helpful and it worked as intended, we'd greatly appreciate your support by giving it a star or a thumbs up on GitHub. Happy Cr4ck1ng!
