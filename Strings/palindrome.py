def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s_ = "".join(c for c in s if c.isalnum())
    s_ = s_.lower()
    # print(s_)

    i, j = 0, len(s_) - 1
    while i < j or i == j:
        if s_[i] != s_[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    s1 = "race a car"
    print(isPalindrome(s1))

    s2 = " "
    print(isPalindrome(s2))

    s3 = "A man, a plan, a canal: Panama"
    print(isPalindrome(s3))

