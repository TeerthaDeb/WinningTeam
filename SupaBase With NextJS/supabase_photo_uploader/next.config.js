/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        remotePatterns: [
            {
                protocol: 'https',
                hostname: 'xbjonuklleyhiudplhaw.supabase.co'
            }
        ]
    }
}

module.exports = nextConfig