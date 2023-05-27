<p align="center">
  <span>
    <img src="https://assets.vercel.com/image/upload/v1588805858/repositories/vercel/logo.png" height="96">
    <h3 align="center">Next.js <b>Typesafe</b> FastAPI Starter</h3>
  </span>
</p>

<p align="center">Simple Next.js boilerplate that uses <a href="https://fastapi.tiangolo.com/lo/">FastAPI</a> as the API backend.</p>

<br/>

## Introduction

This is a hybrid Next.js + Python app that uses Next.js as the frontend and FastAPI as the API backend. One great use case of this is to write Next.js apps that use Python AI libraries on the backend. Furthermore, this automatically generates an OpenAPI schema achieve typesafety between API and frontend.

## How It Works

The Python/FastAPI server is mapped into to Next.js app under `/api/`.

This is implemented using [`next.config.js` rewrites]() to map any request to `/api/:path*` to the Flask API, which is hosted in the `/api` folder.

On dev mode (localhost), the rewrite will be made to the `127.0.0.1:8000` port, which is where the FastAPI server is running.
When you save your index.py file, a openAPI schema is automatically generated, and nodemon intercepts this new file to generate new TS types.

Example: change a server python field from ["name" to "full_name"](https://imgur.com/SMDNPZa), and your frontend [typescript starts complaining](https://imgur.com/aIwae4v). <i>Note: Tested on MacOS/Unix only, Windows might need some tweaks.</i>

In production, the FastAPI server is hosted as [Python serverless functions](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python) on Vercel.

## Demo

## Deploy Your Own

You can clone & deploy it to Vercel with one click:

## Developing Locally

You can clone & create this repo with the following command

## Getting Started

First, install the dependencies:

```bash
npm install
# or
yarn
# or
pnpm install
```

Then, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The FastAPI server will be running on [http://127.0.0.1:8000](http://127.0.0.1:8000) – feel free to change the port in `package.json` (you'll also need to update it in `next.config.js`).

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - learn about FastAPI features and API.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!