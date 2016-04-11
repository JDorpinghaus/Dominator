var Nightmare = require('nightmare');
var nightmare = Nightmare({ show: true })
var secrets = require('./secret.json');

nightmare
  .goto('http://game.hackdfw.com/login')
  .wait('.email')
	.insert(".email", secrets.username)
	.insert(".pass", secrets.password)
	.click("button[data-reactid='.0.0.0.0.0.5'")
	.wait("span[data-reactid='.0.0.0.0.0.1.1.0.2.0.2.2'")
	.click("a[data-reactid='.0.0.0.0.0.1.0.2.1.0'")
	.wait("h1[data-reactid='.0.0.0.0.0.1.1.0.4'")
	.click("b[data-reactid='.0.0.0.0.0.1.1.0.7.0:$caesar.0'")
	.wait(10000)
  .evaluate(function () {
    return document.querySelector('#main .searchCenterMiddle li a').href
  })
  .end()
  .then(function (result) {
    console.log(result)
  })