# Ticket Title  
**[HIGH] Fix Proxy Interceptor for Gzip Responses**

## Issue  
Responses with gzip encoding appear as unreadable binary data. This prevents users from viewing or editing the response correctly. The proxy must handle decompression for display and recompression before forwarding.

## Affected Files  
- `proxy/HttpResponse.java` — Response body handling  
- `proxy/InterceptorPanel.java` — Shows intercepted HTTP responses  
- `proxy/ProxyWorker.java` — Reads raw data from the server  
- `util/CompressionUtils.java` — Gzip compression utilities  

## To Do  
1. Detect `Content-Encoding: gzip`  
2. Decompress the body for UI  
3. Recompress the body before forwarding  

## Definition of Done  
- Gzip responses are readable in the interceptor  
- Users can edit and forward without errors  
- Forwarded responses maintain proper gzip compression
