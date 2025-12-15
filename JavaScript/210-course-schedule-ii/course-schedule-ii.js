/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */


var findOrder = function(numCourses, prerequisites) {
    const result = []

    let graph = new Map();
    let indegree = new Map();


    for(let i=0;i<numCourses; i++) {
        indegree.set(i, 0);
        graph.set(i, []);
    }

    for(let req of prerequisites) {
        let v = req[0];
        let u = req[1];    
        graph.get(u).push(v);
        indegree.set(v, (indegree.get(v) || 0)+1);

    }

    let q = [];
    let front = 0


    for(let key of indegree.keys()) {
        if(indegree.get(key) === 0) {
            q.push(key);
        }
    }
    

    while(front != q.length) {
        const node = q[front++]
        result.push(node)
        if(graph.has(node)) {
            for(let nei of graph.get(node)) {
                indegree.set(nei, (indegree.get(nei) || 0)-1);
                if(indegree.get(nei) === 0) {
                    q.push(nei)
                }
            }
        }
    }

    return result.length === numCourses ? result : [];
};