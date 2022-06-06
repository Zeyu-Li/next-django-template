/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

// appends global share for all files so they can be shared (ie shared colours and mixins)
module.exports = (phase, { defaultConfig }) => {
  if ('sassOptions' in defaultConfig) {
    defaultConfig['sassOptions'] = {
      includePaths: ['./src'],
      prependData: `
        @import "styles/_shared.scss";
      `,
    }
  }
  return defaultConfig
}
