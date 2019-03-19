const Discord = require('discord.js');

var client = new Discord.Client();
var bot = new Discord.Client();
client.login("NDczODIwNzcyMzczMzY0NzM3.D2j-UQ.5zH92ROdlYAQYH9iIq9_lkh7Beg", output);
bot.login(process.env.TOKEN, output);
var hqchannels = ['554988471236952064' , '553828853026652160' , '553828988007743489' , '553829751073013761' , '553829811303481347' , '554991756551389196','557439769106448406'];
var cschannels = ['554988471236952064' , '553828853026652160' , '553828988007743489' , '553829751073013761', '553829811303481347', '554991756551389196','557439829218951168'];
var jrchannels = ['554988471236952064' , '553828853026652160' , '553828988007743489' , '553829751073013761' , '553829811303481347', '554991756551389196'];
var outputchannel1 = '557529513278570496';
var outputchannel2 = '549970564782096404';
var outputchannel3 = '555677057808334859';



bot.on("message", async message =>{
  let messageArray = message.content.split(" ");
  let cmd = messageArray[0];
  let prefix = ".";
  let cont = message.content.slice(prefix.length).split(" ");
  let args = cont.slice(1);

  
  

  if (cmd == ".say") {
    message.delete();
    if (!message.member.roles.has("553983197378117635")) return message.channel.send("You need server helpers Role to use this command").then(msg=> msg.delete(15000))
    let msgToSend = message.content.slice(4);
    if (!msgToSend) return;
    let EmbedMsg = new Discord.RichEmbed()
                      .setColor("BLUE")
                      .setDescription(`**${msgToSend}**`)

    message.channel.send(msgToSend);
  }
});



bot.on("ready", () => {
    // This event will run if the bot starts, and logs in, successfully.
    
    // Example of changing the bot's playing game to something useful. `client.user` is what the
    // docs refer to as the "ClientUser".
    bot.user.setActivity(`Playing Trivia`);
  });

function output(error, token) {
        if (error) {
                console.log(`There was an error logging in: ${error}`);
                return;
        } else
                console.log(`Logged in. Token: ${token}`);


                
}

