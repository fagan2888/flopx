
/*BEGIN replace this code with the javascript you want the client to execute*/

var arr = [67,13,42,20,85,18,51,29,58,22,33,14,67,92,45,82,77]
arr.sort()
var ans = (arr)

/*END replace*/


var xhttp = new XMLHttpRequest()
/*console.log(ans)*/
xhttp.open("POST", "/verify", true)
xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
xhttp.send(JSON.stringify({ "answer": ans}))
