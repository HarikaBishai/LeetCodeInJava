class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return chars
        
        read = chars[0]
        count = 0
        idx = 0

        for i in range(len(chars)):
            c = chars[i]
            if read!=c:
                chars[idx] = read
                idx+=1
                if count > 1:
                    s_count = str(count)
                    chars[idx: idx + len(s_count)] = s_count
                    idx+=len(s_count)
                count = 1
                read = c
            else:
                count+=1
        chars[idx] = read
        idx+=1
        if count > 1:
            s_count = str(count)
            chars[idx: idx + len(s_count)] = s_count
            idx+=len(s_count)
        return idx

        