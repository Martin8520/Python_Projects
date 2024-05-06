def restoreIpAddresses(s):
    def backtrack(start, parts):
        if parts == 4 and start == len(s):
            result.append(".".join(address))
            return

        if parts == 4 or start == len(s):
            return

        for length in range(1, 4):
            if start + length <= len(s) and (length == 1 or s[start] != '0'):
                part = s[start:start + length]
                if 0 <= int(part) <= 255:
                    address.append(part)
                    backtrack(start + length, parts + 1)
                    address.pop()

    result = []
    address = []
    backtrack(0, 0)
    return result


print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("0000"))
print(restoreIpAddresses("101023"))
