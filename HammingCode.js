const fs = require('fs');
const math = require('mathjs');
const path = require('path');

// Hamming (7, 4) Generator and Parity Check Matrices
const Hamming7_4 = {
    generator: math.matrix([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ]),
    parityCheck: math.matrix([
        [1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0]
    ]),
    syndromeToError: {
        '110': 0,
        '101': 1,
        '011': 2,
        '111': 3,
        '100': 4,
        '010': 5,
        '001': 6
    }
};

// Function to read the dataset
async function readDataset(filePath) {
    return fs.promises.readFile(filePath, 'utf8');
}

// Function to decode data using Hamming (7, 4) with error correction
function decodeHamming(data) {
    const { parityCheck, syndromeToError } = Hamming7_4;
    return data.map(row => {
        const inputVector = math.matrix(row);
        const syndrome = math.multiply(parityCheck, inputVector).toArray().map(val => val % 2).join('');
        let correctedRow = row.slice();

        if (syndrome !== '000') {
            const errorBit = syndromeToError[syndrome];
            if (errorBit !== undefined) {
                correctedRow[errorBit] = correctedRow[errorBit] === 0 ? 1 : 0; // Flip the erroneous bit
            }
        }

        const decoded = [correctedRow[0], correctedRow[1], correctedRow[2], correctedRow[3]];
        return { decoded, errorCorrected: syndrome !== '000' };
    });
}

// Function to determine the user's home directory
function getDownloadsFolder() {
    if (process.platform === 'win32') {
        return process.env.USERPROFILE;
    } else {
        return process.env.HOME;
    }
}

// Main function to execute the program
async function main() {
    const downloadsFolder = path.join(getDownloadsFolder(), 'Downloads');
    const filePath = path.join(downloadsFolder, 'output'); // Change this to your actual file

    if (!fs.existsSync(filePath)) {
        console.error(`File not found: ${filePath}`);
        return;
    }

    try {
        const data = await readDataset(filePath);
        const binaryData = data.trim().split('\n').map(line => line.split('').map(Number));

        console.log('Original Encoded Data:', binaryData);

        // Decode the data
        const decodedResults = decodeHamming(binaryData);
        const decodedData = decodedResults.map(result => result.decoded);

        console.log('Decoded Data:', decodedData);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

main();
