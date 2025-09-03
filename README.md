# www.jrishaug.com
Code for my personal site.

Currently based on a fork of [jekyll-now](https://github.com/barryclark/jekyll-now).

### SSL
SSL terminates in Cloudflare, set up according to [this guide](https://sheharyar.me/blog/free-ssl-for-github-pages-with-custom-domains/)

A [Cloudflare post](https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/) about 
providing full(stric) ssl termination that could also be helpful. I couldn't get this completely working,
but I learned some great things like CNAME-flattening from it.

This is worth revisiting if Github ever starts supporting SSL for custom domain sites.

### TODO
1. Parse quotes from images
2. Parse highlight exports from kindle, and add to quotes
3. Separate quotes / favorites into categories of "fiction books", "non-fiction books", Videos, Podcasts, Comments, Articles, etc.
