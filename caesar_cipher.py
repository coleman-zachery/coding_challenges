# Write a program that can reverse the caesar cipher of the following encoded message.
# "Wylkpjapvu pz clyf kpmmpjbsa, lzwljphssf hivba aol mbabyl. ― Uplsz Ivoy"
# The program will only shift letters and numbers, and preserve the case of the letter.

message = "Wylkpjapvu pz clyf kpmmpjbsa, lzwljphssf hivba aol mbabyl. ― Uplsz Ivoy"

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
digit = "0123456789"

def cipher (string_in, shift_n):
  string_out = ""
  for i in string_in:
    if i in UPPER:
      string_out += UPPER[(ord(i)+shift_n-ord("A"))%26]
    elif i in lower:
      string_out += lower[(ord(i)+shift_n-ord("a"))%26]
    elif i in digit:
      string_out += digit[(ord(i)+shift_n-ord("0"))%10]
    else:
      string_out += i
  return string_out

for j in range(26):
  if (j-26 == -7 or j-26 == -6):
    print("\n")
  print(j-26, cipher(message, j-26))

# The solution is that the encoded message used a shift of 7.