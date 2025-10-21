class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            start = read

            while read < len(chars) and chars[start] == chars[read]:
                read+=1
            count = read - start

            chars[write] = chars[start]
            write+=1
            if count > 1:
                s_count = str(count)
                chars[write: write+len(s_count)] = s_count
                write+= len(s_count)
        return write