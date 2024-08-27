const fs = require('fs');
const zlib = require('zlib');
const path = require('path');

function decompressZlibFile(inputFile, outputFile) {
  try {
    const compressedData = fs.readFileSync(inputFile);
    const decompressedData = zlib.unzipSync(compressedData);
    fs.writeFileSync(outputFile, decompressedData);
    console.log(`Decompressed ${inputFile} to ${outputFile}`);
  } catch (err) {
    console.error(`Error decompressing ${inputFile}:`, err.message);
  }
}

const downloadsFolder = path.join(require('os').homedir(), 'Downloads');

const files = [
  { input: path.join(downloadsFolder, '29.zlib'), output: path.join(downloadsFolder, '29_decompressed.txt') },
  { input: path.join(downloadsFolder, '29 (1).zlib'), output: path.join(downloadsFolder, '29(1)_decompressed.txt') },
];

files.forEach(({ input, output }) => {
  decompressZlibFile(input, output);
});
