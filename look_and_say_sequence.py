# Write a program that is able to generate the next term by describing the previouis term.
# 1
# 11
# 21
# 1211
# 111221
# 312211
# The program should also be able to calculate the length of the 40th and 50th term.

def look_and_say(string_in):
  string_out = ""
  flag = [0, ""]
  for i in range(len(string_in)):
    if flag[1] == string_in[i]:
      flag[0] += 1
    else:
      string_out += str(flag[0]) + flag[1]
      flag = [1, string_in[i]]
  return (string_out + str(flag[0]) + flag[1])[1:]

# if string lenth is greater than 99, display length as "#length" instead of displaying the sequence

my_string = "1"; print(0, my_string)
for j in range(50):
  my_string = look_and_say(my_string)
  if len(my_string) > 99:
    print(j+1, f"#{len(my_string)}")
  else:
    print(j+1, my_string)