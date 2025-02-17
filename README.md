# Repo Contents

Copy contents of repository into a single file.

Reason for use is to copy code base into a single file for use in LLM.

## Usage

```bash
python repo_contents.py <repository_path>
```

## Docker Container Usage

```bash
docker run --rm -v /path/to/repo-contents:/app -v /path/to/codebase:/data -w /app python:3.11-slim python repo_contents.py /data
```

## Example Output

Text will be output to `repository_contents.txt` in the repository root.

```txt
File: /data/repository_contents.txt


File: /data/package.json
{
  "name": "starter-template",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview",
    "storybook": "storybook dev -p 6006 --host 0.0.0.0",
    "build-storybook": "storybook build"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@storybook/addon-essentials": "^7.6.17",
    "@storybook/addon-interactions": "^7.6.17",
    "@storybook/addon-links": "^7.6.17",
    "@storybook/addon-onboarding": "^1.0.11",
    "@storybook/blocks": "^7.6.17",
    "@storybook/react": "^7.6.17",
    "@storybook/react-vite": "^7.6.17",
    "@storybook/test": "^7.6.17",
    "@types/react": "^18.2.56",
    "@types/react-dom": "^18.2.19",
    "@vitejs/plugin-react": "^4.2.1",
    "eslint": "^8.56.0",
    "eslint-plugin-react": "^7.33.2",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "eslint-plugin-storybook": "^0.8.0",
    "storybook": "^7.6.17",
    "vite": "^5.1.4"
  }
}

File: /data/vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 5173,
  }
}) 

...
```

## Ignore Files

Files can be ignored by adding them to the `.repoignore` file and listing any files or directories to ignore.

Example `.repoignore` file:
```txt
.repoignore
node_modules
dist
build
```
