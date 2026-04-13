# Ticket Title  
**[HIGH] Enable Gzip Decoding in Proxy Interceptor**

## Problem  
HTTP responses with `Content-Encoding: gzip` are currently unreadable in the interceptor. Users cannot inspect, edit, or forward these responses correctly. The proxy must automatically decompress gzip responses for display and recompress them before forwarding.

## Related Files  
- `proxy/HttpResponse.java` — Response parsing and storage  
- `proxy/InterceptorPanel.java` — Displays intercepted responses  
- `proxy/ProxyWorker.java` — Reads raw server data  
- `util/CompressionUtils.java` — Gzip utility functions  

## Tasks  
1. Detect `Content-Encoding: gzip` in response headers  
2. Decompress body for interceptor display  
3. Recompress body before forwarding to client  

## Acceptance Criteria  
- Gzip responses display correctly  
- Users can edit and forward responses without errors  
- Forwarded responses maintain correct gzip encoding