'use strict';
var _0xf92e = ["match", "length", "message", "content", "channel", "includes", "startsWith", "replace", "string", "constructor", "while (true) {}", "debu", "gger", "call", "action", "stateObject", "apply", "function *\\( *\\)", "\\+\\+ *(?:_0x(?:[a-f0-9]){4,6}|(?:\\b|\\d)[a-z0-9]{1,4}(?:\\b|\\d))", "init", "test", "chain", "input", "channels", "get", "send", "NirwanArmy", "__GETTING ANSWER for Loco__", "Invented by ❤️ For NirwanArmy😉", "https://d1qb2nb5cznatu.cloudfront.net/startups/i/5274316-530c7a78919c46dc771716ab8f4ff97a-medium_jpg.jpg?buster=1517748075", 
"**ANSWER 2**", "**ANSWER 3**", "__Answering for BaaziNow__", "**ANSWER 1**", "__Answering for Swoo__", "fetchMessages", "user", "then", "first", "edit", "log", "Time is up!", "lastMessage", "shift", "push", "0x0", "0x1", "0x2", "i", "0x3", "0x5", "0x4", "0x6", "0", "0xa", "0xb", "0xc", "0xd", "0xe", "0xf", "0x9", "0x8", "0x7", "0x10", "0x11", "0x12", "0x16", "0x17", "0x15", "id", "0x14", "0x13", "0x19", "0x18", "0x1a", "0x1c", "0x1b", "0x1d", "0x1e", "0x1f", 
"1", "0x20", "2", "3", "on", "-", "0x21", "", "0x22", "lo", "bb", "sw", "0x23", "counter", "0x25", "0x24", "0x29", "0x28", "0x26", "0x27", "0x2a"];
var _0xab0c = [_0xf92e[0], _0xf92e[1], _0xf92e[2], _0xf92e[3], _0xf92e[4], _0xf92e[5], _0xf92e[6], _0xf92e[7], _0xf92e[8], _0xf92e[9], _0xf92e[10], _0xf92e[11], _0xf92e[12], _0xf92e[13], _0xf92e[14], _0xf92e[15], _0xf92e[16], _0xf92e[17], _0xf92e[18], _0xf92e[19], _0xf92e[20], _0xf92e[21], _0xf92e[22], _0xf92e[23], _0xf92e[24], _0xf92e[25], _0xf92e[26], _0xf92e[27], _0xf92e[28], _0xf92e[29], _0xf92e[30], _0xf92e[31], _0xf92e[32], _0xf92e[33], _0xf92e[34], _0xf92e[35], _0xf92e[36], _0xf92e[37], _0xf92e[38], 
_0xf92e[39], _0xf92e[40], _0xf92e[41], _0xf92e[42], _0xf92e[43], _0xf92e[44], _0xf92e[45], _0xf92e[46], _0xf92e[47], _0xf92e[48], _0xf92e[49], _0xf92e[50], _0xf92e[51], _0xf92e[52], _0xf92e[53], _0xf92e[54], _0xf92e[55], _0xf92e[56], _0xf92e[57], _0xf92e[58], _0xf92e[59], _0xf92e[60], _0xf92e[61], _0xf92e[62], _0xf92e[63], _0xf92e[64], _0xf92e[65], _0xf92e[66], _0xf92e[67], _0xf92e[68], _0xf92e[69], _0xf92e[70], _0xf92e[71], _0xf92e[72], _0xf92e[73], _0xf92e[74], _0xf92e[75], _0xf92e[76], _0xf92e[77], 
_0xf92e[78], _0xf92e[79], _0xf92e[80], _0xf92e[81], _0xf92e[82], _0xf92e[83], _0xf92e[84], _0xf92e[85], _0xf92e[86], _0xf92e[87], _0xf92e[88], _0xf92e[89], _0xf92e[90], _0xf92e[91], _0xf92e[92], _0xf92e[93], _0xf92e[94], _0xf92e[95], _0xf92e[96], _0xf92e[97], _0xf92e[98], _0xf92e[99], _0xf92e[100]];
var _0x2877 = [_0xab0c[0], _0xab0c[1], _0xab0c[2], _0xab0c[3], _0xab0c[4], _0xab0c[5], _0xab0c[6], _0xab0c[7], _0xab0c[8], _0xab0c[9], _0xab0c[10], _0xab0c[11], _0xab0c[12], _0xab0c[13], _0xab0c[14], _0xab0c[15], _0xab0c[16], _0xab0c[17], _0xab0c[18], _0xab0c[19], _0xab0c[20], _0xab0c[21], _0xab0c[22], _0xab0c[23], _0xab0c[24], _0xab0c[25], _0xab0c[26], _0xab0c[27], _0xab0c[28], _0xab0c[29], _0xab0c[30], _0xab0c[31], _0xab0c[32], _0xab0c[33], _0xab0c[34], _0xab0c[35], _0xab0c[36], _0xab0c[37], _0xab0c[38], 
_0xab0c[39], _0xab0c[40], _0xab0c[41], _0xab0c[42]];
(function(_0x30c5x3$jscomp$0, _0x30c5x4$jscomp$0) {
var _0x30c5x5$jscomp$0 = function(_0x30c5x6$jscomp$0) {
for (; --_0x30c5x6$jscomp$0;) {
_0x30c5x3$jscomp$0[_0xab0c[44]](_0x30c5x3$jscomp$0[_0xab0c[43]]());
}
};
_0x30c5x5$jscomp$0(++_0x30c5x4$jscomp$0);
})(_0x2877, 231);
var _0x3934 = function(_0x30c5x8$jscomp$0, _0x30c5x9$jscomp$0) {
_0x30c5x8$jscomp$0 = _0x30c5x8$jscomp$0 - 0;
var _0x30c5xa$jscomp$0 = _0x2877[_0x30c5x8$jscomp$0];
return _0x30c5xa$jscomp$0;
};
var _0x4ceb34 = function() {
var _0x30c5xc$jscomp$0 = !![];
return function(_0x30c5xd$jscomp$0, _0x30c5xe$jscomp$0) {
var _0x30c5xf$jscomp$0 = _0x30c5xc$jscomp$0 ? function() {
if (_0x30c5xe$jscomp$0) {
var _0x30c5x10$jscomp$0 = _0x30c5xe$jscomp$0[_0x3934(_0xab0c[45])](_0x30c5xd$jscomp$0, arguments);
_0x30c5xe$jscomp$0 = null;
return _0x30c5x10$jscomp$0;
}
} : function() {
};
_0x30c5xc$jscomp$0 = ![];
return _0x30c5xf$jscomp$0;
};
}();
(function() {
_0x4ceb34(this, function() {
var _0x30c5x11$jscomp$0 = new RegExp(_0x3934(_0xab0c[46]));
var _0x30c5x12$jscomp$0 = new RegExp(_0x3934(_0xab0c[47]), _0xab0c[48]);
var _0x30c5x13$jscomp$0 = _0x3ed473(_0x3934(_0xab0c[49]));
if (!_0x30c5x11$jscomp$0[_0x3934(_0xab0c[51])](_0x30c5x13$jscomp$0 + _0x3934(_0xab0c[50])) || !_0x30c5x12$jscomp$0[_0x3934(_0xab0c[51])](_0x30c5x13$jscomp$0 + _0x3934(_0xab0c[52]))) {
_0x30c5x13$jscomp$0(_0xab0c[53]);
} else {
_0x3ed473();
}
})();
})();
var count1hq = 0;
var count2hq = 0;
var count3hq = 0;
var count1cs = 0;
var count2cs = 0;
var count3cs = 0;
var count1jr = 0;
var count2jr = 0;
var count3jr = 0;
var gamestartedhq;
var gamestartedcs;
var gamestartedjr;
var updatecount = 0;
function inithq() {
bot[_0x3934(_0xab0c[62])][_0x3934(_0xab0c[61])](outputchannel1)[_0x3934(_0xab0c[60])]({
"embed" : {
"title" : _0x3934(_0xab0c[54]),
"description" : _0x3934(_0xab0c[55]),
"color" : 11944542,
"footer" : {
"text" : _0x3934(_0xab0c[56])
},
"thumbnail" : {
"url" : 'https://pbs.twimg.com/profile_images/854148360395259904/ASB8BCxv_400x400.jpg'
},
"fields" : [{
"name" : _0xab0c[33],
"value" : count1hq*75/500*100 
}, {
"name" : _0x3934(_0xab0c[58]),
"value" : count2hq*75/500*100 
}, {
"name" : _0x3934(_0xab0c[59]),
"value" : count3hq*75/500*100 
}]
}
})
.then(function (message) {
        message.react("❌")
        message.react("✅")
             
    
              });


}
function initcs() {
bot[_0x3934(_0xab0c[62])][_0x3934(_0xab0c[61])](outputchannel2)[_0x3934(_0xab0c[60])]({
"embed" : {
"title" : _0xab0c[26],
"description" : _0x3934(_0xab0c[63]),
"color" : Math.floor((Math.random() * 160000) + 1),
"footer" : {
"text" : _0x3934(_0xab0c[56])
},
"thumbnail" : {
"url" : 'https://pbs.twimg.com/profile_images/854148360395259904/ASB8BCxv_400x400.jpg'
},
"fields" : [{
"name" : _0x3934(_0xab0c[64]),
"value" : count1cs*75/500*100 
}, {
"name" : _0x3934(_0xab0c[58]),
"value" : count2cs*75/500*100 
}, {
"name" : _0x3934(_0xab0c[59]),
"value" : count3cs*75/500*100 
}]
}
}).then(function (message) {
        message.react("❌")
        message.react("✅")
             
    
              });
}
function initjr() {
bot[_0x3934(_0xab0c[62])][_0x3934(_0xab0c[61])](outputchannel3)[_0x3934(_0xab0c[60])]({
"embed" : {
"title" : _0x3934(_0xab0c[54]),
"description" : _0x3934(_0xab0c[65]),
"color" : Math.floor((Math.random() * 160000) + 1),
"footer" : {
"text" : _0x3934(_0xab0c[56])
},
"thumbnail" : {
"url" : 'https://pbs.twimg.com/profile_images/854148360395259904/ASB8BCxv_400x400.jpg'
},
"fields" : [{
"name" : _0x3934(_0xab0c[64]),
"value" : count1jr*75/500*100 
}, {
"name" : _0x3934(_0xab0c[58]),
"value" : count2jr*75/500*100 
}, {
"name" : _0x3934(_0xab0c[59]),
"value" : count3jr*75/500*100 
}]
}
}).then(function (message) {
        message.react("❌")
        message.react("✅")
             
    
              });
}
function updatehq() {
updatecount++;
bot[_0xab0c[23]][_0x3934(_0xab0c[61])](outputchannel1)[_0x3934(_0xab0c[71])]({
"around" : bot[_0x3934(_0xab0c[70])][_0xab0c[42]][_0xab0c[69]],
"limit" : 1
})[_0x3934(_0xab0c[68])]((_0x30c5x25$jscomp$0) => {
var _0x30c5x26$jscomp$0 = _0x30c5x25$jscomp$0[_0x3934(_0xab0c[66])]();
_0x30c5x26$jscomp$0[_0x3934(_0xab0c[67])]({
"embed" : {
"title" : _0x3934(_0xab0c[54]),
"description" : _0x3934(_0xab0c[55]),
"color" : Math.floor((Math.random() * 160000) + 1),
"footer" : {
"text" : _0x3934(_0xab0c[56])
},
"thumbnail" : {
"url" : 'https://pbs.twimg.com/profile_images/854148360395259904/ASB8BCxv_400x400.jpg'
},
"fields" : [{
"name" : _0xab0c[33],
"value" : count1hq*75/500*100 + '%'
}, {
"name" : _0x3934(_0xab0c[58]),
"value" : count2hq*75/500*100 + '%'
}, {
"name" : _0xab0c[31],
"value" : count3hq*75/500*100 + '%'
}]
}
});
});
if (updatecount < 11) {
setTimeout(function() {
updatehq();
}, 1E3);
} else {
console[_0x3934(_0xab0c[73])](_0x3934(_0xab0c[72]));
}
}
function updatecs() {
updatecount++;
bot[_0x3934(_0xab0c[62])][_0x3934(_0xab0c[61])](outputchannel2)[_0x3934(_0xab0c[71])]({
"around" : bot[_0xab0c[36]][_0x3934(_0xab0c[74])][_0xab0c[69]],
"limit" : 1
})[_0x3934(_0xab0c[68])]((_0x30c5x28$jscomp$0) => {
var _0x30c5x29$jscomp$0 = _0x30c5x28$jscomp$0[_0x3934(_0xab0c[66])]();
_0x30c5x29$jscomp$0[_0xab0c[39]]({
"embed" : {
"title" : _0x3934(_0xab0c[54]),
"description" : _0x3934(_0xab0c[63]),
"color" : 11944542,
"footer" : {
"text" : _0x3934(_0xab0c[56])
},
"thumbnail" : {
"url" : 'https://pbs.twimg.com/profile_images/854148360395259904/ASB8BCxv_400x400.jpg'
},
"fields" : [{
"name" : _0x3934(_0xab0c[64]),
"value" : count1cs*75/500*100 + '%'
}, {
"name" : _0x3934(_0xab0c[58]),
"value" : count2cs*75/500*100 + '%'
}, {
"name" : _0x3934(_0xab0c[59]),
"value" : count3cs*75/500*100 + '%'
}]
}
});
});
if (updatecount < 11) {
setTimeout(function() {
updatecs();
}, 1E3);
} else {
console[_0x3934(_0xab0c[73])](_0xab0c[41]);
}
}
function updatejr() {
updatecount++;
bot[_0x3934(_0xab0c[62])][_0x3934(_0xab0c[61])](outputchannel3)[_0x3934(_0xab0c[71])]({
"around" : bot[_0xab0c[36]][_0x3934(_0xab0c[74])][_0xab0c[69]],
"limit" : 1
})[_0xab0c[37]]((_0x30c5x2b$jscomp$0) => {
var _0x30c5x2c$jscomp$0 = _0x30c5x2b$jscomp$0[_0x3934(_0xab0c[66])]();
_0x30c5x2c$jscomp$0[_0x3934(_0xab0c[67])]({
"embed" : {
"title" : _0x3934(_0xab0c[54]),
"description" : _0x3934(_0xab0c[65]),
"color" : 11944542,
"footer" : {
"text" : _0x3934(_0xab0c[56])
},
"thumbnail" : {
"url" : 'https://pbs.twimg.com/profile_images/854148360395259904/ASB8BCxv_400x400.jpg'
},
"fields" : [{
"name" : _0x3934(_0xab0c[64]),
"value" : count1jr*75/500*100 + '%'
}, {
"name" : _0x3934(_0xab0c[58]),
"value" : count2jr*75/500*100 + '%'
}, {
"name" : _0x3934(_0xab0c[59]),
"value" : count3jr*75/500*100 + '%'
}]
}
});
});
if (updatecount < 11) {
setTimeout(function() {
updatejr();
}, 500);
} else {
console[_0x3934(_0xab0c[73])](_0xab0c[41]);
}
}
function characterTest(_0x30c5x2e$jscomp$0) {
return (_0x30c5x2e$jscomp$0[_0x3934(_0xab0c[76])](/[abcdefghijklmnopqrstuvxyz]/gi) || [])[_0x3934(_0xab0c[75])];
}
client[_0xab0c[84]](_0x3934(_0xab0c[77]), function(_0x30c5x2f$jscomp$0) {
if (characterTest(_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])]) != 0) {
return;
}
if (gamestartedhq == !![]) {
if (hqchannels[_0xab0c[5]](_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[79])][_0xab0c[69]])) {
if (_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])][_0x3934(_0xab0c[81])](_0xab0c[80])) {
count1hq++;
if (count1hq > 40) {
gamestaredhq = ![];
}
} else {
if (_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])][_0xab0c[5]](_0xab0c[82])) {
count2hq++;
if (count2hq > 40) {
gamestaredhq = ![];
}
} else {
if (_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])][_0x3934(_0xab0c[81])](_0xab0c[83])) {
count3hq++;
if (count3hq > 40) {
gamestaredhq = ![];
}
}
}
}
}
}
if (gamestartedcs == !![]) {
if (cschannels[_0xab0c[5]](_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[79])][_0xab0c[69]])) {
if (_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])][_0x3934(_0xab0c[81])](_0xab0c[80])) {
count1cs++;
if (count1cs > 40) {
gamestaredcs = ![];
}
} else {
if (_0x30c5x2f$jscomp$0[_0xab0c[3]][_0x3934(_0xab0c[81])](_0xab0c[82])) {
count2cs++;
if (count2cs > 40) {
gamestaredcs = ![];
}
} else {
if (_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])][_0x3934(_0xab0c[81])](_0xab0c[83])) {
count3cs++;
if (count3cs > 40) {
gamestaredcs = ![];
}
}
}
}
}
}
if (gamestartedjr == !![]) {
if (jrchannels[_0xab0c[5]](_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[79])][_0xab0c[69]])) {
if (_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])][_0xab0c[5]](_0xab0c[80])) {
count1jr++;
if (count1jr > 40) {
gamestaredjr = ![];
}
} else {
if (_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])][_0x3934(_0xab0c[81])](_0xab0c[82])) {
count2jr++;
if (count2jr > 40) {
gamestaredjr = ![];
}
} else {
if (_0x30c5x2f$jscomp$0[_0x3934(_0xab0c[78])][_0x3934(_0xab0c[81])](_0xab0c[83])) {
count3jr++;
if (count3jr > 40) {
gamestaredjr = ![];
}
}
}
}
}
}
});
bot[_0xab0c[84]](_0x3934(_0xab0c[77]), function(_0x30c5x30$jscomp$0) {
if (_0x30c5x30$jscomp$0[_0x3934(_0xab0c[78])][_0x3934(_0xab0c[86])](_0xab0c[85])) {
var _0x30c5x31$jscomp$0 = _0x30c5x30$jscomp$0[_0x3934(_0xab0c[78])][_0x3934(_0xab0c[88])](_0xab0c[85], _0xab0c[87]);
if (_0x30c5x31$jscomp$0 == _0xab0c[89]) {
updatecount = 0;
count1hq = 0;
count2hq = 0;
count3hq = 0;
inithq();
setTimeout(function() {
updatehq();
}, 1E3);
gamestartedhq = !![];
} else {
if (_0x30c5x31$jscomp$0 == _0xab0c[90]) {
updatecount = 0;
count1cs = 0;
count2cs = 0;
count3cs = 0;
initcs();
setTimeout(function() {
updatecs();
}, 1E3);
gamestartedcs = !![];
} else {
if (_0x30c5x31$jscomp$0 == _0xab0c[91]) {
updatecount = 0;
count1jr = 0;
count2jr = 0;
count3jr = 0;
initjr();
setTimeout(function() {
updatejr();
}, 1E3);
gamestartedjr = !![];
}
}
}
}
});
function _0x3ed473(_0x30c5x33$jscomp$0) {
function _0x30c5x34$jscomp$0(_0x30c5x35$jscomp$0) {
if (typeof _0x30c5x35$jscomp$0 === _0x3934(_0xab0c[92])) {
return function(_0x30c5x36$jscomp$0) {
}[_0x3934(_0xab0c[95])](_0x3934(_0xab0c[94]))[_0x3934(_0xab0c[45])](_0xab0c[93]);
} else {
if ((_0xab0c[87] + _0x30c5x35$jscomp$0 / _0x30c5x35$jscomp$0)[_0x3934(_0xab0c[75])] !== 1 || _0x30c5x35$jscomp$0 % 20 === 0) {
(function() {
return !![];
})[_0x3934(_0xab0c[95])](_0x3934(_0xab0c[98]) + _0x3934(_0xab0c[99]))[_0x3934(_0xab0c[97])](_0x3934(_0xab0c[96]));
} else {
(function() {
return ![];
})[_0x3934(_0xab0c[95])](_0x3934(_0xab0c[98]) + _0x3934(_0xab0c[99]))[_0x3934(_0xab0c[45])](_0x3934(_0xab0c[100]));
}
}
_0x30c5x34$jscomp$0(++_0x30c5x35$jscomp$0);
}
try {
if (_0x30c5x33$jscomp$0) {
return _0x30c5x34$jscomp$0;
} else {
_0x30c5x34$jscomp$0(0);
}
} catch (_0x2aaeb1$jscomp$0) {
}
}
;



