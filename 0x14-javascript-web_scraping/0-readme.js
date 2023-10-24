#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (erorr, data) => {
	if (error) {
		console.error(error);
		return;
	}
	console.log(data);
});
