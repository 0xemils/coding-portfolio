import SwiftUI

struct ContentView: View {
    @ObservedObject var networkManager = NetworkManager()
    
    var body: some View {
        NavigationView{
            //  For every post in array of posts
            List(networkManager.posts) { post in
                //  NavigationLink is a button (arrow) on the right side of each cell which triggers the presentation to the DetailView
                NavigationLink(
                    destination: DetailView(url: post.url),
                    label: {
                        HStack {
                            Text("\(post.points)")
                            Text(verbatim: post.title)
                        }
                    })
            }
            .navigationBarTitle("H4X0R News")
        }
        //  onAppear method is like viewDidLoad, but in SwiftUI
        //  We define what will be performed, when the var body appears on the screen
        .onAppear {
            self.networkManager.fetchData()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
