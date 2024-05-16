from generator import generate_password
import argparse  # for handling command-line arguments

def main():
  # Parse command-line arguments for password length and character types (optional)
  parser = argparse.ArgumentParser(description="Generate a random password")
  parser.add_argument("length", type=int, nargs="?", default=10, help="Desired password length (default: 10)")
  parser.add_argument("-u", "--uppercase", action="store_true", help="Include uppercase letters")
  parser.add_argument("-l", "--lowercase", action="store_true", help="Include lowercase letters")
  parser.add_argument("-d", "--digits", action="store_true", help="Include digits")
  parser.add_argument("-s", "--special", action="store_true", help="Include special characters")
  args = parser.parse_args()

  # Generate password based on arguments
  password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special)
  if not any([args.uppercase, args.lowercase, args.digits, args.special]):
    args.lowercase = True  # Set lowercase as default if none chosen
  # Display the generated password
  print(f"Your generated password: {password}")

if __name__ == "__main__":
  main()
