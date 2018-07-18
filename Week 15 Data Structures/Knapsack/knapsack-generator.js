//This file generates more data sets for the knapsack solver to process.
//It is not a part of any solution to this problem.

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);

if (args.length != 2) {
  console.error("usage: knapsack-generator filename size");
  process.exit(2);
}

let [filename, size] = args;
const filePath = path.resolve(__dirname, filename);

if (fs.existsSync(filePath)) {
  console.error(`File "${filePath}" already exists!`);
  process.exit(2);
}

if (isNaN(size)) {
  console.error(`size must be a number!`);
  process.exit(2);
}

size = ~~Number(size);

let text = '';

for (let i = 1; i <= size; i++)
  text += `${i} ${Math.floor(Math.random() * 101)} ${Math.floor(Math.random() * 101)}${i === size ? '' : '\n'}`;

fs.writeFile(filePath, text, (error) => {
    if(error) {
      console.error('The file could not be saved');
      process.exit(1);
    }

    console.log(`Knapsack problem saved to ${filePath}`);
});
