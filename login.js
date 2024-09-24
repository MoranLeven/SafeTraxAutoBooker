const cryptoJS = require('crypto-js')
let digest =(message)=> cryptoJS.MD5(message).toString()

let generateHash = function(username,password){
    return digest( `${username}:safetraxOpentxt:${password}:${generateCnonce()}`)
}
let generateCnonce = function(){
    return digest(`${Date.now()}:safetraxOpentxt`)
}



console.log(`ha1 ===> ${generateHash('username','password')}`)
console.log(`Canone = ${generateCnonce()}`)
