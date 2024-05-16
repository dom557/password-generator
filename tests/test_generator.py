import string
import unittest
from generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
  """
  Unit tests for the password generator function.
  """

  def test_generate_password_valid(self):
    """
    Tests generating password with valid parameters.
    """
    password = generate_password(10)
    self.assertIsInstance(password, str)
    self.assertEqual(len(password), 10)

  def test_generate_password_all_types(self):
    """
    Tests generating password with all character types included.
    """
    password = generate_password(12, True, True, True, True)
    self.assertAnyCharIn(password, string.ascii_uppercase)
    self.assertAnyCharIn(password, string.ascii_lowercase)
    self.assertAnyCharIn(password, string.digits)
    self.assertAnyCharIn(password, string.punctuation)

  def test_generate_password_no_types(self):
    """
    Tests error handling for no character types selected.
    """
    with self.assertRaises(ValueError) as error:
      generate_password(10, False, False, False, False)
    self.assertEqual(str(error.exception), "Error: Please select at least one character type.")

  def test_generate_password_invalid_length(self):
    """
    Tests error handling for invalid password length.
    """
    with self.assertRaises(ValueError) as error:
      generate_password(0)
    self.assertEqual(str(error.exception), "Error: Password length must be at least 1 character.")

  # Helper functions for character checks in password
  def assertAnyCharIn(self, password, char_set):
    for char in password:
      if char in char_set:
        return
    self.fail(f"Password does not contain any characters from {char_set}")

if __name__ == '__main__':
  unittest.main()
