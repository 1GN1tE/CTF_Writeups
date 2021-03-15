# reklest

In our infrastructure it works perfectly but it takes time
http://reklest.web.jctf.pro

Attachments:
* [reklest](./reklest)

## Solution
- Rust Binary for MacOS
- It generates a hardcoded string by xor
- It base64 decodes the string and performs `get`
```python
import base64
vals = [0xA884DF8AB2FBC902, 0xE0D28ACBFB46461A, 0x6178F0BE4CD508AC, 0x603AD81291B66724, 0xDE5CDDE19279A148, 0x70E60361F80E8EB4]

to_xor = [0xD8BDEEE9C2938E66, 0xD598D291C97F7779, 0x0D32C3E736983BF4, 0x0C428F73FC8F2140, 0xA419A7AFE834F505, 0x4DAB6D008D6DF4F9]

def xor(a,b):
	c = 0
	for i in range(8):
		tmp1 = (a >> 8*i) & 0xFF
		tmp2 = (b >> 8*i) & 0xFF
		tmp3 = (tmp1 ^ tmp2)
		c = (c << 8) | tmp3
	return c

to_dec = b""
for i in range(6):
	tmp = hex(xor(vals[i],to_xor[i]))[2:]
	to_dec += bytes.fromhex(tmp)

print(base64.b64decode(to_dec).decode())
```

[this_is_very_s3cret_file13371337.js](http://reklest.web.jctf.pro/this_is_very_s3cret_file13371337.js)

We get a JS
```javascript
var _0x38d9 = [
	'charCodeAt',
	'537865HVvFyd',
	'153402TvesmL',
	'637814tgMjYr',
	'191740qwGPgk',
	'length',
	'21541OOTfbk',
	'2FaFWFo',
	'4DOGutk',
	'21qyUBwr',
	'500024opEyBW',
	'2669431PGatTv'
];
var _0x2b2f = function (_0x20b4d4, _0x6e7ec) {
	_0x20b4d4 = _0x20b4d4 - 104;
	var _0x38d9ae = _0x38d9[_0x20b4d4];
	return _0x38d9ae;
};
(function (_0x610c0b, _0x118d97) {
	var _0xdf5613 = _0x2b2f;
	while (!![]) {
		try {
			var _0x51bf5f = parseInt(_0xdf5613(114)) + parseInt(_0xdf5613(111)) + -parseInt(_0xdf5613(109)) * -parseInt(_0xdf5613(115)) + parseInt(_0xdf5613(104)) + -parseInt(_0xdf5613(110)) * -parseInt(_0xdf5613(107)) + parseInt(_0xdf5613(108)) * parseInt(_0xdf5613(105)) + -parseInt(_0xdf5613(112));
			console.log(_0x51bf5f);
			if (_0x51bf5f === _0x118d97){
				console.log(_0x610c0b);
				break;
			}
			else{
				_0x610c0b['push'](_0x610c0b['shift']());
			}
		} catch (_0x41e7a9) {
			_0x610c0b['push'](_0x610c0b['shift']());
		}
	}
}(_0x38d9, 455721), text = '{rewJey\0bnF\x05B_EnEC\0RZHnSD\x06nCdbEn]\x01\x01ZBnbR\x05CHL');
```
We get the `_0x38d9` array after the transformations...
`["637814tgMjYr", "191740qwGPgk", "length", "21541OOTfbk", "2FaFWFo", "4DOGutk", "21qyUBwr", "500024opEyBW", "2669431PGatTv", "charCodeAt", "537865HVvFyd", "153402TvesmL"]`

By this we beautify the function `xyz`
```javascript
function xyz(_0x4821d8, _0x1e7b78) {
	var output = '';
	for (var i = 0; i < _0x4821d8['length']; i++) {
		output += String['fromCharCode'](_0x4821d8['charCodeAt'](i) ^ _0x1e7b78['charCodeAt'](i % _0x1e7b78['length']));
	}
	console.log("FLag"+output);
}
```

- So it's basic repeating xor
- Flag starts with `JCTF` so if we xored the `text` with `JCTF` we get `1` 
- xor `text` with `1` we will get the flag

https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'1'%7D,'Standard',false)&input=MHg3YiAweDcyIDB4NjUgMHg3NyAweDRhIDB4NjUgMHg3OSAweDAwIDB4NjIgMHg2ZSAweDQ2IDB4MDUgMHg0MiAweDVmIDB4NDUgMHg2ZSAweDQ1IDB4NDMgMHgwMCAweDUyIDB4NWEgMHg0OCAweDZlIDB4NTMgMHg0NCAweDA2IDB4NmUgMHg0MyAweDY0IDB4NjIgMHg0NSAweDZlIDB4NWQgMHgwMSAweDAxIDB4NWEgMHg0MiAweDZlIDB4NjIgMHg1MiAweDA1IDB4NDMgMHg0OCAweDRjIA

## Flag
> JCTF{TH1S_w4snt_tr1cky_bu7_rUSt_l00ks_Sc4ry}
