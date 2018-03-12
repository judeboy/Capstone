 var json = require('./govProgs.json')

let obj = {}
for (let i of json){
  let agency = i.AgencyShort
  !obj[agency] ? obj[agency] = 1 : obj[agency] += 1
}
// console.log(obj);

let HHSObj = {}
for (let i of json){
  if (i.AgencyShort === "HHS"){
    HHSObj[i.AgencyShort] += i.ProgTitle
  }
}
// console.log(HHSObj);

var pairs = Object.keys(obj).map(key => [key, obj[key]])
let sorted = pairs.sort((a, b) => b[1] - a[1])
// console.log(sorted.slice(0, 4))
var result = sorted.slice(0, 5).reduce((a, b) => {
  a[b[0]] = b[1]
  return a
})
// console.log(result)
