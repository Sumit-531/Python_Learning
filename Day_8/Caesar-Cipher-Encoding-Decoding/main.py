from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(user_text, user_shift_amount, user_direction):
  cipher_text = ""
  plain_text = ""
  for char in user_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position_encode = position + user_shift_amount
      new_position_decode = position - user_shift_amount
      cipher_text += alphabet[new_position_encode]
      plain_text += alphabet[new_position_decode]
    else:
      cipher_text += char
      plain_text += char

  if user_direction == "encode":
    print(f"The encoded text is {cipher_text}")
  elif user_direction == "decode":
    print(f"The decoded text is {plain_text}")

print(logo)
should_continue = False
while not should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  ceasar(user_text = text, user_shift_amount = shift, user_direction  = direction)
  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if result == "yes":
    should_continue = False
  elif result == "no":
    should_continue = True
  else:
    print("Invalid input")
