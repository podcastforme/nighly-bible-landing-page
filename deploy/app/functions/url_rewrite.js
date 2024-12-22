function handler(event) {
    var request = event.request;
    var uri = request.uri;
    
    // Check if the URI doesn't end with a pattern like /something.something
    if (!uri.match(/\/[^\/]+\.[^\/]+$/)) {
        // Remove trailing slash if present
        uri = uri.replace(/\/$/, '');
        // Add /index.html
        uri = uri + '/index.html';
    }
    
    request.uri = uri;
    return request;
}
