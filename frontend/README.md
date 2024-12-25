## Frontend for OAuth Sandbox

### Install React via Vite

```sh
npm create vite@latest frontend                                                                                                ✔  22:11:38 

✔ Select a framework: › React
✔ Select a variant: › TypeScript
```

### Install libraries

```sh
npm install -D @types/node
npm install -D @inertiajs/react
```

### Install formatter and linter

```sh
npm install --save-dev --save-exact @biomejs/biome

npx @biomejs/biome init
npx biome migrate eslint --write
npx biome migrate prettier --write
```