import SwiftUI

struct DetailView: View {
    let url: String?
    
    var body: some View {
        //  We creating a Web View from UIKit component called WKWebView    ->  makeUIView
        WebView(urlString: url)
    }
}

struct DetailView_Previews: PreviewProvider {
    static var previews: some View {
        DetailView(url: "https://www.google.com")
    }
}
