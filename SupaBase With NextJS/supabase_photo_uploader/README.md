# Next.js Project Setup

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

### Installation

1. Install all dependencies by running:
   ```bash
   npm install
   ```

   - if any error encountered:
   ```bash
   npm audit fix --force
   ```

### Supabase Setup

1. Go to [Supabase](https://supabase.com) and create a new project.
2. Navigate to the API page of your new project.
3. Create a file named `.env.local` in the root of your project and add the following:
   ```env
   NEXT_PUBLIC_SUPABASE_URL=<YOUR_PROJECT_URL>
   NEXT_PUBLIC_SUPABASE_ANON_KEY=<YOUR_PROJECT_API_KEY>
   ```
4. Note your project URL, which should look something like: `https://<unique-identifier>.supabase.co`.

5. Update your `next.config.js` file to allow images from your Supabase project URL:
   ```js
   images: {
       remotePatterns: [
           {
               protocol: 'https',
               hostname: '<unique-identifier>.supabase.co',
           }
       ]
   }
   ```

### Running the Development Server

Run the development server with one of the following commands:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser to see the result.

You can start editing the page by modifying `app/page.js`. The page will automatically update as you make changes.

### Font Optimization

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.
