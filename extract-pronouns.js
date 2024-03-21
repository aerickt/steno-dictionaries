const fs = require('fs');

// Read the lapwing-base.json file
fs.readFile('lapwing-base.json', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }

  try {
    // Parse the JSON data
    const jsonData = JSON.parse(data);

    // Partition the data into two objects
    const nonPrefixedProperNouns = {};
    const baseNoPronouns = {};

    for (const key in jsonData) {
      if (key.startsWith('#')) {
        nonPrefixedProperNouns[key] = jsonData[key];
      } else {
        baseNoPronouns[key] = jsonData[key];
      }
    }

    // Write the partitioned objects into separate files
    fs.writeFile('lapwing-non-prefixed-proper-nouns.json', JSON.stringify(nonPrefixedProperNouns, null, 2), (err) => {
      if (err) {
        console.error('Error writing file:', err);
      } else {
        console.log('lapwing-non-prefixed-proper-nouns.json written successfully.');
      }
    });

    fs.writeFile('lapwing-base-no-pronouns.json', JSON.stringify(baseNoPronouns, null, 2), (err) => {
      if (err) {
        console.error('Error writing file:', err);
      } else {
        console.log('lapwing-base-no-pronouns.json written successfully.');
      }
    });

  } catch (error) {
    console.error('Error parsing JSON:', error);
  }
});
