#!/usr/bin/node

const fs = require('fs');
const arg = fs.readFileSync(process.argv[2], 'utf8');
const b = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], arg + b);
