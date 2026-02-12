const users = [{name: 'A', age: 25}, {name: 'B', age: 15}], return an array of names for users over 18
const l=users.filter(a=>a.age>18).map(n=>n.name)
