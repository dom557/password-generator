import random
import string

def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True):
  """
  Generates a random password based on specified criteria.

  Args:
      length (int): Desired length of the password.
      include_uppercase (bool, optional): Include uppercase letters (default: True).
      include_lowercase (bool, optional): Include lowercase letters (default: True).
      include_digits (bool, optional): Include digits (default: True).
      include_special_chars (bool, optional): Include special characters (default: True).

  Returns:
      str: The generated password or an error message if no character type is selected.

  Raises:
      ValueError: If the provided password length is less than 1.
  """

  chars = ''
  char_sets = []
  if include_uppercase:
    char_sets.append(string.ascii_uppercase)
  if include_lowercase:
    char_sets.append(string.ascii_lowercase)
  if include_digits:
    char_sets.append(string.digits)
  if include_special_chars:
    char_sets.append(string.punctuation)

  if not char_sets:
    raise ValueError("Error: Please select at least one character type.")

  chars = ''.join(char_sets)  # Combine all selected character sets

  if length < 1:
    raise ValueError("Error: Password length must be at least 1 character.")

  password = ''.join(random.choice(chars) for _ in range(length))
  return password
