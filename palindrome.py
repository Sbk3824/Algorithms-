def checkPalindrome(num):
	n = num
	rev = 0

	while num > 0:
		dig = num % 10
		rev = rev * 10 + dig
		num = num // 10

	if n == num:
		print("Palindrome")
	else:
		print("Not a Palindrome")

	checkPalindrome(121)
	checkPalindrome(123)


