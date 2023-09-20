import UIKit

struct PasswordGen {
    
    var hardnessSegment: Int?
    var numberOfSymbols: Int = 0
    var passwordPrefix: String?
    
    let alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    let numArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    let specialSymbols = ["=", "_", "-", "#", "@", "!", "%", "&", "*", "(", ")", "$"]

    var resultPassword: String?
    
    mutating func generatePassword() -> String {
        
        if hardnessSegment == 0 {
            let letters = (alphabet.shuffled()).prefix(numberOfSymbols)
            resultPassword = letters.joined(separator: "")
            
            return resultPassword!
        }
        
        
        else if hardnessSegment == 1 {
            var lettersAndNums = alphabet
            lettersAndNums += numArray
            resultPassword = ( (lettersAndNums.shuffled()).prefix(numberOfSymbols) ).joined(separator: "")

            return resultPassword!
        }
        
        else {
            var everyTypeSymbolAlphabet = [String]()
            
            everyTypeSymbolAlphabet += specialSymbols
            everyTypeSymbolAlphabet += numArray
            everyTypeSymbolAlphabet += alphabet
            everyTypeSymbolAlphabet += alphabet.map{$0.uppercased()}
            
            resultPassword = ( everyTypeSymbolAlphabet.shuffled().prefix(numberOfSymbols) ).joined(separator: "")
            
            return resultPassword!
        }
        
    }
    
}




