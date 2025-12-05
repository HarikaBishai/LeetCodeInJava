function groupAnagrams(strs: string[]): string[][] {
    const groups = {}



    for(let str of strs) {
        const sorted = str.split("").sort().join("");
        (groups[sorted]??=[]).push(str);
    }
    return Object.values(groups);
};