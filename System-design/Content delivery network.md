A CDN is a globally distributed set of networks or servers, which help in streaming the content from the nearest server so that it reduces time and load on the origin servers. It can also help in load management by allowing the users at will when there is a traffic increase.

There are 2 ways of changing the information in the CDN edge servers which are normally replicated from the origin servers. But when the information or content is updated in main servers, the we use:

Push CDNs: Where the new update is pushed into all the CDN servers simultaneously by the content owner and the CDN will now stream new content. This requires more initial setup and more maintenance but is very cheap and affordable. This type of CDN is normally used for static pages and content where there are no much changes. Ex: Akamai, 

Pull CDNs: These are cache based CDNs, where mostly the content is requested only when the user asks for it, So it fetches the new content and caches the new content for itself until its expiry (TTL) or there is another update to the content. Its mainly used for dynamic content. Examples: Cloudflare or Amazon Cloud front

![[Screenshot 2026-07-01 at 2.53.06 PM.png]]