/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    

    function match(i,j) {
        if(j === p.length) {
            return i === s.length;
        }

        const firstMatch = i< s.length && (s[i] === p[j] || p[j] == '.');

        if(j+1 < p.length && p[j+1] == '*') {
            return match(i, j+2) || firstMatch && match(i+1, j);
        }

        return firstMatch && match(i+1, j+1);
    }
    return match(0,0);
};