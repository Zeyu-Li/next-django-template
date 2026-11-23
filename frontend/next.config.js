/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // static HTML export into out/ (replaces the removed `next export` command)
  output: 'export',
  // `next dev` only serves HMR/dev assets to these hosts (the traefik alias used by `make up`)
  allowedDevOrigins: ['next-django-template.test'],
  // appends global share for all files so they can be shared (ie shared colours and mixins)
  sassOptions: {
    loadPaths: [__dirname],
    additionalData: `
      @import "styles/_shared.scss";
    `,
  },
}

module.exports = nextConfig
