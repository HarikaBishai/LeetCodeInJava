/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    
    const ROWS = grid.length;
    const COLS = grid[0].length;
    const visited = new Set();
    const dirs = [[-1,0], [1,0], [0,1], [0,-1]];
    function dfs(r, c){
        visited.add(`${r} ${c}`);

        for(let dir of dirs) {
            let newr = dir[0] + r;
            let newc = dir[1] + c;
            if(newr<ROWS && newr >= 0 && newc<COLS && newc>=0 && grid[newr][newc] == "1" && !visited.has(`${newr} ${newc}`)) {
                dfs(newr, newc);
            }
        }
    }

    let islands = 0;

    for(let i=0;i<ROWS;i++) {
        for(let j=0; j<COLS;j++) {
            if(grid[i][j] === "1" &&!visited.has(`${i} ${j}`)) {
                dfs(i, j);
                islands++;
            }
        }
    }
    return islands;

};