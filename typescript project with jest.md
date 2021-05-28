## Developer setup

Initialize with [Google Typescript Style (gts)](https://github.com/google/gts)

```bash
npx gts init
npm i
```

### [Jest](https://github.com/facebook/jest)

```bash
npm i -D jest ts-jest @types/jest
```

In `package.json` add the scripts for test and coverage:

```json
  "scripts": {
    "test": "jest",
    "coverage": "jest --coverage",
    ...
  }
```

Add a `jest.config.js` file:

```javascript
module.exports = {
  transform: {'^.+\\.ts?$': 'ts-jest'},
  testEnvironment: 'node',
  testRegex: '/test/.*\\.(test|spec)?\\.(ts|tsx)$',
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node']
};
```

### [Visual Studio Code](https://code.visualstudio.com/)

In `.vscode/launch.json` add configuration to debug tests:

```json
    {
      "type": "node",
      "request": "launch",
      "name": "Jest Current File",
      "program": "${workspaceFolder}/node_modules/.bin/jest",
      "args": ["${relativeFile}"],
      "console": "integratedTerminal",
      "internalConsoleOptions": "neverOpen",
      "windows": {
        "program": "${workspaceFolder}/node_modules/jest/bin/jest"
      }
    }
```

### Optional (but worth it)

Add the [Jest Text Explorer](https://marketplace.visualstudio.com/items?itemName=kavod-io.vscode-jest-test-adapter) extension.

Add [Coverage badge](https://github.com/olavoparno/istanbul-badges-readme) ![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)
