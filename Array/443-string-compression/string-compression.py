class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            start = read

            while read < len(chars) and chars[read] == chars[start]:
                read+=1
            count = read-start

            chars[write] = chars[start]

            write+=1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write+=1
        
        return write