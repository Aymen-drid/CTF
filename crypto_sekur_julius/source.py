def decrypt_caesar_repeated(ciphertext, original_shift_key):
    # Calculate the effective shift from repeating the key 1337 times
    effective_shift = original_shift_key; 
    
    # Decrypt by shifting each letter backwards by the effective shift
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            shifted = ord(char) - effective_shift
            if char.isupper():
                decrypted_text.append(chr((shifted - ord('A')) % 26 + ord('A')))
            # else:
            #     decrypted_text.append(chr((shifted - ord('a')) % 26 + ord('a')))
        elif char=='0':
            decrypted_text.append(' ')
        else:
            decrypted_text.append(char)  # Non-alphabetic characters remain the same

    return ''.join(decrypted_text)

# Example usage
ciphertext =  "LTARDBT0ID0WPRZIWTQDD0ILDIWDJHPCSILTCINUDJG!0IWXH0XH0P0EGDDU0DU0RDCRTEI0ID0EGDKT0NDJ0IWPI0IWT0RPTHPG0RXEWTG0XH0XCHTRJGT0CD0BPIITG0WDL0BPCN0IXBTH0NDJ0PEEAN0XI.0IWT0HTRJGXIN0DU0P0IWDJHPCS0SXHIXCRI0HWXUIH0XH0TKTCIJPAAN0IWT0HPBT0PH0IWPI0DU0P0HXCVAT0HWXUI.0TCDJVW0BJBQAXCV,0IPZT0NDJG0UAPV0PCS0TCYDN0IWT0GTHI0DU0IWT0RDCITHI.0BPZT0HJGT0NDJ0LGPE0IWT0UDAADLXCV0ITMI0LXIW0IWT0WIQ0UAPV0UDGBPI0HTRJGXINDUPIWDJHPCSDGHTRJGXINDUPHXCVAT.";
for i in range(26):
    original_shift_key = i;  # Example shift key
    decrypted_text = decrypt_caesar_repeated(ciphertext, original_shift_key)
    print("Decrypted Text:", decrypted_text)
