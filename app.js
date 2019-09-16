const fs = require('fs');

const node_xj = require('xls-to-json');
// node_xj({
//     input: "Table-S4-career-2018.xlsx",  // input xls
//     output: "authors.json", // output json
//     sheet: "Career",  // specific sheetname
//     rowsToSkip: 0 // number of rows to skip at the top of the sheet; defaults to 0
//   }, function(err, result) {
//     if(err) {
//       console.error(err);
//     } else {
//       console.log(result);
//     }
//   });

node_xj({
    input: "Table-S4-career-2018.xlsx",  // input xls
    output: "authors_descriptions.json", // output json
    sheet: "Key",  // specific sheetname
    rowsToSkip: 0 // number of rows to skip at the top of the sheet; defaults to 0
  }, function(err, result) {
    if(err) {
      console.error(err);
    } else {
      console.log(result);
    }
  });

// fs.writeFileSync('authors.json', JSON.stringify(result));